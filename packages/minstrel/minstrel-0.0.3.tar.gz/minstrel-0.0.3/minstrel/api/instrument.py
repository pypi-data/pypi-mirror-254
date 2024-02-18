#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Blueprint
from quart import render_template
from quart import request

from ..db import get_db
from ..slug import slugify
from ..token import token_required

instrument = Blueprint(
    "instrument",
    __name__,
    url_prefix="/api",
)


@instrument.post("/instrument")
@token_required
async def create_instrument():
    """Create instrument."""

    form = (await request.form).copy().to_dict()
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            INSERT INTO instrument (
                slug,
                title,
                host,
                port
            ) VALUES (
                :slug,
                :title,
                :host,
                :port
            )
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Instrument successfully created.", 201


@instrument.get("/instrument/<int:id>")
async def read_instrument(id: int):
    """Read instrument."""

    row = (
        get_db()
        .execute(
            "SELECT * FROM instrument WHERE id = ?",
            (id,),
        )
        .fetchone()
    )
    if not row:
        return "Instrument does not exist.", 404
    return dict(row), 200


@instrument.put("/instrument/<int:id>")
@token_required
async def update_instrument(id: int):
    """Update instrument."""

    form = (await request.form).copy().to_dict()
    form["id"] = id
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            UPDATE instrument SET
                updated_at = CURRENT_TIMESTAMP,
                slug = :slug,
                title = :title,
                host = :host,
                port = :port
            WHERE id = :id
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Instrument successfully updated.", 201


@instrument.delete("/instrument/<int:id>")
@token_required
async def delete_instrument(id: int):
    """Delete instrument."""

    db = get_db()
    db.execute("DELETE FROM instrument WHERE id = ?", (id,))
    db.commit()
    return "Instrument successfully deleted.", 200


@instrument.get("/instrument")
async def list_instruments():
    """List instruments."""

    rows = get_db().execute("SELECT * FROM instrument").fetchall()
    if not rows:
        return "Instruments do not exist.", 404
    return list(map(dict, rows)), 200
