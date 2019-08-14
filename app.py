#!/usr/bin/env python
# -*- coding=utf-8 -*-

###
# I use my liked Redis for Job Scheduler.
###

from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from upgrade_ics import upgrade_all_events


@app.route("/", defaults={"path": "app"})
@app.route("/<link:link>")
def catch_all(link):
    return render_template("index.html", link=link)


if __name__ == "__main__":
    app = Flask(__name__, static_folder="app")

    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(upgrade_all_events, "interval", minutes=60)
    scheduler.start()

    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))
