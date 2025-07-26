from flask import Flask, redirect, request, jsonify
import requests
import urllib.parse

app = Flask(__name__)

# Spotify API credentials (inserted directly)
CLIENT_ID = "f39352bfae6b44d1805848b81396cd1d"
CLIENT_SECRET = "881f8af97ae443e1a2f7f51309a924dc"
REDIRECT_URI = "https://jolly-taffy-99923a.netlify.app/callback.html"

@app.route("/login")
def login():
    scope = "user-read-private user-read-email"
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": scope
    }
    return redirect(f"{auth_url}?{urllib.parse.urlencode(params)}")

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Authorization code not found", 400

    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(token_url, data=payload, headers=headers)
    if response.status_code != 200:
        return f"Failed to get token: {response.text}", 400

    token_info = response.json()
    return jsonify(token_info)

if __name__ == "__main__":
    app.run(debug=True)
