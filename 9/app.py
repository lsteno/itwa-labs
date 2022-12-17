#imports
from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, session, app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_session import Session
from datetime import timedelta
import posts_dao

#app creation
app = Flask(__name__)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

#session configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

#login configuration setup
login_manager = LoginManager()
login_manager.login_view = 'login_page'
login_manager.init_app(app)

#website pages
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)

@app.route('/')
def index():
    posts = posts_dao.get_posts()
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def single_post(id):
    if request.method == 'POST':
        comment = request.form.to_dict()
        userid = posts_dao.get_userid(session['username'])
        comment['userid'] = userid['id']
        comment['postid'] = id
        success = posts_dao.add_comment(comment)
        if success:
            flash('Commento aggiunto correttamente', 'success')
        else:
            flash('Errore nella creazione del commento: riprova!', 'danger')
        return redirect(url_for('single_post', id=id))

    else:
        post = posts_dao.get_post(id)
        posts = posts_dao.get_posts()
        comments = posts_dao.get_comments(id)
        return render_template('post.html', post=post, comments=comments, posts = posts)

@app.route('/about_us.html')
def about():
    return render_template('about_us.html')

@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
         return render_template('login_page.html')
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = posts_dao.get_user_by_username(username)

        if not user or not check_password_hash(str(user['password']), str(password)):
            flash('Wrong username or password', 'danger')
            return redirect(url_for('login_page'))

        else:
            new = User(id=user['id'], username=user['username'], password=user['password'], profilepic=user['profilepic'])
            login_user(new, True)
            session['logged_in'] = True
            session['username'] = username
            flash('You are logged in', 'success')
            return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    try:
        user = posts_dao.get_user_by_id(user_id)

        new_user = User(id=user['id'], username=user['username'], password=user['password'], profilepic=user['profilepic'])
        return new_user

    except TypeError:
        pass


@app.route('/signup_page', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'GET':
         return render_template('signup_page.html')
    
    else:
            username = request.form.get('username')
            password = request.form.get('password')

            user_in_db = posts_dao.get_user_by_username(username)
            if user_in_db:
                flash('Username already taken', 'danger')
                return redirect(url_for('signup_page'))
            else:
                profilepic = request.files['image']
                if profilepic:
                    profilepic.save('static/' + username.lower() + 'profilepic' +'.jpg')
                    profilepic = (username.lower() + 'profilepic' +'.jpg')
                else:
                    profilepic = 'profile.webp'

                new_user = {"username": username, "password": generate_password_hash(password, method='sha256'), "profilepic": profilepic}
                
                success = posts_dao.add_user(new_user)

                if success:
                    flash('Utente creato correttamente', 'success')
                    return redirect(url_for('index'))
                else:
                    flash('Errore nella creazione del utente: riprova!', 'danger')

            return redirect(url_for('signup_page'))

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You successfully logged out', 'success')
    return redirect(url_for('index'))

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':

        post = request.form.to_dict()
        post_image = request.files['image']
        if post_image:
            postid1 = posts_dao.get_postid()
            postid = postid1['MAX(id)']
            if not postid:
                postid = 1
            post_image.save('static/' + current_user.username.lower() + str(postid+1) +'.jpg')
            post['postpic'] = current_user.username.lower() + str(postid+1) +'.jpg'
        post['profilepic'] = current_user.profilepic
        post['username'] = current_user.username
        userid = posts_dao.get_userid(current_user.username)
        post['text'] = post['testo']
        del post['testo']
        success = posts_dao.add_post(post, userid)
        if success:
            flash('Post creato correttamente', 'success')
        else:
            flash('Errore nella creazione del post: riprova!', 'danger')
        return redirect(url_for('index'))

    else:
        return render_template('new-post.html')
