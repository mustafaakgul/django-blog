from django import forms
from .models import  Article

#forms.Form yerine Model formlarndan olusturmak
#forms.Form dan turetileblir class parantezinin icine ancak kndimizde olusturabliriz
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        #fields = ["title", "content"]
        fields = ["title", "content", "article_image"]


from captcha.fields import ReCaptchaField


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]