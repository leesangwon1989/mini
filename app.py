from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rvhpcnz.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@cluster0.a1shctu.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route('/signIn')
def signIn():
    return render_template('signIn.html')


@app.route('/chatRoom')
def chatRoom():
    return render_template('chat_room.html')


@app.route('/signUp/give', methods=["POST"])
def signUpPost():
    idReceive = request.form["idGive"]
    nameReceive = request.form["nameGive"]
    passwordReceive = request.form["passwordGive"]

    doc = {
        'id': idReceive,
        'name': nameReceive,
        'password': passwordReceive
    }

    db.users.insert_one(doc)
    return jsonify({'msg': 'complete sign up!'})


@app.route('/signUp/check', methods=["GET"])
def signUpGet():
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': userList})


@app.route('/signIn/give', methods=["POST"])
def signInGive():
    idReceive = request.form["idGive"]
    passwordReceive = request.form["passwordGive"]
    user = list(db.users.find({'id': idReceive, 'password': passwordReceive}, {'_id': False}))
    if len(user):
        doc = {
            'userId': user[0]['id'],
            'userName': user[0]['name']
        }
        return jsonify({'error': None, 'data': doc})
    else:
        return jsonify({'error': 'login-fail'})

# //comment 관리
@app.route("/noticeBoard/post", methods=["POST"])
def commentPost():
    commentReceive = request.form["commentGive"]
    nameReceive = request.form["nameGive"]
    doc = {
        'comment' : commentReceive,
        'name' : nameReceive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': 'complete message up!'})


@app.route("/noticeBoard/get", methods=["GET"])
def commentGet():
    # commentList = list(db.comment.find({}, {'_id': False}))
    commentList = list(db.comment.find({}, {'_id': False}))
    return jsonify({'comment':commentList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
