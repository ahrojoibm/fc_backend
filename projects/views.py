from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from cloudant import Cloudant, database, query
from django.views.decorators.csrf import csrf_exempt

try:
    apikey = os.environ['CLOUDANT_APIKEY']
    host = os.environ['CLOUDANT_HOST']
    url = os.environ['CLOUDANT_URL']
    username = os.environ['CLOUDANT_USERNAME']
except:
    from .database_credentials import *

client = Cloudant.iam(username, apikey)
client.connect()
db = database.CloudantDatabase(client, 'korsdb')
query_db = query.Query(db)

# Create your views here.
@csrf_exempt
def all(request):
    if request.method == "GET":
        docs = query_db(limit=100, selector={'_id': {'$gt': 0}})['docs']
        return JsonResponse({'docs': docs})
    return HttpResponseNotFound({"Wrong Method"})

def detail(request, project_id):
    if request.method == "GET":
        doc = query_db(selector={'_id': {'$eq': project_id}})['docs']
        if doc:
            return JsonResponse({'doc': doc})
        return HttpResponseNotFound({"Project id not found"})

    return HttpResponseNotFound({"Wrong Method"})

