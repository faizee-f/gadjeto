from django.shortcuts import render
from .models import sub_category
from django.http import HttpResponse
import json


def get_subcategory(request):
    print('hello')
    id = request.GET.get('id', '')
    result = list(sub_category.objects.filter(
    category_id=int(id)).values('id', 'name'))
    print(result)
    return HttpResponse(json.dumps(result), content_type="application/json")
