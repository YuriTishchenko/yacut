
from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id
from .validators import check_id, empty_id, is_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        not_empty_custom_id = get_unique_short_id() if (custom_id is None or empty_id(custom_id)) else custom_id
        if not is_url(original_link):
            flash('Недопустимый вариант URL.')
            return render_template('index.html', form=form)
        if not check_id(not_empty_custom_id):
            flash('Недопустимый вариант короткой ссылки.')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=not_empty_custom_id).scalar():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        url_map = URLMap(
            original=original_link,
            short=not_empty_custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('index.html', custom_id=not_empty_custom_id, form=form)
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>', methods=['GET'])
def redirection(custom_id):
    url = URLMap.query.filter_by(short=custom_id).first_or_404()
    return redirect(url.original)
