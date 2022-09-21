from django.http import JsonResponse
from django.shortcuts import render
from api.models import Tasks

# Create your views here.
def rendApi(requests):
    title = Tasks.objects.all().values('title')
    title_dict = [ {'title': item['title']} for item in title]
    print(title_dict)
    context = {
        'tasks':title_dict,
    }
    return JsonResponse(context)
