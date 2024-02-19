#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from typing import Any

from flask import Blueprint, Flask

# version is same as tabler-icons
__version__ = "2.47.0"


class TablerIcons:
    def __init__(self, app: Any = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions["tabler_icons"] = self
        bp = Blueprint(
            "tabler_icons",
            __name__,
            static_folder="static",
            static_url_path=f"/tabler-icons{app.static_url_path}",
            template_folder="templates",
        )
        app.register_blueprint(bp)
        app.jinja_env.globals["tabler_icons"] = self
        app.config.setdefault("TABLER_ICON_SIZE", 24)
