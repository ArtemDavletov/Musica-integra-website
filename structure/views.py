from django.shortcuts import render
from django.template import RequestContext


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


def not_ready(request):
    return render(request, "error/not_ready.html")


def e_handler404(request, exception):
    # context = RequestContext(request)
    # response = render("error/not_ready.html", context)
    # response.status_code = 404
    # return response
    return render(request, "error/error404.html")


def e_handler500(request):
    # context = RequestContext(request)
    # response = render("error/not_ready.html", context)
    # response.status_code = 500
    # return response
    return render(request, "error/error500.html")
