from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello friend!'
	
if __name__ == '__main__':
	app.run()
