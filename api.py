from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/Hollo')
def hello_world1():
   return 'Hello user'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello ' + name

@app.route('/add/<num1>/<num2>')
def addition(num1 , num2):
   return str(int(num1) + int(num2))

if __name__ == '__main__':
   app.run()
   