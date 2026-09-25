from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        print(request.form)

        name = request.form.get("name")
        email = request.form["email"]
        password = request.form["password"]
        city = request.form["city"]
        language = request.form["language"] 

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (name, email, password, city, language)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, password, city, language)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        print("LOGIN FORM:", request.form)
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
          return render_template(
        "dashboard.html",
        username=user[1]
    )
        else:
           return render_template(
        "login.html",
        error="Invalid Email or Password"
    )

    return render_template("login.html")


# ---------------------------
# Emergency Guidance
# ---------------------------
@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        username="Guest"
    )

@app.route("/heart-attack")
def heart_attack():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT language FROM users WHERE id=1"
    )

    result = cursor.fetchone()

    conn.close()

    language = result[0]

    if language == "Hindi":
        return render_template("heart_attack_hi.html")

    return render_template("heart_attack.html")


@app.route("/burns")
def burns():
    return render_template("burns.html")


@app.route("/snake-bite")
def snake_bite():
    return render_template("snake_bite.html")


@app.route("/bleeding")
def bleeding():
    return render_template("bleeding.html")


@app.route("/choking")
def choking():
    return render_template("choking.html")


# ---------------------------
# Blood Donor Module
# ---------------------------

@app.route("/donor-register", methods=["GET", "POST"])
def donor_register():

    if request.method == "POST":

        name = request.form["name"]
        blood_group = request.form["blood_group"]
        city = request.form["city"]
        phone = request.form["phone"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO donors
            (name, blood_group, city, phone)
            VALUES (?, ?, ?, ?)
            """,
            (name, blood_group, city, phone)
        )

        conn.commit()
        conn.close()

        return "Donor Registered Successfully"

    return render_template("donor_register.html")


@app.route("/search-donor", methods=["GET", "POST"])
def search_donor():

    if request.method == "POST":

        blood_group = request.form["blood_group"]
        city = request.form["city"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM donors
            WHERE LOWER(blood_group)=LOWER(?)
            AND LOWER(city)=LOWER(?)
            """,
            (blood_group, city)
        )

        donors = cursor.fetchall()

        conn.close()

        return render_template(
            "donor_results.html",
            donors=donors
        )

    return render_template("search_donor.html")


# ---------------------------
# Hospital Module
# ---------------------------

@app.route("/add-hospital", methods=["GET", "POST"])
def add_hospital():

    if request.method == "POST":

        hospital_name = request.form["hospital_name"]
        city = request.form["city"]
        address = request.form["address"]
        phone = request.form["phone"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO hospitals
            (hospital_name, city, address, phone)
            VALUES (?, ?, ?, ?)
            """,
            (hospital_name, city, address, phone)
        )

        conn.commit()
        conn.close()

        return "Hospital Added Successfully"

    return render_template("add_hospital.html")


@app.route("/search-hospital", methods=["GET", "POST"])
def search_hospital():

    if request.method == "POST":

        city = request.form["city"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM hospitals
            WHERE LOWER(city)=LOWER(?)
            """,
            (city,)
        )

        hospitals = cursor.fetchall()

        conn.close()

        return render_template(
            "hospital_results.html",
            hospitals=hospitals
        )

    return render_template("search_hospital.html")


# ---------------------------
# Emergency Contacts
# ---------------------------

@app.route("/emergency-contacts")
def emergency_contacts():
    return render_template("emergency_contacts.html")


# ---------------------------
# Run App
# ---------------------------
@app.route("/save-language", methods=["POST"])
def save_language():

    language = request.form["language"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET language=? WHERE id=1",
        (language,)
    )

    conn.commit()
    conn.close()

    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(debug=True)