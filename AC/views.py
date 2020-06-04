from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'AC/index.html')


def signIn(request):
    return render(request, 'AC/signIn.html')

