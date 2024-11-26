from flask import Flask, make_response, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    cookie_consent = request.cookies.get('cookie_consent')
    return render_template('home.html', cookie_consent=cookie_consent)

@app.route('/set_cookie', methods=['GET', 'POST'])
def set_cookie():
    decision = request.form['decision']
    response = make_response(redirect('/'))

    if decision == 'aceptado':
        response.set_cookie('cookie_consent', decision, httponly=True, secure=True)
    elif decision == 'rechazado':
        redirect('/')
    return response

@app.route('/gestion_cookie', methods=['GET', 'POST'])
def gestion_cookie():
    response = make_response(redirect('/'))
    response.delete_cookie('cookie_consent')
    return response

if __name__ == '__main__':
    app.run()
