from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>World!</h1>'

@app.route("/cat")
def cat():
    return '<blockquote class="reddit-card" data-card-created="1546786759"><a href="https://www.reddit.com/r/funny/comments/aczfgr/ohmygodthisisthebestthingeva/">"OHMYGODTHISISTHEBESTTHINGEVA"</a> from <a href="http://www.reddit.com/r/funny">r/funny</a></blockquote> <script async src="//embed.redditmedia.com/widgets/platform.js" charset="UTF-8"></script>'
