from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Kamal Barman", profession="Python Developer Intern")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # For now, just print in terminal (in real-world, save to DB or send email)
        print(f"Message from {name} ({email}): {message}")
        return redirect(url_for("success"))

    return render_template("contact.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
