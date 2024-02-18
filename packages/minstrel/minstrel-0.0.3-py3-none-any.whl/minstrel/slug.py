#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub


def slugify(x: str) -> str:
    """
    Convert string into slug.
    """

    x = x.lower().strip()
    x = sub(r"[^\w\s-]", "", x)
    x = sub(r"[\s_-]+", "_", x)
    x = sub(r"^-+|-+$", "", x)
    return x
