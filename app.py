from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps

from src.feature_extraction import FeatureExtractor
from src.predict import predict

# =====================================
# Flask App Configuration
# =====================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "phishshield_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# =====================================
# Temporary Scan History
# =====================================

history = []

# =====================================
# User Model
# =====================================

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)


with app.app_context():
    db.create_all()


# =====================================
# Login Required Decorator
# =====================================

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:

            flash("Please login first.", "warning")

            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


# =====================================
# Home Route
# =====================================

@app.route("/")
def home():

    if "user" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# =====================================
# Signup
# =====================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        name = request.form["name"].strip()

        email = request.form["email"].strip().lower()

        password = request.form["password"]

        confirm_password = request.form["confirm_password"]

        # Password Match Check
        if password != confirm_password:

            flash("Passwords do not match.", "danger")

            return redirect(url_for("signup"))

        # Existing Email Check
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Email already exists.", "danger")

            return redirect(url_for("signup"))

        # Hash Password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Save User
        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please login.", "success")

        return redirect(url_for("login"))

    return render_template("signup.html")


# =====================================
# Login
# =====================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        email = request.form["email"].strip().lower()

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            session["user"] = user.name
            session["email"] = user.email

            flash(f"Welcome {user.name}!", "success")

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password.", "danger")

    return render_template("login.html")


# =====================================
# Logout
# =====================================

@app.route("/logout")
@login_required
def logout():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))

# =====================================
# Dashboard
# =====================================

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():

    result = None
    confidence = None
    features = {}
    url = ""

    if request.method == "POST":

        url = request.form.get("url")

        if url:

            extractor = FeatureExtractor(url)

            features = extractor.extract()

            result, confidence = predict(features)

            history.append({
                "url": url,
                "result": result,
                "confidence": confidence
            })

    return render_template(
        "dashboard.html",
        url=url,
        result=result,
        confidence=confidence,
        features=features
    )


# =====================================
# Scan Redirect
# =====================================

@app.route("/scan")
@login_required
def scan():

    return redirect(url_for("dashboard"))


# =====================================
# Analytics
# =====================================

@app.route("/analytics")
@login_required
def analytics():

    safe = len([x for x in history if "Legitimate" in x["result"]])

    phishing = len([x for x in history if "Phishing" in x["result"]])

    return render_template(
        "analytics.html",
        total=len(history),
        safe=safe,
        phishing=phishing
    )


# =====================================
# History
# =====================================

@app.route("/history")
@login_required
def history_page():

    return render_template(
        "history.html",
        history=history
    )


# =====================================
# Reports
# =====================================

@app.route("/reports")
@login_required
def reports():

    return render_template("reports.html")


# =====================================
# Settings
# =====================================

@app.route("/settings")
@login_required
def settings():

    return render_template("settings.html")


# =====================================
# About
# =====================================

@app.route("/about")
def about():

    return render_template("about.html")


# =====================================
# Run App
# =====================================

if __name__ == "__main__":

    app.run(debug=True, port=5001)