from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "image_repository_app/index.html")


def run_tests(request):
    return render(request, "image_repository_app/SpecRunner.html")

