from app import app, requests


@app.route('/')
@app.route("/home")
def home():
    quote=requests.get_quote()
    posts = Post.query.all()
    return render_template('home.html', posts=posts, quote=quote)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'primary')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)    