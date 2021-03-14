from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=  [DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators= [DataRequired('내용은 필수입력 항목입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators = [DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자 이름은 필수입력 항목입니다.'), Length(min=3,max=25)])
    password1 = PasswordField('비밀번호', validators =[DataRequired('비밀번호를 입력해주세요.'),EqualTo('password2','비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators = [DataRequired('같은 비밀번호를 다시 입력해주세요.')])
    email = EmailField('이메일', validators = [DataRequired('답변을 받으실 이메일을 입력해주세요.'),Email()])
