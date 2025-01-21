from django.shortcuts import render

from forms import SentimentTextForm

# Create your views here.
def analyze_text(request):
    if request.method == "POST":
        form = SentimentTextForm(request.POST)

        if form.is_valid():

            pass

        else:
            return render(request, "sentiment_index.html", {"form": form})

    else:
        form = SentimentTextForm()

    return render(request, "sentiment_index.html", {"form": form})

