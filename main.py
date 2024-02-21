from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home_page.html')

app.run(port=8000, debug=True)
