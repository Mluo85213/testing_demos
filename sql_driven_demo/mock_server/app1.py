from flask import Flask, request, jsonify

app = Flask(__name__)

# 内存数据结构模拟数据库
users = {}     # 存储用户信息：id -> {"email": ..., "password": ...}
tokens = {}    # 存储 token 映射：token -> user_id

# 注册接口
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = {
        "email": data["email"],
        "password": data["password"]
    }
    return jsonify({"msg": "registered", "id": user_id})

# 登录接口
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    for uid, info in users.items():
        if data["email"] == info["email"] and data["password"] == info["password"]:
            token = f"token_{uid}"
            tokens[token] = uid
            return jsonify({"token": token})
    return jsonify({"error": "login failed"}), 401

# 用户信息查询接口

def user_info():
    token = request.headers.get("Authorization")
    if token in tokens:
        uid = tokens[token]
        return jsonify({"email": users[uid]["email"]})
    return jsonify({"error": "unauthorized"}), 403

if __name__ == "__main__":
    app.run(port=5000)