from flask import Flask ,render_template,request, redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:admin@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://drfwhxzljwungm:66c0032083f85141b064cdaeeb2df0bf86869afff64cc6576b43e4e51816e331@ec2-54-155-87-214.eu-west-1.compute.amazonaws.com:5432/d3ko8os5ki6sqk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class favquote(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote  = db.Column(db.String(1000))

@app.route('/')
def index():
        #fruits = ["Banana","Mango","Cherry","Strawberry"]
        #return render_template('index.html',inp='I am jinja Parameter',fruits=fruits)
        result = favquote.query.all()
        return render_template('index.html',result=result)

@app.route('/end')
def end():
        return '<body> <h1 style="background-color:powderblue;"> This is a heading</h1> <p style="background-color:tomato;">This is a paragraph.</p> </body>'
                #<h1>This is a heading</h1>
                #'<body style="background-color:powderblue;"> <p>This is a paragraph.</p> </body>'

@app.route('/quotes')
def quotes():
        return render_template('quotes.html')

@app.route('/process',methods=['POST'])
def process():
        quote = request.form['quote']
        author = request.form['author']
        addquotes=favquote(author=author,quote=quote)
        db.session.add(addquotes)
        db.session.commit()

        return redirect(url_for('index'))
