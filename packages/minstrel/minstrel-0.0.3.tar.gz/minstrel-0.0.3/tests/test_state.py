#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from sqlite3 import connect
from tempfile import NamedTemporaryFile
from unittest import IsolatedAsyncioTestCase
from unittest import main

from minstrel import create_app


class StateTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls._resources = Path(__file__).parent
        path = cls._resources / "preload.sql"
        with open(path, mode="r", encoding="utf-8") as f:
            cls._preload = f.read()

    def setUp(self):
        self.db = NamedTemporaryFile()
        self.app = create_app({"TESTING": True, "DATABASE": self.db.name})
        self.client = self.app.test_client()
        self.app.test_cli_runner().invoke(args=["init-db"])
        db = connect(self.db.name)
        db.executescript(self._preload)
        resp = self.app.test_cli_runner().invoke(args=["token"])
        self.token = resp.output.rstrip()

    def tearDown(self):
        self.db.close()

    async def test_create_state(self):
        response = await self.client.post(
            f"/api/state?token={self.token}",
            form={"title": "state 2"},
        )
        self.assertEqual(response.status_code, 201)

    async def test_read_state(self):
        response = await self.client.get("/api/state/1")
        self.assertEqual(response.status_code, 200)

    async def test_update_state(self):
        response = await self.client.put(
            f"/api/state/1?token={self.token}",
            form={"title": "state 1_"},
        )
        self.assertEqual(response.status_code, 201)

    async def test_delete_state(self):
        response = await self.client.delete(
            f"/api/state/1?token={self.token}",
        )
        self.assertEqual(response.status_code, 200)

    async def test_list_states(self):
        response = await self.client.get("/api/state")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
