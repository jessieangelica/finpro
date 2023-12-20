# import libraries here
# libraries penting : matplotlib, BytesIO

app = Flask(__name__)

# decorator function buat login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)

        if user:
            return f(*args, **kwargs)
        return redirect('/')
    return decorated_function

# to fetch data from the database
def fetch_from_db():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, amount, category WHERE username=session(username) FROM expenses ORDER BY category')
    expenses = cur.fetchall()
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
@login_required
def visualize():
    data = fetch_from_db()

    plot_url = create_plot(data)

    return render_template('visualize.html', image=plot_url)
