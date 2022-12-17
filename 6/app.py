from fileinput import filename
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{'id':1, 'username':'Luigi', 'profilepic':'profile.webp', 'text':'Holy shit i love this frog', 'postpic':'Red-Eyed-Tree-Frog-Picture.jpg' }, 
        {'id':2, 'username':'Alberto', 'profilepic':'profile.webp', 'text':'Look at this cute mf', 'postpic':'frog-eyes-chubby-frog-flower-full-width.jpg' },
        {'id':3, 'username':'Juan', 'profilepic':'profile.webp', 'text':'frorg', 'postpic':'frog_101329531.jpg'}]

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