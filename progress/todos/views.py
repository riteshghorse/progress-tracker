import json
from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_protect ,csrf_exempt


def index(request):
	return render(request, 'index.html', {})

@csrf_exempt
def newEntry(request):
	data = request.body.decode('utf-8') 
	received_json_data = json.loads(data)
	print(received_json_data['info'])
	# data = request.json['info1']
	# print(data)
	# item = data
	# print(item)
	return render(request, 'index.html', {})