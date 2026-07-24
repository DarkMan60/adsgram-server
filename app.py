from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AdsGram Server Running"

@app.route("/reward")
def reward():
    user_id = request.args.get("userid")
    return f"Reward received for user {user_id}", 200
