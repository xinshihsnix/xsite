# -*-coding:utf-8 -*

from django import forms

from models import User


class SignUpForm(forms.Form):
    username = forms.CharField(error_messages={'required': u'请正确填写您的用户名',
                                             'invalid': u'请正确填写您的用户名'})
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),
                               error_messages={'required': u'请正确填写您的密码'})
    email = forms.EmailField(error_messages={'required': u'请正确填写您的邮箱',
                                             'invalid': u'请正确填写您的邮箱'})
    # remember = forms.BooleanField(required=False)
    user = None

    def clean(self):
        return self.cleaned_data