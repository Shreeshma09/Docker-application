from flask import Flask
app = Flask(__name__)

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S)
print("Current Time = ",current_time)

@app.route('/')
def hello_world():
    return 'Hello world!'


app.run(host='0.0.0.0',
        port=8080,
        debug=True)