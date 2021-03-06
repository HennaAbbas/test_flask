from flask import Flask, render_template, request, flash, redirect, session

from helpers import is_person


app = Flask(__name__)


app.secret_key = "ABC"  


@app.route('/', methods=['GET','POST'])
def greet_person():
    if request.method == 'GET':
        return render_template('index.html')

    else :
        person = request.form['person'] 
        if is_person(person):
            # session['person'] = person
        
            return render_template('index.html', person=person)  
        else:
            flash("You enetered an empty string. Please enter your name again")
            return redirect('/')  


if __name__ == '__main__':
    app.run(host='0.0.0.0')