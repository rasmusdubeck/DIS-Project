from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Konfiguration til databasen
db_config = {
    'host': 'localhost',
    'dbname': 'cycling_buddy',
    'user': 'postgres',
    'password': 'PostgresSQLthomas1'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    users = []
    postal_input = ""

    if request.method == 'POST':
        postal_input = request.form.get('postal_codes')  # fx "1050,2100"
        postal_list = [code.strip() for code in postal_input.split(',') if code.strip().isdigit()]
        
        if postal_list:
            placeholders = ','.join(['%s'] * len(postal_list))
            query = f"SELECT username,ID, email, skill_level, postal_code FROM users WHERE postal_code IN ({placeholders})"

            try:
                conn = psycopg2.connect(**db_config)
                cur = conn.cursor()
                cur.execute(query, postal_list)
                users = cur.fetchall()
                cur.close()
                conn.close()
            except Exception as e:
                return f"Fejl: {e}"

    return render_template("index.html", users=users, postal_input=postal_input)

if __name__ == '__main__':
    app.run(debug=True)