from django import forms


class SentimentTextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your text here', 'rows': 5, 'cols': 40}),
        label="Text",
        required=True
    )
    task = forms.ChoiceField(
        choices=[
            ('sentiment', 'Sentiment Analysis'),
            ('moderation', 'Moderation Radar'),
            ('emotion', 'Emotion Analysis'),
        ],
        label="Task",
        required=True,
        initial='sentiment'
    )


