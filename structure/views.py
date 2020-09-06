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


def inspiration(request):
    return render(request, "inspiration.html")


def playing(request):
    return render(request, "playing.html")


def teachers(request):
    return render(request, "teachers.html")


def children_playing(request):
    return render(request, "playing/children_playing.html")


def konkurces(request):
    return render(request, "playing/konkurces.html")


def gumo(request):
    return render(request, "teachers/session/gumo.html")


def courses(request):
    return render(request, "teachers/session/course.html")


def konferences(request):
    return render(request, "teachers/session/konferences.html")


def remote(request):
    return render(request, "teachers/session/remote.html")


def course_materials(request):
    return render(request, "teachers/method/course_materials.html")


def methods_dev(request):
    return render(request, "teachers/method/methods_dev.html")


def notes(request):
    return render(request, "teachers/method/notes.html")


def publications(request):
    return render(request, "teachers/method/publications.html")


def videoconf_materials(request):
    return render(request, "teachers/method/videoconf_materials.html")


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
