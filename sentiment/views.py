from django.shortcuts import render
import requests

from pysentimiento import create_analyzer
from decouple import config

from .forms import SentimentTextForm

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
HUFFINGFACE_API_KEY = config('HUGGING_FACE')
headers = {"Authorization": f"Bearer {HUFFINGFACE_API_KEY}"}

# Create your views here.
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
            language = form.cleaned_data['language']


            # analyzer = create_analyzer(task=task, lang=language)
            # result = analyzer.predict(text)
            payload = {
                'text': text,
                "parameters": {
                    'task':task, 
                    'lang':language,
                }
            }
            response = requests.post(API_URL, headers=headers, json=payload)
            result = response.json()
            print(result)
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


