from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tools")
def tools():
    return render_template("tools.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
