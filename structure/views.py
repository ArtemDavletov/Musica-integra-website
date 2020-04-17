from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def artodox(request):
    return render(request, "session.html")


def incubator(request):
    return render(request, "children.html")


def children(request):
    return render(request, "children.html")


def session(request):
    return render(request, "session.html")
