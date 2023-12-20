from flask import (
    Flask, request, render_template, session, flash, redirect, url_for, jsonify
)

from db import db_connection


app = Flask(__name__)
app.secret_key = 'THISISMYSECRETKEY'  # create the unique one for yourself


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ function to show and process login page """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = db_connection()
        cur = conn.cursor()
        sql = """
            SELECT id, username
            FROM users
            WHERE username = '%s' AND password = '%s'
        """ % (username, password)
        cur.execute(sql)
        user = cur.fetchone()

        error = ''
        if user is None:
            error = 'Wrong credentials. No user found'
        else:
            session.clear()
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('index'))

        flash(error)
        cur.close()
        conn.close()

    return render_template('login.html')

@app.route('/logout')
def logout():
    """ function to do logout """
    session.clear()  # clear all sessions
    return redirect(url_for('login'))

# to fetch data from the database
def fetch_from_db(user_id):
    conn = db_connection()
    cur = conn.cursor()
    # select with the user_id
    sql = """
        SELECT id, amount, category
        FROM expenses
        WHERE username = %s 
        ORDER BY category
    """ % (user_id)
    cur.execute(sql)
    conn.commit()  # commit to make sure changes are saved
    cur.close()
    conn.close()

    return data

# take the data from the function above, and make the plot with it
def create_plot(data):
    # matplotlib magic here

    # save the generated plot to img using BytesIO object

    # then encode that image to base64 biar bisa di embed di HTML
    # like this : <img href=""></img>

    return plot_url

# the app routing thingy to visualize
@app.route('/visualize')
def visualize():

    # check if user is logged in or not 
    if not session :
        return redirect(url_for('login'))

    user_id = session.get('user_id')

    data = fetch_from_db(user_id)

    plot_url = create_plot(data)

    return render_template('visualize.html', image=plot_url)
