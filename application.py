from flask import Flask, redirect, url_for, render_template, request

application=Flask(__name__)

@application.route("/index.html")
@application.route("/")
def home():
    return render_template ("index.html")

@application.route("/shop.html")
def shop():
    return render_template ("shop.html")

@application.route("/contact.html")
def contact():
    return render_template ("contact.html")

@application.route("/product-details.html")
def productDetails():
    return render_template ("product-details.html")

@application.route("/signup.html", methods=['POST', 'GET']) 
def signup():
    if request.method == 'POST':
        connection = sqlite3.connect('user_data.db')    
        cursor = connection.cursor()
    return render_template ("signup.html")


if __name__ == "__main__":
    application.run(debug=True)