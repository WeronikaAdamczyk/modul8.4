from flask import Flask
from flask import render_template
from flask import redirect, request

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET','POST'])
def me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET','POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/contact")
