from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(label='Загрузите файл')


class WordCountForm(forms.Form):
    word = forms.CharField(max_length=100, label='Введите слово')
