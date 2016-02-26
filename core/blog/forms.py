from pagedown.widgets import PagedownWidget
from django import forms
from models import Blog


class FooModelForm(forms.ModelForm):
    a_text_field = forms.CharField(widget=PagedownWidget())
    # another_text_field = forms.CharField(widget=PagedownWidget())
