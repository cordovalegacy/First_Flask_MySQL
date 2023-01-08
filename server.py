from flask import Flask, render_template, request, redirect
from friend import Friend
#import the classes we want to use, in this case, friend.py
app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all()
    #call the get all classmethod to get all friends
    print(friends)
    return render_template('index.html', all_friends = friends)

@app.route('/create_friend', methods = ['POST'])
def create_friend():
    #First we make a data dictionary from our request.form coming from our template
    #The keys in data need to line up exactly with the variables in our query string
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "occ": request.form['occ']
    }
    Friend.save(data)
    #Here we pass the data dictionary to the save function/method from the Friend class file (friend.py)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)