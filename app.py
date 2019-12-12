from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/store")
def store():
	products = all_products() 
	return render_template("store.html", products = products)

@app.route("/cart/<int:id>")
def cart(id):
	add_to_cart(id = id)
	items = all_cart_items()
	return render_template("cart.html", items = items)

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)