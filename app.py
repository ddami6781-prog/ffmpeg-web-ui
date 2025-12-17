from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        src = request.form.get("source")
        dst = request.form.get("destination")
        try:
            subprocess.Popen([
                "ffmpeg", "-re", "-i", src,
                "-c", "copy", "-f", "flv", dst
            ])
            message = "Streaming started!"
        except Exception as e:
            message = f"Error: {e}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
