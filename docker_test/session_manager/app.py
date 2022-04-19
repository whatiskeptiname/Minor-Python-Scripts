from flask import Flask, request, make_response
import redis
import random
import string


app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)


@app.route("/")
def index():
    letters = string.ascii_lowercase
    id_string = "".join(random.choice(letters) for _ in range(10)) + str(
        random.randint(0, 1000)
    )
    user_id = request.cookies.get("id", id_string)
    if r.exists(user_id):
        r.incr(user_id)
    else:
        r.set(user_id, 1)
    response = make_response(r.get(user_id))
    response.set_cookie("id", user_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
