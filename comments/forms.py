from django import forms
from .models import Post, Comment
from captcha.fields import ReCaptchaField

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]