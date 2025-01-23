from django.shortcuts import render
from django.http import JsonResponse
import requests

from decouple import config

from .forms import SentimentTextForm

SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
EMOTION_API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
MODERATION_API_URL = "https://api-inference.huggingface.co/models/KoalaAI/Text-Moderation"


HUFFINGFACE_API_KEY = config('HUGGING_FACE')
headers = {"Authorization": f"Bearer {HUFFINGFACE_API_KEY}"}


def analyze_text(request):
    context = {}
    if request.method == "POST":
        form = SentimentTextForm(request.POST)
        context.update({
            'form': form
        })

        if form.is_valid():
            text = form.cleaned_data['text']

            task = form.cleaned_data['task']
            if task == 'sentiment':
                URL = SENTIMENT_API_URL
            elif task == 'emotion':
                URL = EMOTION_API_URL
            elif task == 'moderation':
                URL = MODERATION_API_URL
        

            payload = {
                'text': text,
            }

            response = requests.post(URL, headers=headers, json=payload)
            result = response.json()


            if request.htmx:
                return JsonResponse({'result': result})

            context.update(
                {
                    'result': result
                }
            )

        else:
            return render(request, "sentiment_index.html", context)

    else:
        context.update({
            'form': SentimentTextForm()
        })

    return render(request, "sentiment_index.html", context)


