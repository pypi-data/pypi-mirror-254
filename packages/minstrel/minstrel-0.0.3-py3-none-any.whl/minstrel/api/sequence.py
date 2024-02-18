#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Blueprint
from quart import render_template
from quart import request

from ..db import get_db
from ..slug import slugify
from ..token import token_required

sequence = Blueprint(
    "sequence",
    __name__,
    url_prefix="/api",
)


@sequence.post("/sequence")
@token_required
async def create_sequence():
    """Create sequence."""

    form = (await request.form).copy().to_dict()
    try:
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            INSERT INTO sequence (
                instrument_id,
                state_id,
                command_id
            ) VALUES (
                :instrument_id,
                :state_id,
                :command_id
            )
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Sequence successfully created.", 201


@sequence.get("/sequence/<int:id>")
async def read_sequence(id: int):
    """Read sequence."""

    row = (
        get_db()
        .execute(
            "SELECT * FROM sequence WHERE id = ?",
            (id,),
        )
        .fetchone()
    )
    if not row:
        return "Sequence does not exist.", 404
    return dict(row), 200


@sequence.put("/sequence/<int:id>")
@token_required
async def update_sequence(id: int):
    """Update sequence."""

    form = (await request.form).copy().to_dict()
    form["id"] = id
    try:
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            UPDATE sequence SET
                updated_at = CURRENT_TIMESTAMP,
                instrument_id = :instrument_id,
                state_id = :state_id,
                command_id = :command_id
            WHERE id = :id
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Sequence successfully updated.", 201


@sequence.delete("/sequence/<int:id>")
@token_required
async def delete_sequence(id: int):
    """Delete sequence."""

    db = get_db()
    db.execute("DELETE FROM sequence WHERE id = ?", (id,))
    db.commit()
    return "Sequence successfully deleted.", 200


@sequence.get("/sequence")
async def list_sequences():
    """List sequences."""

    rows = get_db().execute("SELECT * FROM sequence").fetchall()
    if not rows:
        return "Sequences do not exist.", 404
    return list(map(dict, rows)), 200
