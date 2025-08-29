from django.forms.models import ModelForm

from diary.models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'page_date']
