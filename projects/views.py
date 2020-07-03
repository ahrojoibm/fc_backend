from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound
from cloudant import Cloudant, database, query
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from django.views import View

from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated

from .models import Mock

try:
    apikey = os.environ['CLOUDANT_APIKEY']
    host = os.environ['CLOUDANT_HOST']
    url = os.environ['CLOUDANT_URL']
    username = os.environ['CLOUDANT_USERNAME']
except:
    from .database_credentials import *

from django.views.decorators.csrf import csrf_exempt



client = Cloudant.iam(username, apikey)
client.connect()
db = database.CloudantDatabase(client, 'korsdb')
query_db = query.Query(db)

class AllProjects(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        docs = query_db(limit=100, selector={'_id': {'$gt': 0}})['docs']
        return Response({'docs': docs})

    def get_queryset(self):
        return Mock.objects.all()

class SingleProject(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, project_id):
        doc = query_db(selector={'_id': {'$eq': project_id}})['docs']
        if doc:
            return JsonResponse({'doc': doc})
        return HttpResponseNotFound({"Project id not found"})

    def get_queryset(self):
        return Mock.objects.all()






