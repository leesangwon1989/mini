from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.r0xf715.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUp/check', methods = ["POST"])
def signUpPost():
    id_receive = request.form["id_give"]
    name_receive = request.form["name_give"]
    password_receive = request.form["password_give"]

    doc = {
        'id': id_receive,
        'name': name_receive,
        'password': password_receive
    }

    db.sign.insert_one(doc)
    return jsonify({'msg': 'complete sign up!'})

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/signIn/check' ,methods = ["GET"])
def signInCheck():
    signList =list(db.sign.find({}, {'_id': False}))
    return jsonify({'sign':signList})

@app.route("/noticeBoard", methods=["POST"])
def commentPost():
    comment_receive = request.form["comment_give"]

    doc = {
        'id': id_receive,
        'name': name_receive,
        'password': password_receive,

    }

    db.homework.insert_one(doc)
    return jsonify({'msg':'complete sign up!'})

@app.route("/noticeBoard", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)