from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'secret123'
@app.route('/set/<name>')
def set_session(name):
    session['user'] = name
    return 'Session set!'
@app.route('/get')
def get_session():
    return f"User: {session.get('user')}"
if __name__ == '__main__':
    app.run(debug=True)
