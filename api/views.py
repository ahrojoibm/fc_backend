from django.shortcuts import render
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

from projects.models import Mock

class Login(APIView):

    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user:
            auth.login(request, user)
            print(auth)
            return JsonResponse({'message': 'ok!'})
        return JsonResponse({'message': 'Username or password is incorrect!'})

    def get_queryset(self):
        return Mock.objects.all()
            