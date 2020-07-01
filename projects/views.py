from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from cloudant import Cloudant, database, query
from django.views.decorators.csrf import csrf_exempt

from django.views import View

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

class AllProjects(View):

    def get(self, request, *args, **kwargs):
        docs = query_db(limit=100, selector={'_id': {'$gt': 0}})['docs']
        return JsonResponse({'docs': docs})

class SingleProject(View):
    def get(self, request, project_id, *args, **kwargs):
        doc = query_db(selector={'_id': {'$eq': project_id}})['docs']
        if doc:
            return JsonResponse({'doc': doc})
        return HttpResponseNotFound({"Project id not found"})

