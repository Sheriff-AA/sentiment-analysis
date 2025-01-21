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
            ('hate_speech', 'Hate Speech Detection'),
            ('emotion', 'Emotion Analysis'),
            ('irony', 'Irony Detection')
        ],
        label="Task",
        required=True,
        initial='sentiment'
    )
    language = forms.ChoiceField(
        choices=[
            ('en', 'English'),
            ('es', 'Spanish'),
            ('it', 'Italian'),
            ('pt', 'Portuguese'),
        ],
        label="Language",
        required=True,
        initial='en'
    )

