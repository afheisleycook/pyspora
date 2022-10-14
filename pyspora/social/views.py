from django.shortcuts import (render, redirect, reverse, resolve_url)
from  django.http import (request, response)


def home(request):

    posts = {}
    return render(request,template_name="index.html")