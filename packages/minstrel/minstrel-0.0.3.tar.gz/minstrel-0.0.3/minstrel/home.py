#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncio import gather
from asyncio import sleep
from itertools import groupby

from quart import Blueprint
from quart import flash
from quart import redirect
from quart import render_template
from quart import url_for
from uscpi import TCP

from .db import get_db

home = Blueprint("home", __name__)


async def sendall(host: str, port: int, sequences: list) -> None:
    async with TCP(host=host, port=port, timeout=5) as client:
        for sequence in sequences:
            command = bytes(sequence["scpi"], encoding="utf8")
            await client.write(command + b"\n")
            await sleep(0.1)  # 100 milliseconds


@home.get("/")
async def index():
    rows = get_db().execute("SELECT * FROM state").fetchall()
    return await render_template("home.html", states=rows)


@home.get("/configure/<int:state_id>")
async def configure(state_id: int):
    rows = (
        get_db()
        .execute(
            """
        SELECT
            instrument.host AS host,
            instrument.port AS port,
            command.scpi AS scpi
        FROM sequence
            INNER JOIN command ON command.id = sequence.command_id
            INNER JOIN instrument ON instrument.id = sequence.instrument_id
            INNER JOIN state ON state.id = sequence.state_id
        WHERE state.id = ?
        """,
            (state_id,),
        )
        .fetchall()
    )
    keyfunc = lambda x: (x["host"], x["port"])
    records = sorted(map(dict, rows), key=keyfunc)
    groups = groupby(records, key=keyfunc)
    coros = [sendall(*p, list(s)) for p, s in groups]
    try:
        await gather(*coros)
        await flash(f"Setup complete.", "success")
    except TimeoutError:
        await flash(f"Timeout Error. Verify instrumentation is powered on.", "error")
    except OSError as e:
        await flash(f"{e}", "failed")
    return redirect(url_for("home.index"))
