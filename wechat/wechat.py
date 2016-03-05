from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123@127.0.0.1:3306/wall"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

global NUM, COUNT
NUM = 0
COUNT = 0


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(20))
    tel = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)

    def __init__(self, name, tel, num):
        self.name = name
        self.tel = tel
        self.num = num

    def __str__(self):
        return "[name:{};  tel:{}]; num:{}".format(self.name, self.tel, self.num)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start')
def start_wall():
    return render_template("start.html")


@app.route('/rule')
def rule_wall():
    return render_template("rule.html")


@app.route('/signIn')
def sign_wall():
    names = []
    print "test"
    users = User.query.order_by(User.num.desc()).all()
    print "test...2"
    for user in users:
        name = user.name
        print(name)
        names.append(name)
    return render_template('signIn.html', names=names)


@app.route('/draw')
def draw_wall():
    return render_template('draw.html')


@app.route('/end')
def end_wall():
    return render_template("end.html")


@app.route('/backManage')
def manage():
    return render_template("backManage.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/manageMenu', methods=["GET", "POST"])
def manageMenu():
    form = request.form
    name = form.get('name')
    pwd = form.get('pwd')
    if (name == 'yxl') and (pwd == '123'):
        return render_template("manageMenu.html")
    else:
        return render_template("backManage.html")


@app.route('/phone_tip')
def phoneTip():
    return render_template("phone_tip.html")


@app.route('/thank')
def thank():
    return render_template('thank.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/successReg', methods=["GET", "POST"])
def successReg():
    global NUM, COUNT
    form = request.form
    userName = form.get("name")
    tel = form.get('tel')
    num = NUM + 1
    user = User(userName, tel, num)
    db.session.add(user)
    db.session.commit()
    COUNT = NUM
    NUM = num
    return render_template("successReg.html")


if __name__ == '__main__':
    app.run()
