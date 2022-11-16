from django.shortcuts import render


def index(request):
    return render(request, 'personal_portfolio/pages/index.html')
# Create your views here.
