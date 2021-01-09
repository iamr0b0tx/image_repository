from django.db.models import Q
from django.shortcuts import render, redirect
from image_repository_app.models import Image


# Create your views here.
def index(request):
    context = {
        "query": "",
        "search_results": Image.objects.all()[:10]
    }

    return render(request, "image_repository_app/index.html", context)


def search(request, query=""):
    if not query:
        redirect(index)

    search_results = Image.objects.filter(
        Q(description__icontains=query) |
        Q(tags__icontains=query) |
        Q(alt__icontains=query)
    )

    print(search_results)

    context = {
        "query": query,
        "search_results": search_results
    }

    return render(request, "image_repository_app/index.html", context)


def run_tests(request):
    return render(request, "image_repository_app/SpecRunner.html")

