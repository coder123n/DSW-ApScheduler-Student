from flask import Flask, Markup
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

def job_function():
    return print("What's up?!")

scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
scheduler.add_job(job_function, trigger='interval', seconds=15)
#scheduler.start()
@app.route('/')
def welcome():
    return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False)
