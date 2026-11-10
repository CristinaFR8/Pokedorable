from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class EntrenadorForm(FlaskForm):
    trainer = StringField(
        "Nombre del entrenador/@:",
        validators=[
            DataRequired(message="Debes introducir un nombre."),
            Length(
                min=3,
                max=15,
                message="El nombre debe tener entre 3 y 15 caracteres."
            )
        ]
    )

    submit = SubmitField("Entrar en la Pokédex")