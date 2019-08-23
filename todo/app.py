from flask import Flask

app = Flask(__name__)

@app.route('/') 

# Any view you specify must be decorated by app.route to be a functional part of the application. 
# You can have as many functions as you want scattered across the application, 
# but in order for that functionality to be accessible from anything external to the application, 
# you must decorate that function and specify a route to make it into a view.




def hello_world():
    #Print 'Hello world' as the response body.
    return 'Hello world'






# DON'T KNOW HOW TO DO THIS

# The app.py file will be the application's root. This is where all the Flask application goodness will go, and you'll create an environment variable that points to that file. If you're using pipenv (like I am), you can locate your virtual environment with pipenv --venv and set up that environment variable in your environment's activate script.

# # in your activate script, probably at the bottom (but anywhere will do)

# export FLASK_APP=$VIRTUAL_ENV/../todo/app.py
# export DEBUG='True'

