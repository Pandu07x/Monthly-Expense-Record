from flask import *
from pymongo import *
import matplotlib.pyplot as plt
import datetime
app=Flask(__name__,template_folder="template")
cli=MongoClient("mongodb://localhost:27017")
mydba=cli["accounts"]
now=datetime.datetime.now()
curr=now.strftime("%H:%M:%S")
datre=datetime.date.today()
today=datre.strftime("%b-%d-%Y")


mon=datetime.datetime.now()
month=mon.strftime("%b")
mytba=mydba[month]
@app.route('/')
def home():
    total=0
    data=mytba.find()


    return render_template("index.html",data=data)

@app.route("/add",methods=["POST"])
def add():
    if request.method=="POST":
        to=request.form["pay"]
        purpose=request.form["pur"]
        amt=request.form["amt"]
        ID=request.form["id"]
        datea=request.form["date"]
        tim=request.form["time"]

        data={
            "payto":to,
            "purpose":purpose,
            "Amount":amt,
            "TranscationID":ID,
            "date":datea,
            "time":tim
        }

        mytba.insert_one(data)
        print("DSata Added")
        return redirect("/")

    return redirect("/")

@app.route("/month")
def months():
    data=mydba.list_collection_names()
    data.sort()
    print(data)
    return render_template("monthlist.html",data=data)
@app.route("/report/<name>")
def report(name):
    tba=mydba[name]
    data=tba.find()
    l = []
    d = []
    for i in data:
        l.append(int(i["Amount"]))
        d.append(i["date"])
    l.sort()
    d.sort()
    fig = plt.figure(figsize=(10, 5))
    plt.bar(d, l, color="Pink", width=0.4)
    plt.title(name)
    res = (redirect("/month"), plt.show())
    return res

@app.route("/report2/<name>")
def report2(name):
    tba=mydba[name]
    data=tba.find()
    return render_template("report.html",data=data)


@app.route("/sum")
def ass():
    total = 0
    average = 0
    data = mytba.find()
    for i in data:
        s = int(i["Amount"])

        total += s
        average = len(i["Amount"])
    da={

        "Total":total,
        "average":total/average
    }
    return render_template("details.html",data=da)
@app.route("/del/<id>")
def delte(id):
    mytba.delete_one({"TranscationID":id})
    return redirect("/")
@app.route("/date/<date>")
def dat():
    pass



if __name__=="__main__":
    app.run(debug=True)
