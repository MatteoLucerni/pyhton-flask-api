import flask
import sqlite3

app = flask.Flask(__name__)


def get_users():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users


@app.route("/users", methods=["GET"])
def users():
    users = get_users()
    users_list = [
        {"id": user[0], "username": user[1], "password": user[2]} for user in users
    ]
    return flask.jsonify(users_list)


if __name__ == "__main__":
    app.run(debug=True)
