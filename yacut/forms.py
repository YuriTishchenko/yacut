from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import MAX_LENGTH, PATTERN_CUSTOM_ID


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 128),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, MAX_LENGTH),
            Optional(),
            Regexp(PATTERN_CUSTOM_ID, message='Допустимы только латинские буквы и цифры.'),
        ]
    )
    submit = SubmitField('Создать')
