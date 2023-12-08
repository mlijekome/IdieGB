# IdieGB v. 0.9.1

A simple guestbook application or a comment system, depending on how you implement it.
IdieGB is built with Flask and it allows other users to post comments on your website.

## Features
- User can post a comment.
- Uses flatfile `guests.db` as a comment database, therefore you don't have to deal with complicated SQL software.
- Early to mid 2010s-styled custom captcha system in place.

## Requirements
- Python 3.x
- Flask

## Installation
1. Download the code from GitHub or clone this repo.
2. Install the required dependencies using `pip install -r requirements.txt`
3. Edit the `guestbook.html` template according to your liking.
4. Create a folder called `static` in rootdir and folder named `style` inside the `static` folder.
5. To "link" your stylesheets with guestbook.html, inside guestbook html template you must place a line with jinja syntax, for an example: `<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style/main.css') }}">`
5. Ensure the `guests.db` file is writeable by the Flask application.
6. Edit `app.secret_key = 'your_secret_key'` inside app.py to include any random string of your choice. DO NOT SHARE THIS WITH ANYONE!!!!!
7. For non-english sites also change `CAPTCHA_CHARACTERS = '!@#$%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'` to (for an example) `CAPTCHA_CHARACTERS = 'CAPTCHA_CHARACTERS = '!@#$%АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШабвгдђежзијклљмнњопрстћуфхцчџш0123456789'`
8. Run the Flask application to start the guestbook.

## Usage
1. Load the page where you integrated this code.
2. Fill in the form and submit to post a comment.


## Contributing
If you would like to contribute to this project, please submit a pull request.

## Disclaimer

IndeGB is provided as-is and may or may not receive continuous updates. Repo owner and/or its current, past or future contributors ARE NOT responsible for any issues or damages that may occur as a result of using this software. It's important to backup your server regurally and to be vary when using code you do not understand. Use it at your own discretion and risk.
