from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.r0xf715.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')
   return render_template('signUp.html')
   return render_template('chat_room.html')
   return render_template('signIn.html')

@app.route("/noticeBoard/signUp", methods=["POST"])
def homework_post():
    nick_name_receive = request.form["nick_name_give"]
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'id': name_receive,
        'name': name_receive,
        'comment': comment_receive,

    }

    db.homework.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/noticeBoard", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)