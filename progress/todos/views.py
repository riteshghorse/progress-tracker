import json
from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
from django.http import HttpResponse
from django.db import connection


def index(request):
	return render(request, 'index.html', {})

@csrf_exempt
def newEntry(request):
	data = request.body.decode('utf-8') 
	received_json_data = json.loads(data)
	item = received_json_data['info']
	return render(request, 'abc.html', {"abc":your_list})