#imports
from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, session, app
from flask_session import Session
from datetime import timedelta
import posts_dao

#app creation
app = Flask(__name__)

#session configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

#array of dictionaries used for posts content
#posts = [{'id':1, 'username':'Luigi', 'profilepic':'profile.webp', 'text':'Holy shit i love this frog', 'postpic':'Red-Eyed-Tree-Frog-Picture.jpg' }, 
#        {'id':2, 'username':'Alberto', 'profilepic':'profile.webp', 'text':'Look at this cute mf', 'postpic':'frog-eyes-chubby-frog-flower-full-width.jpg' },
#        {'id':3, 'username':'Juan', 'profilepic':'profile.webp', 'text':'frorg', 'postpic':'frog_101329531.jpg'}]

#website pages
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=2)

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

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    session['logged_in'] = True
    session['username'] = request.form['username']
    return redirect(url_for('index'))

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post = request.form.to_dict()
        post_image = request.files['image']
        if post_image:
            postid = posts_dao.get_postid()
            #postid['MAX(id)'] = postid['MAX(id)'] + 1
            post_image.save('static/' + session['username'].lower() + str(postid['MAX(id)']+1) +'.jpg')
            post['postpic'] = session['username'].lower() + str(postid['MAX(id)']+1) +'.jpg'
        post['profilepic'] = 'profile.webp'
        post['username'] = session['username']
        userid = posts_dao.get_userid(post['username'])
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
