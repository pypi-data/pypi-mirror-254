#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from flask import Flask, render_template
from flask_tabler_icons import TablerIcons

app = Flask(__name__)
TablerIcons(app)


@app.route("/")
def index():
    return render_template("index.html")
