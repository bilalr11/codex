from flask import Flask, render_template, request, abort
import os
import praw

"""A lightweight viewer for browsing Reddit content.
This project is not affiliated with or endorsed by Reddit.
"""

app = Flask(__name__)

# Initialize Reddit instance using environment variables
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT", "simple-reddit-viewer"),
    check_for_async=False
)

@app.route('/')
def front_page():
    posts = reddit.front.top(limit=20)
    return render_template('index.html', posts=posts, title='Front Page')

@app.route('/r/<subreddit>')
def subreddit_page(subreddit):
    try:
        posts = reddit.subreddit(subreddit).hot(limit=20)
    except Exception:
        abort(404)
    return render_template('subreddit.html', posts=posts, subreddit=subreddit, title=f"r/{subreddit}")

@app.route('/r/<subreddit>/comments/<post_id>')
def comments_page(subreddit, post_id):
    try:
        submission = reddit.submission(id=post_id)
        submission.comments.replace_more(limit=0)
    except Exception:
        abort(404)
    return render_template('comments.html', post=submission, subreddit=subreddit, title=submission.title)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = reddit.subreddit('all').search(query, limit=20) if query else []
    return render_template('search.html', results=results, query=query, title='Search')



if __name__ == '__main__':
    app.run(debug=True)
