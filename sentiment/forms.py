from django import forms


class SentimentTextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Write a text...', 
                   'rows': 4, 
                    'cols':100,
                    'class':"form-control w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400",
                    }),
        label="Text",
        required=True,
    )
    task = forms.ChoiceField(
        choices=[
            ('sentiment', 'Sentiment Analysis'),
            ('moderation', 'Moderation Radar'),
            ('emotion', 'Emotion Analysis'),
        ],
        label="Select Task",
        required=True,
        initial='sentiment',
        widget=forms.Select(attrs={
            'class': 'form-select bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        })
    )


