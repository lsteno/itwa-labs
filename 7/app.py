#imports
from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, session, app
from flask_session import Session
from datetime import timedelta

#app creation
app = Flask(__name__)

#session configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

#array of dictionaries used for posts content
posts = [{'id':1, 'username':'Luigi', 'profilepic':'profile.webp', 'text':'Holy shit i love this frog', 'postpic':'Red-Eyed-Tree-Frog-Picture.jpg' }, 
        {'id':2, 'username':'Alberto', 'profilepic':'profile.webp', 'text':'Look at this cute mf', 'postpic':'frog-eyes-chubby-frog-flower-full-width.jpg' },
        {'id':3, 'username':'Juan', 'profilepic':'profile.webp', 'text':'frorg', 'postpic':'frog_101329531.jpg'}]

#website pages
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:id>')
def single_post(id):
    post = posts[id-1]
    return render_template('post.html', post=post)

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
        print(post)
        post['id'] = posts[-1]['id'] + 1
        post_image = request.files['image']
        if post_image:
            post_image.save('static/' + session['username'].lower() + str(post['id']) +'.jpg')
        post['postpic'] = session['username'].lower() + str(post['id']) +'.jpg'
        post['profilepic'] = posts[-1]['profilepic']
        post['username'] = session['username']
        post['text'] = post['testo']
        del post['testo']
        posts.append(post)
        flash('Post creato correttamente', 'success')
        return redirect(url_for('index'))

    else:
        return render_template('new-post.html')
