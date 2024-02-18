# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 sharedRDM.
#
# invenio-override  is free software.

"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "invenio-override-theme": "./less/invenio_override/theme.less",
                "invenio-override-js": "./js/invenio_override/theme.js",
            },
            dependencies={
                # add any additional npm dependencies here...
            },
        )
    },
)
