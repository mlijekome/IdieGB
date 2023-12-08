from flask import Flask, render_template, request, redirect, flash, session
import json
import html
import random
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
JSON_FILE = 'guestbook.json'
MAX_COMMENT_LENGTH = 280
CAPTCHA_CHARACTERS = '!@#$%ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def generate_captcha(size=6):
    return ''.join(random.choice(CAPTCHA_CHARACTERS) for _ in range(size))

def load_guestbook():
    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {'guests': []}
    return data

def save_guestbook(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    guestbook_data = load_guestbook()
    captcha = generate_captcha()
    session['captcha'] = captcha
    captcha_image = generate_captcha_image(captcha)
    session['captcha_image'] = captcha_image
    return render_template('index.html', guestbook_data=guestbook_data['guests'], captcha_image=captcha_image)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    guestbook_data = load_guestbook()
    name = request.form.get('name')
    message = request.form.get('message')
    user_captcha = request.form.get('captcha')
    captcha = session.get('captcha')
    if not captcha or user_captcha != captcha:
        flash("CAPTCHA code is incorrect.")
        return redirect('/')
    if not name or not message:
        flash("Name and message are required fields.")
    else:
        name = html.escape(name)
        if len(message) > MAX_COMMENT_LENGTH:
            flash(f"Comment exceeds {MAX_COMMENT_LENGTH} characters.")
        else:
            message = html.escape(message)
            new_entry = {'name': name, 'message': message}
            guestbook_data['guests'].append(new_entry)
            save_guestbook(guestbook_data)
            flash("Comment added successfully!")
    return redirect('/')

def generate_captcha_image(captcha_text, image_size=(100, 30), font_size=24):
    image = Image.new('RGB', image_size, color='pink')
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("ComicMono.ttf", font_size)
    except IOError:
        raise Exception("Font file not found or inaccessible")

    text_width = draw.textlength(captcha_text, font=font)
    text_height = font_size * len(captcha_text.split('\n'))
    x = (image_size[0] - text_width) / 2
    y = (image_size[1] - text_height) / 2
    draw.text((x, y), captcha_text, font=font, fill='#111')

    # Add random noise dots
    for _ in range(random.randint(100, 200)):
        noise_x = random.randint(0, image_size[0] - 1)
        noise_y = random.randint(0, image_size[1] - 1)
        draw.point((noise_x, noise_y), fill='#00582c')

    # Add random lines
    for _ in range(random.randint(2, 5)):
        line_x1 = random.randint(0, image_size[0] - 1)
        line_y1 = random.randint(0, image_size[1] - 1)
        line_x2 = random.randint(0, image_size[0] - 1)
        line_y2 = random.randint(0, image_size[1] - 1)
        draw.line([(line_x1, line_y1), (line_x2, line_y2)], fill='#cf5757', width=random.randint(1, 2))

    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return f"data:image/png;base64,{image_base64}"

if __name__ == '__main__':
    app.run(debug=True)
