from django import forms


class SentimentTextForm(forms.Form):
    text = forms.Textarea()