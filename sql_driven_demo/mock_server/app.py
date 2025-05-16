# mock_server/app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user_info")
def user_info():
    user_id = request.args.get("id")
    if user_id == "1":
        return jsonify({"email": "eve.holt@reqres.in"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(port=5000)
