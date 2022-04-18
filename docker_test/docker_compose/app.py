import redis
from flask import Flask, session

app = Flask(__name__)

app.secret_key = "GENERATE_A_SECRET_THEN_PLACE_HERE"

# Configure Redis for storing the session data on the server-side
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = redis.from_url("redis://localhost:6379")


@app.route("/")
def hello():
    if "code" in session:
        return "Hello %s!" % session["code"]
    session["code"] = "again!!!"

    return "Hello"


if __name__ == "__main__":
    app.run()
