from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from cloudant import Cloudant

# Create your views here.
def index(request):
    client = Cloudant.iam("username", "apikey")
    client.connect()
    bases_de_datos = client.all_dbs()
    print(bases_de_datos)
    return JsonResponse({'nlc_response': bases_de_datos})

