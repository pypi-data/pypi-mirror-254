# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Shared RDM.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_override import InvenioOverride


def test_version():
    """Test version import."""
    from invenio_override import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioOverride(app)
    assert "invenio-override" in app.extensions

    app = Flask("testapp")
    ext = InvenioOverride()
    assert "invenio-override" not in app.extensions
    ext.init_app(app)
    assert "invenio-override" in app.extensions


def test_app(app):
    """Test extension initialization."""
    _ = InvenioOverride(app)
