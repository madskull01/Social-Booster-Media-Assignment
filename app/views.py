import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Product


def crud_page(request):
    return render(request, 'crud.html')

def chart_page(request):
    return render(request, 'chart.html')



@csrf_exempt
def create(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    data = json.loads(request.body)
    Product.objects.create(
        name=data.get('name'),
        price=data.get('price')
    )
    return JsonResponse({'message': 'created'})


def list_items(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)


@csrf_exempt
def update(request, id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'PUT required'}, status=405)

    data = json.loads(request.body)
    p = Product.objects.get(id=id)
    p.price = data.get('price')
    p.save()
    return JsonResponse({'message': 'updated'})


@csrf_exempt
def delete(request, id):
    if request.method != 'DELETE':
        return JsonResponse({'message': 'deleted'}, safe=False)

    Product.objects.filter(id=id).delete()
    return JsonResponse({'message': 'deleted'})


def external(request):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    return JsonResponse(response.json(), safe=False)



def report(request):
    data = Product.objects.all()
    return JsonResponse({
        'names': [p.name for p in data],
        'prices': [p.price for p in data],
    })