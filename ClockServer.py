from flask import Flask, Response
from datetime import datetime
import time
app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/streams')


def return_time():
    time.sleep(1)
    time_now = str(datetime.now().time()).split(".")

    return time_now[0]


@app.route("/")
def static_clock():
    time_string = str(datetime.now().time()).split(".")
    return Response("Hello, the current time is: " + time_string[0], mimetype='text')


@app.route("/dynamicClock")
def dynamic_clock():
    def event_stream():
        while True:
            yield return_time() + "\n"
    return Response(event_stream(), mimetype="text/event-stream")


@app.route("/whoami")
def who_am_i():
    return Response("You are Sean!", mimetype="text")

def boot_app():
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    boot_app()