from django import forms

from .models import *


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('category','title', 'content', 'file', 'reference_number')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('report', 'comment')