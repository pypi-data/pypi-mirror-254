#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Blueprint
from quart import flash
from quart import redirect
from quart import render_template
from quart import request
from quart import url_for

from .db import get_db
from .api.command import create_command as create_command_api
from .api.command import update_command as update_command_api
from .api.command import delete_command as delete_command_api
from .api.instrument import create_instrument as create_instrument_api
from .api.instrument import update_instrument as update_instrument_api
from .api.instrument import delete_instrument as delete_instrument_api
from .api.sequence import create_sequence as create_sequence_api
from .api.sequence import update_sequence as update_sequence_api
from .api.sequence import delete_sequence as delete_sequence_api
from .api.state import create_state as create_state_api
from .api.state import update_state as update_state_api
from .api.state import delete_state as delete_state_api

settings = Blueprint("settings", __name__)


@settings.get("/settings")
async def index():
    states = get_db().execute("SELECT * FROM state").fetchall()
    instruments = get_db().execute("SELECT * FROM instrument").fetchall()
    commands = get_db().execute("SELECT * FROM command").fetchall()
    sequences = (
        get_db()
        .execute(
            """
        SELECT
            sequence.id AS id,
            sequence.command_id AS command_id,
            sequence.instrument_id AS instrument_id,
            sequence.state_id AS state_id,
            command.title AS command_title,
            instrument.title AS instrument_title,
            state.title AS state_title
        FROM sequence
            INNER JOIN state ON state.id = sequence.state_id
            INNER JOIN instrument ON instrument.id = sequence.instrument_id
            INNER JOIN command ON command.id = sequence.command_id
        """
        )
        .fetchall()
    )
    return await render_template(
        "settings.html",
        commands=commands,
        states=states,
        instruments=instruments,
        sequences=sequences,
    )


@settings.route("/settings/instrument/create", methods=("GET", "POST"))
async def create_instrument():
    if request.method == "POST":
        response = await create_instrument_api.__wrapped__()
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    return await render_template("create_instrument.html")


@settings.route("/settings/instrument/<int:id>/update", methods=("GET", "POST"))
async def update_instrument(id: int):
    if request.method == "POST":
        response = await update_instrument_api.__wrapped__(id)
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    row = get_db().execute("SELECT * FROM instrument WHERE id = ?", (id,)).fetchone()
    return await render_template("update_instrument.html", row=row)


@settings.route("/settings/instrument/<int:id>/delete", methods=("GET",))
async def delete_instrument(id: int):
    response = await delete_instrument_api.__wrapped__(id)
    if response[1] >= 300:
        await flash(response[0], "error")
    return redirect(url_for(".index"))


@settings.route("/settings/state/create", methods=("GET", "POST"))
async def create_state():
    if request.method == "POST":
        response = await create_state_api.__wrapped__()
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    return await render_template("create_state.html")


@settings.route("/settings/state/<int:id>/update", methods=("GET", "POST"))
async def update_state(id: int):
    if request.method == "POST":
        response = await update_state_api.__wrapped__(id)
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    row = get_db().execute("SELECT * FROM state WHERE id = ?", (id,)).fetchone()
    return await render_template("update_state.html", row=row)


@settings.route("/settings/state/<int:id>/delete", methods=("GET",))
async def delete_state(id: int):
    response = await delete_state_api.__wrapped__(id)
    if response[1] >= 300:
        await flash(response[0], "error")
    return redirect(url_for(".index"))


@settings.route("/settings/command/create", methods=("GET", "POST"))
async def create_command():
    if request.method == "POST":
        response = await create_command_api.__wrapped__()
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    return await render_template("create_command.html")


@settings.route("/settings/command/<int:id>/update", methods=("GET", "POST"))
async def update_command(id: int):
    if request.method == "POST":
        response = await update_command_api.__wrapped__(id)
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    row = get_db().execute("SELECT * FROM command WHERE id = ?", (id,)).fetchone()
    return await render_template("update_command.html", row=row)


@settings.route("/settings/command/<int:id>/delete", methods=("GET",))
async def delete_command(id: int):
    response = await delete_command_api.__wrapped__(id)
    if response[1] >= 300:
        await flash(response[0], "error")
    return redirect(url_for(".index"))


@settings.route("/settings/sequence/create", methods=("GET", "POST"))
async def create_sequence():
    if request.method == "POST":
        response = await create_sequence_api.__wrapped__()
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    commands = get_db().execute("SELECT * FROM command").fetchall()
    states = get_db().execute("SELECT * FROM state").fetchall()
    instruments = get_db().execute("SELECT * FROM instrument").fetchall()
    return await render_template(
        "create_sequence.html",
        instruments=instruments,
        states=states,
        commands=commands,
    )


@settings.route("/settings/sequence/<int:id>/update", methods=("GET", "POST"))
async def update_sequence(id: int):
    if request.method == "POST":
        response = await update_sequence_api.__wrapped__(id)
        if response[1] < 300:
            return redirect(url_for(".index"))
        await flash(response[0], "error")
    row = get_db().execute("SELECT * FROM sequence WHERE id = ?", (id,)).fetchone()
    commands = get_db().execute("SELECT * FROM command").fetchall()
    states = get_db().execute("SELECT * FROM state").fetchall()
    instruments = get_db().execute("SELECT * FROM instrument").fetchall()
    return await render_template(
        "update_sequence.html",
        row=row,
        instruments=instruments,
        states=states,
        commands=commands,
    )


@settings.route("/settings/sequence/<int:id>/delete", methods=("GET",))
async def delete_sequence(id: int):
    response = await delete_sequence_api.__wrapped__(id)
    if response[1] >= 300:
        await flash(response[0], "error")
    return redirect(url_for(".index"))
