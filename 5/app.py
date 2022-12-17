from fileinput import filename
from flask import Flask, render_template, url_for

app = Flask(__name__)

#posts = [{'username':'Luigi', 'profilepic':'url_for(\'static\', filename=\'profile.webp\')', 'text':'Holy shit i love this frog', 'postpic':'url_for(\'static\', filename=\'Red-Eyed-Tree-Frog-Picture.jpg\')' }, 
#         {'username':'Alberto', 'profilepic':'url_for(\'static\', filename=\'profile.webp\')', 'text':'Look at this cute mf', 'postpic':'url_for(\'static\', filename=\'frog-eyes-chubby-frog-flower-full-width.jpg\')' },
#         {'username':'Juan', 'profilepic':'url_for(\'static\', filename=\'profile.webp\')', 'text':'frorg', 'postpic':'url_for(\'static\', filename=\'frog_101329531.jpg\')'}]


#profilepic = '/static/profile.webp'
#postimgs = ['1':'/static/Red-Eyed-Tree-Frog-Picture.jpg', '2':'/static/frog-eyes-chubby-frog-flower-full-width.jpg', '3':'static/frog_101329531.jpg']
#for post in posts:
#    post.postpic : url_for('static', filename:'frog_101329531.jpg')

@app.route('/')
def index():
    posts = [{'username':'Luigi', 'profilepic':'profile.webp', 'text':'Holy shit i love this frog', 'postpic':'Red-Eyed-Tree-Frog-Picture.jpg' }, 
         {'username':'Alberto', 'profilepic':'profile.webp', 'text':'Look at this cute mf', 'postpic':'frog-eyes-chubby-frog-flower-full-width.jpg' },
         {'username':'Juan', 'profilepic':'profile.webp', 'text':'frorg', 'postpic':'frog_101329531.jpg'}]
    return render_template('index.html', posts=posts)

@app.route('/about_us.html')
def about():
    return render_template('about_us.html')