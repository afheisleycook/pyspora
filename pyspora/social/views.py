from django.shortcuts import (render, redirect, reverse, resolve_url)
from  django.http import (request, response)
def Home(request):
    return render(request,template_name="index.html")