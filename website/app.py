from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
@app.get("/index.html")
def home():
    return render_template("index.html")

@app.get("/admin")
@app.get("/admin.html")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
