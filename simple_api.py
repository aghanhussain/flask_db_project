from flask import Flask,jsonify,request,render_template,session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/test_db'
db = SQLAlchemy(app)

app.secret_key = 'secret_key'

class Friend(db.Model):
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), unique=True,primary_key=True)
    
with app.app_context():
    db.create_all()


@app.route("/records")
def get_records():
    friends =Friend.query.all()
    friend_list = [{'name':friend.name,'city':friend.city,"contact":friend.contact} for friend in friends]
    return jsonify({'friends':friend_list})




data = [
         {'name':'Nasir Hussain', 'city':"Karachi", 'contact':"+92332-3446734"},
         {'name':'Yasir Hussain', 'city':"Lahore", 'contact':"+92332-3446736"},
         {'name':'Tahir Hussain', 'city':"Faisalabad", 'contact':"+92332-3446737"},
         {'name':'Basir Hussain', 'city':"Peshawar", 'contact':"+92332-3446738"},
         {'name':'Sabir Hussain', 'city':"Karachi", 'contact':"+92332-3446739"},]

# hello
@app.route("/")
def home():
    return "<h1>We are making API-HOME PAGE</h1>"

@app.route("/api_response")
def response():
    return jsonify(data)

@app.route("/record", methods=['GET','POST'])
def add_record():
    # if request.method =="POST":
    #     data_rcvd = request.get_json()
    #     record = {'name':data_rcvd['name'], 'city':data_rcvd['city'], 'contact':data_rcvd['contact']}
    #     data.append(record)
    #     return "Record Addedd Successfully"
    # else:
    #     pass
    
    if request.method =="POST":
        record = {'name':request.form['name'], 'city':request.form['city'], 'contact':request.form['contact']}
        data.append(record)
        return "Record Addedd Successfully"
    else:
        return render_template('response.html')    
    
@app.route("/db_record", methods=['GET','POST'])
def add_db_record():
    # if request.method=="POST":        
    #     data = request.get_json()        
    #     new_friend = Friend(name=data['name'], city=data['city'], contact=data['contact'])        
    #     db.session.add(new_friend)
    #     db.session.commit()
    #     return jsonify({'msg':"Friend Added"})
    # else:
    #     return "Please add record via postman in json format"
    if request.method =="POST":
        new_record = Friend(name=request.form['name'], city=request.form['city'], contact=request.form['contact'])        
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'msg':"Friend Added"})
    else:
        return "Please add record via postman in json format"
        
    
    
    
    
    

if __name__=="__main__":
    app.run(debug=True)
    
    
