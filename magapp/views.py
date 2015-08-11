from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def post_list(request):
    return render(request, 'magapp/post_list.html', {})
