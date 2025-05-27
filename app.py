from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os, re

app = Flask(__name__)

# ── Database Configuration ────────────────────────────────────
db_config = {
    "host":     os.getenv("DB_HOST", "db"),
    "dbname":   os.getenv("DB_NAME", "cycling_buddy"),
    "user":     os.getenv("DB_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "PostgresSQLthomas1")
}


# Mapping integer → label
skill_map = {0: "Beginner", 1: "Intermediate", 2: "Advanced"}

# Regex for exactly 4 digits
postal_pattern = re.compile(r"^\d{4}$")

# ── Homepage / Search ─────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        postal_input = request.form.get("postal_codes", "")
        skill_input  = request.form.get("skill_level", "all")
    else:
        postal_input = request.args.get("postal_codes", "")
        skill_input  = request.args.get("skill_level", "all")

    users = []

    query  = """
        SELECT username, id, email, skill_level, postal_code
        FROM users
        WHERE TRUE
    """
    params = []

    # Postal codes (validated)
    postal_list = [p.strip() for p in postal_input.split(",") if postal_pattern.match(p.strip())]
    if postal_list:
        placeholders = ",".join(["%s"] * len(postal_list))
        query += f" AND postal_code IN ({placeholders})"
        params.extend(postal_list)

    # Skill level
    if skill_input != "all":
        query += " AND skill_level = %s"
        params.append(int(skill_input))

    try:
        with psycopg2.connect(**db_config) as conn, conn.cursor() as cur:
            cur.execute(query, params)
            users = cur.fetchall()
    except psycopg2.Error as e:
        return f"Error connecting to the database: {e.pgerror}"

    return render_template(
        "index.html",
        users=users,
        postal_input=postal_input,
        skill_input=skill_input,
        skill_map=skill_map
    )

# ── Sign‑up ‑ Create New User ────────────────────────────────
@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username    = request.form.get("username", "").strip()
        email       = request.form.get("email", "").strip()
        skill_level = request.form.get("skill_level", "").strip()
        postal_code = request.form.get("postal_code", "").strip()

        # Validation
        errors = []
        if not (username and email and postal_code):
            errors.append("All fields must be filled out.")
        if not postal_pattern.match(postal_code):
            errors.append("Postal code must be exactly 4 digits.")
        if not (skill_level.isdigit() and int(skill_level) in skill_map):
            errors.append("Invalid skill level selected.")

        if errors:
            message = " ".join(errors)
        else:
            try:
                with psycopg2.connect(**db_config) as conn, conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO users (username, email, skill_level, postal_code)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (username, email, int(skill_level), postal_code)
                    )
                    conn.commit()
                return redirect(url_for("index", postal_codes=postal_code, skill_level="all"))
            except psycopg2.Error as e:
                message = f"Database error: {e.pgerror}"

    return render_template("signup.html", skill_map=skill_map, message=message)

# ── Run the Server ────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)