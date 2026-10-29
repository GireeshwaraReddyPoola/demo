from flask import Flask, jsonify, request
import config
app = Flask(__name__)
#
@app.route("/")
def hello_world():
    return "home page"
# @app.route("/mobiles")
# def mobiles():
#     return "Mobiles list"
# @app.route("/mobiles/moto")
# def moto_mobiles():
#     return "MOTO Mobiles list"
# @app.route("/students")
# def students():
#     return "students list"
@app.route("/students")
def students():
    mydb=config.connect()
    mc=mydb.cursor(dictionary=True)
    mc.execute("select * from students;")
    r=mc.fetchall()
    return jsonify(r)
@app.route("/students/<int:id>")
def each_students(id):
    mydb=config.connect()
    mc=mydb.cursor(dictionary=True)
    mc.execute('''select * from students
    where roll_no=%s;''',(id,))
    r=mc.fetchall()
    return jsonify(r)
@app.route("/students/<gender>")
def gender_students(gender):
    mydb=config.connect()
    mc=mydb.cursor(dictionary=True)
    mc.execute('''select * from students
    where gender=%s;''',(gender,))
    r=mc.fetchall()
    return jsonify(r)
@app.route("/stu",methods=["POST"])
def add_student():
    data=request.get_json()
    roll_no=data["roll_no"]
    name=data["name"]
    dob=data["dob"]
    gender=data["gender"]
    phone=data["phone"]
    mydb = config.connect()
    mc = mydb.cursor()
    mc.execute('''insert into students values
    (%s,%s,%s,%s,%s);''',(roll_no,name,dob,gender,phone))
    mydb.commit()
    return "added new student"