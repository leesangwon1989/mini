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

@app.route('/signUp/give', methods = ["POST"])
def signUpPost():
    idReceive = request.form["idGive"]
    nameReceive = request.form["nameGive"]
    passwordReceive = request.form["passwordGive"]

    doc = {
        'id': idReceive,
        'name': nameReceive,
        'password': passwordReceive
    }

    db.sign.insert_one(doc)
    return jsonify({'msg': 'complete sign up!'})

@app.route('/signUp/check', methods =["GET"])
def signUpGet():
    signList = list (db.sign.find({}, {'_id':False}))
    return jsonify({'signs':signList})

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/signIn/check' ,methods = ["GET"])
def signInCheck():
    signList =list(db.sign.find({}, {'_id': False}))
    return jsonify({'signs':signList})

@app.route("/noticeBoard", methods=["POST"])
def commentPost():
    commentReceive = request.form["commentGive"]

    doc = {
        'comment': commentReceive
    }

    db.comment.insert_one(doc)
    return jsonify({'msg':'complete message up!'})

@app.route("/noticeBoard", methods=["GET"])
def commentGet():
    commentList = list(db.comment.find({},{'_id':False}))
    return jsonify({'comments':commentList})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)