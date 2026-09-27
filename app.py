from flask import Flask, request, render_template_string

app = Flask(__name__)

CORRECT_PASSWORD = "123"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cybersecurity Login Demo</title>
</head>
<body>
    <h2>Simple Login Page</h2>

    <form method="POST">
        <label>Enter 3-digit password:</label>
        <input type="password" name="password" maxlength="3" required>
        <button type="submit">Login</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password", "")

        if password == CORRECT_PASSWORD:
            return render_template_string(
                HTML, message="Login successful!"
            )

        return render_template_string(
            HTML, message="Invalid password"
        )

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)