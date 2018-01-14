from django import forms


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.Textarea()


class AnswerForm(forms.Form):
    text = forms.Textarea()
    question = forms.IntegerField()