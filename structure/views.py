from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def artodox(request):
    return render(request, "artodox.html")


def incubator(request):
    return render(request, "incubator.html")
