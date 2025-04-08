from flask import Flask, request
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']  # Get data from POST form
        return f"Welcome, {username}!"
    
    return '''
        <form method="POST">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
