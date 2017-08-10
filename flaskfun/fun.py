from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)

@app.route('/')
def hello():
    return '<a href="derp">hello friend!</a>'
    
@app.route('/derp')
def test():
    e='test this'
    return render_template('test.html', entry=e)
    
if __name__ == '__main__':
    app.run()
