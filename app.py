from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1ec677b04360d83c1fe8598d9fbbb9fa'

posts = [
    {
        'author': 'Sam Magagula',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20 2020'
    },
    {
        'author': 'Isaac Gama',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 10 2020'
    },
    {
        'author': 'Thoko Ndlovu',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 20 20190'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
