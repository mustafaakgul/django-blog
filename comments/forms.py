from django.forms import ModelForm
from .models import Comment
# from captcha.fields import ReCaptchaField


class CommentForm(ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
