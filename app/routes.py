from app import app, requests


@app.route('/')
@app.route("/home")
def home():
    quote=requests.get_quote()
    posts = Post.query.all()
    return render_template('home.html', posts=posts, quote=quote)