from flask import jsonify, request, url_for
from http import HTTPStatus

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id
from .validators import check_id, is_url


@app.route('/api/id/', methods=['POST'])
def add_opinion():
    data = request.get_json()
    url = URLMap()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    original_link = data.get('url')
    custom_id = data.get('custom_id')
    if custom_id is None or (custom_id.strip() == ''):
        custom_id = get_unique_short_id()
    if URLMap.query.filter_by(short=custom_id).scalar():
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    if not is_url(original_link):
        raise InvalidAPIUsage('Недопустимый вариант URL.')
    if not check_id(custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    data['custom_id'] = custom_id
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify({
        'url': url.original,
        'short_link': url_for('redirection', custom_id=url.short, _external=True)
    }), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
