from flask import Flask
from handlers.public import main as public_main

app = Flask(__name__)

# PUBLIC URLS

# HOME PAGE
app.add_url_rule(rule="/", endpoint="public.main.home_page", view_func=public_main.home_page, methods=["GET", "POST"])


# FOR RUNNING THE APP

if __name__ == '__main__':
    app.run(debug=True)