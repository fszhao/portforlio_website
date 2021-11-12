from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title = "Welcome to my Portfolio Website!"
    title_text = "I am a Data Scientist and Analytics Engineer specializing in clinical informatics"

    return render_template('index.html',
                                title_text=title_text,
                                title=title,
                                id="index")


@app.route('/about/', methods=['POST', 'GET'])
def about():
    
    title = "About Me"
    title_text = "A little bit about myself, my journey and my trajectory."


    return render_template('/about.html',
                                title_text=title_text,
                                title=title,
                                id="about") 

@app.route('/portfolio/', methods=['POST', 'GET'])
def portfolio():
    
    title = "Portfolio Projects"
    title_text = "Check out the work I've been doing."

    
    return render_template('/portfolio.html',
                                title_text=title_text,
                                title=title,
                                id="portfolio") 

if __name__ == "__main__":
    app.run(debug=True)

