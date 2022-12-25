from django.shortcuts import render
from django.http import HttpResponse
from .models import Newspaper
from django.views.generic.base import View


def index(request):
    return render(request, 'main/index.html')


class PostView(View):
    def get(self, request):
        posts = Newspaper.objects.all()
        return render(request, 'main/index.html', {'post_list': posts})
