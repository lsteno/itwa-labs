import sqlite3

def get_posts():
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT posts.id, text, postpic, username, profilepic FROM posts,users WHERE posts.userid = users.id'
    cursor.execute(sql)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()

    return posts

def get_post(id):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT posts.id, text, postpic, username, profilepic FROM posts,users WHERE posts.id = ? AND posts.userid = users.id'
    cursor.execute(sql, (id,))
    post = cursor.fetchone()

    cursor.close()
    conn.close()

    return post

def get_comments(id):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT text, username FROM comments,users WHERE comments.postid = ? AND comments.userid = users.id'
    cursor.execute(sql, (id,))
    comments = cursor.fetchall()

    cursor.close()
    conn.close()

    return comments

def get_user_by_username(username):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM users WHERE username = ?'
    cursor.execute(sql, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_id(id):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM users WHERE id = ?'
    cursor.execute(sql, (id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_userid(username):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT id FROM users WHERE username = ?'
    cursor.execute(sql, (username,))
    userid = cursor.fetchone()

    cursor.close()
    conn.close()

    return userid

def get_username(userid):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT username FROM users WHERE id = ?'
    cursor.execute(sql, (userid,))
    username = cursor.fetchone()

    cursor.close()
    conn.close()

    return username

def add_post(post, userid):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    success = False
    sql = 'INSERT INTO posts(text,postpic,userid) VALUES(?,?,?)'
    
    try:
        cursor.execute(sql, (post['text'], post['postpic'], userid['id']))
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
    # if something goes wrong: rollback
        conn.rollback()

    cursor.close()
    conn.close()

    return success

def add_comment(comment):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    success = False
    sql = 'INSERT INTO comments(text,postid,userid) VALUES(?,?,?)'

    try:
        cursor.execute(sql, (comment['text'], comment['postid'], comment['userid']))
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
    # if something goes wrong: rollback
        conn.rollback()

    cursor.close()
    conn.close()

    return success

def add_user(user):
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    success = False
    sql = 'INSERT INTO users(username,password,profilepic) VALUES(?,?,?)'

    try:
        cursor.execute(sql, (user['username'], user['password'], user['profilepic']),)
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
        # if something goes wrong: rollback
        conn.rollback()

    cursor.close()
    conn.close()

    return success

def get_postid():
    conn = sqlite3.connect('frogbook.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT MAX(id) FROM posts'
    cursor.execute(sql)
    postid = cursor.fetchone()

    cursor.close()
    conn.close()

    return postid