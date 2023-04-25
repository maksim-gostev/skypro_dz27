from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ads.models import Categories, Ads


def index(request):
    return JsonResponse({"status": "ok"}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for categorie in categories:
            response.append({
                "id": categorie.id,
                "name": categorie.name
            })

        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):

    def get(self, request):
        ads = Ads.objects.all()

        response = []
        for ads_ in ads:
            response.append({
                "id": ads_.id,
                "name": ads_.name,
            "author": ads_.author,
            "price": ads_.price,
            "description": ads_.description,
            "address": ads_.address,
            "is_published": ads_.is_published
            })
        return JsonResponse(response, safe=False)