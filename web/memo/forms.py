from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('question', 'image', 'text', 'tag')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].widget.attrs['class'] = 'form-control question'
        self.fields['question'].widget.attrs['placeholder'] = '問題(必須)'
        self.fields['question'].widget.attrs['maxlength'] = '150'
        self.fields['text'].widget.attrs['class'] = 'form-control text'
        self.fields['text'].widget.attrs['placeholder'] = '解答・解説(必須)'
        self.fields['tag'].widget.attrs['class'] = 'form-control tag'
        self.fields['tag'].widget.attrs['placeholder'] = 'タグ(任意)'
        self.fields['tag'].widget.attrs['maxlength'] = '100'
        self.fields['image'].widget.attrs['class'] = 'image'
        self.fields['image'].widget.attrs['placeholder'] = '画像(任意)'