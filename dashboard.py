from flask import Flask, render_template, request
import asyncio
from async_scanner import run_scan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None

    if request.method == "POST":
        try:
            target = request.form.get("target", "localhost")
            start = int(request.form.get("start", 1))
            end = int(request.form.get("end", 1024))

            if start < 1 or end > 65535 or start > end:
                raise ValueError("Invalid port range")

            results = asyncio.run(run_scan(target, start, end, quiet=True))
            results = sorted(results, key=lambda x: x["port"])

        except Exception as e:
            error = str(e)

    return render_template("index.html", results=results, error=error)


if __name__ == "__main__":
    app.run(debug=True)
