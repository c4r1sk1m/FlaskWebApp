from flask import Flask, request, jsonify
from flask_login import user_loaded_from_header
from flask import g
from flask.sessions import SecureCookieSessionInterface


app = Flask(__name__)



# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"



#login
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        login_user(user)
        flask.flash('Log in successful')
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)
        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)

#Settings
@app.route("/settings")
@login_required
def settings():
    pass

# GET
@app.route('/users/<user>')
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user


# POST
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})

# running web app in local machine
if __name__ == '__main__':
    login_manager = LoginManager()
    app.run(host='0.0.0.0', port=5000)
    login_manager.init_app(app)