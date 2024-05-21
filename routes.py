 #  pip install flask
from flask import Flask, render_template
import sqlite3

def triangle(size):
  size += 1
  for number in range(size):
    print("*" * number)

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/triangle/direction/<int:size>')
#add extra types so inverted triangles, pyramids and maybe even diamonds can be made. 
def triangle(direction, size):
    result = ""
    for number in range(1, size + 1):
        result += "*" * number + "<br>"
    return result


@app.route('/about')
def about():
    return"about"

@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('chatgptpizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id =?', (id,))
    pizza = cur.fetchone()
    return render_template('pizza.html', pizza =pizza)


if __name__ == "__main__":
    app.run(debug=True)  # DEBUG , MUST BE FINAL LINE


