import random
import re
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap
from .constants import RANDOM_LENGTH, URL_REGEX


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        pattern_custom_id = r'^[a-zA-Z0-9]([a-zA-Z0-9]?){16}'
        # if not re.match(URL_REGEX, original_link):
        #     flash('Недопустимый вариант URL.')
        #     return render_template('index.html', form=form)
        # if not re.match(pattern_custom_id, custom_id):
        #     flash('Недопустимый вариант короткой ссылки.')
        #     return render_template('index.html', form=form)
        # if URLMap.query.filter_by(original_link=original_link).first():
        #     flash('URL уже занят.')
        #     return render_template('index.html', form=form)
        # if URLMap.query.filter_by(custom_id=custom_id).first():
        #     flash('Предложенный вариант короткой ссылки уже существует.')
        #     return render_template('index.html', form=form)
        url = URLMap(
            original_link=form.original_link.data, 
            custom_id=form.custom_id.data, 
        )
        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form, custom_id=custom_id)
    return render_template('index.html', form=form)

    
def get_unique_short_id(short_id=None):
    if short_id is not None:
        return short_id
    input_range = string.ascii_letters + string.digits
    random_str = ''.join(random.sample(input_range, RANDOM_LENGTH))
    return random_str


@app.route('/<string:custom_id>', methods=['GET'])
def redirection(custom_id):
    url = URLMap.query.filter_by(custom_id=custom_id).first()
    if not url:
        abort(404)
    return redirect(url.original)
    