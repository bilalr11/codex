# Simple Reddit Viewer

This project provides a simple Flask application that displays Reddit content using the [PRAW](https://praw.readthedocs.io/) library. It supports viewing the front page, browsing specific subreddits, searching posts, and reading comments for submissions. It is intended as a lightweight viewer and is **not** affiliated with Reddit.

## Setup

1. Install dependencies:

```bash
pip install flask praw
```

2. Set your Reddit API credentials as environment variables:

```bash
export REDDIT_CLIENT_ID="your_client_id"
export REDDIT_CLIENT_SECRET="your_client_secret"
export REDDIT_USER_AGENT="simple-reddit-viewer"
```

3. Run the application:

```bash
python app.py
```

Open a browser at `http://localhost:5000` to browse Reddit content.

The UI uses basic Bootstrap styling and is intentionally simple so it is clear this project is a personal viewer and not the official Reddit website.

## Files

- `app.py` – Flask application implementing a simple Reddit viewer.
- `templates/` – HTML templates used to render pages.
- `static/` – Contains `style.css` for minor custom styling.
- `README.md` – This file.
