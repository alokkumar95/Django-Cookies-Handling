from django.shortcuts import render
from django.http import HttpResponse


def setcookie(request):
    html = HttpResponse("<h1>localhost cookie</h1>")
    html.set_cookie(
        "localhost", "Welcome to the world your Dream", max_age=None)
    return html


def getcookie(request):
    cookie = request.COOKIES['localhost']
    res = HttpResponse(f"<h1>Localhost cookie is {cookie}</h1>")
    return res


def deletecookie(request):
    cookie = request.COOKIES.get('localhost', None)
    print(type(request.COOKIES))
    if cookie:
        response = HttpResponse(
            f"<h1>Your localhost cookie is {cookie} and you deleted the cookie</h1>")
        response.delete_cookie('localhost')
    else:
        response = HttpResponse(f"<h1> Your have to create cookie {cookie}")
    return response
