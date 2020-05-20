from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
def scheduled_task():
    return print('It is now 7:00am')

 
@app.route('/')
def welcome():
    return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False)
