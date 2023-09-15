from django.db import models


banned_email_list = ['ahmet@gmail.com', 'deneme@carpedu.com', 'teoman@carpedu.com']


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email

    def clean_isim(self):
        isim = self.cleaned_data.get('isim')
        if isim == 'ahmet':
            raise forms.ValidationError('Lütfen Ahmet Dışında Bir Kullanıcı Giriniz')
        return isim

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('Lütfen Banlı mail adresleri dışında bir mail giriniz')
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            self.add_error('email', 'Emailler Eşleşmedi')
            self.add_error('email2', 'Emailler Eşleşmedi')
            raise forms.ValidationError('Emailler Eşleşmedi.')
