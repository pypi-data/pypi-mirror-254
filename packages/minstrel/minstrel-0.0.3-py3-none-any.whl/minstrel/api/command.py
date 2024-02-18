#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Blueprint
from quart import render_template
from quart import request

from ..db import get_db
from ..slug import slugify
from ..token import token_required

command = Blueprint(
    "command",
    __name__,
    url_prefix="/api",
)


@command.post("/command")
@token_required
async def create_command():
    """Create command."""

    form = (await request.form).copy().to_dict()
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            INSERT INTO command (
                title,
                slug,
                scpi
            ) VALUES (
                :title,
                :slug,
                :scpi
            )
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Command successfully created.", 201


@command.get("/command/<int:id>")
async def read_command(id: int):
    """Read command."""

    row = (
        get_db()
        .execute(
            "SELECT * FROM command WHERE id = ?",
            (id,),
        )
        .fetchone()
    )
    if not row:
        return "Command does not exist.", 404
    return dict(row), 200


@command.put("/command/<int:id>")
@token_required
async def update_command(id: int):
    """Update command."""

    form = (await request.form).copy().to_dict()
    form["id"] = id
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            UPDATE command SET
                updated_at = CURRENT_TIMESTAMP,
                title = :title,
                slug = :slug,
                scpi = :scpi
            WHERE id = :id
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "Command successfully updated.", 201


@command.delete("/command/<int:id>")
@token_required
async def delete_command(id: int):
    """Delete command."""

    db = get_db()
    db.execute("DELETE FROM command WHERE id = ?", (id,))
    db.commit()
    return "Command successfully deleted.", 200


@command.get("/command")
async def list_commands():
    """List commands."""

    rows = get_db().execute("SELECT * FROM command").fetchall()
    if not rows:
        return "Commands do not exist.", 404
    return list(map(dict, rows)), 200
