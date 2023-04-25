import json

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for categorie in categories:
            response.append({
                "id": categorie.id,
                "name": categorie.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        categorie_data = json.loads(request.body)

        categorie = Categories()
        categorie.name = categorie_data["name"]

        categorie.save()

        return JsonResponse({
            "id": categorie.id,
            "name": categorie.name
        })



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

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads()
        ads.name =ads_data["name"]
        ads.author =ads_data["author"]
        ads.price =ads_data["price"]
        ads.description =ads_data["description"]
        ads.address =ads_data["address"]
        ads.is_published =ads_data["is_published"]

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categorie = self.get_object()

        return JsonResponse({
            "id": categorie.id,
            "name": categorie.name
        })

class AdsDetailView(DetailView):
    model = Ads
    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })
