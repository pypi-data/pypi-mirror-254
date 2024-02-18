#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Blueprint
from quart import render_template
from quart import request

from ..db import get_db
from ..slug import slugify
from ..token import token_required

state = Blueprint(
    "state",
    __name__,
    url_prefix="/api",
)


@state.post("/state")
@token_required
async def create_state():
    """Create state."""

    form = (await request.form).copy().to_dict()
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            INSERT INTO state (
                title,
                slug
            ) VALUES (
                :title,
                :slug
            )
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "State successfully created.", 201


@state.get("/state/<int:id>")
async def read_state(id: int):
    """Read state."""

    row = (
        get_db()
        .execute(
            "SELECT * FROM state WHERE id = ?",
            (id,),
        )
        .fetchone()
    )
    if not row:
        return "State does not exist.", 404
    return dict(row), 200


@state.put("/state/<int:id>")
@token_required
async def update_state(id: int):
    """Update state."""

    form = (await request.form).copy().to_dict()
    form["id"] = id
    try:
        form["slug"] = slugify(form.get("title"))
        db = get_db()
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            UPDATE state SET
                updated_at = CURRENT_TIMESTAMP,
                title = :title,
                slug = :slug
            WHERE id = :id
            """,
            form,
        )
        db.commit()
    except db.ProgrammingError:
        return "Missing parameter(s).", 400
    except db.IntegrityError:
        return "Invalid parameter(s).", 400
    return "State successfully updated.", 201


@state.delete("/state/<int:id>")
@token_required
async def delete_state(id: int):
    """Delete state."""

    db = get_db()
    db.execute("DELETE FROM state WHERE id = ?", (id,))
    db.commit()
    return "State successfully deleted.", 200


@state.get("/state")
async def list_states():
    """List states."""

    rows = get_db().execute("SELECT * FROM state").fetchall()
    if not rows:
        return "States do not exist.", 404
    return list(map(dict, rows)), 200
