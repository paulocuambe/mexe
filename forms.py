from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class FileForm(FlaskForm):
  image = FileField("file", validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], 'formato incorrecto')])
  rotation = StringField("Rotação de")
  left = StringField("Valor de X")
  right = StringField("Largura")
  top = StringField("Valor de Y")
  down = StringField("Altura")
  height = StringField("Altura")
  width = StringField("Largura")
  submit = SubmitField('Carregar')