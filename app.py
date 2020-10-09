from flask import Flask, render_template

app = Flask(__name__)

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
def index():
    return render_template("home.html",posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
