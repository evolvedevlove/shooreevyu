from flask import Flask

app = Flask(__name__)

@app.route('/index.html')
def index():
    # TO DO - can i get a banner or take a still from my phone video with the shoes
    return '<p>we are here</p><p>but go <a href="reviews.html">here</a> if you want</p>'

@app.route('/reviews.html')
def reviews():
    html_head = f"<head><link rel=stylesheet type=css</head>" # need a stylesheet and ? to use db connection    
    first_review_text = "the dc white shoes were great but grip under the left ball wore through in 4 months"
    html_body = f"<body>{first_review_text}</body>" 
    # TO DO - template page for reviews is a 4 image gallery with a paragraph below
    # what else goes in a review ? title, date, rating, post

    return html_head + html_body

@app.route('/')
def hey_shoo_viewer():
    return 'shooooo ree vyu'

if __name__ == '__main__':
    app.run()