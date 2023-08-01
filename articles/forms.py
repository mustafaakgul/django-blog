from django.forms import ModelForm
from .models import Article
#from captcha.fields import ReCaptchaField


# Alternative Inheritance -> forms.Form
class ArticleForm(ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "image",
        ]
