from django.shortcuts import render,get_object_or_404,get_list_or_404
# Create your views here.
from django.http import HttpResponse
from .models import personDetails
import pprint
from django.http import JsonResponse
import json
from django.core import serializers
import requests
from django.db import IntegrityError
def index(request):
        #data = serializers.serialize("json",personDetails.objects.all(),fields=('email','password'))
		data=list(personDetails.objects.all())
		dict1 ={}
		for i in data:
			dict1[i.email] = i.password
		json1  = json.dumps(dict1,sort_keys=True)
		return render(request,'loginPage.html',{'personObject':json1})

def registration(request):
	if request.method=='POST':
		if (request.POST.get('name') and request.POST.get('email') and request.POST.get('phonenumber') and request.POST.get('password')):
			post=personDetails()
			post.name=request.POST.get('name')
			post.email=request.POST.get('email')
			post.phonenumber=request.POST.get('phonenumber')
			post.password=request.POST.get('password')
			check= {
        		"variable": "0"
			}
			json2 =json.dumps(check,sort_keys=True)
			try:
				post.save()
				return render(request,'cards.html')
			except IntegrityError as e:
				check["variable"]="1"
				json2 =json.dumps(check,sort_keys=True)
				return render(request,'registrationPage.html',{'validator':json2})
	else:
		return render(request,'registrationPage.html')

def newshome(request):
	return render(request,'index.html')
def User(request):
	return render(request,'User.html')

# def homepage_news(request):
# 	secret = 'f7aa83c2f6844c939839510e05fdb832'
# 	url = 'https://newsapi.org/v2/everything?'
# 	parameters = {
# 	    'q': 'Dhoni Retirement', # query phrase
# 	    'pageSize': 20,  # maximum is 100
# 	    'apiKey': secret # your own API key
# 	}
# 	# Make the request
# 	response = requests.get(url, params=parameters)
#
# 	# Convert the response to JSON format and pretty print it
# 	response_json = response.json()
# 	titles = []
# 	pprint.pprint(response_json)
# 	for i in response_json['articles']:
# 	    titles.append(i['title'])
# 	return render(request,'homepage_news.html',{'homepage_news':temp})
def cards(request):
	return render(request,'cards.html')
def subscription(request):
	return render(request,'Subscription.html')
def payment(request):
	return render(request,'payments.html')
def homePage(request):
	secret = 'f7aa83c2f6844c939839510e05fdb832'
	headers = {'Authorization': 'f7aa83c2f6844c939839510e05fdb832'}
	top_headlines_url = 'https://newsapi.org/v2/top-headlines'
	headlines_payload = {'category': 'business', 'country': 'in'}
	response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
	pretty_json_output = json.dumps(response.json(), indent=4)
	json1_data=json.loads(pretty_json_output)
	x =len(json1_data['articles'])
	newsDict ={}
	count=0
	for i in json1_data['articles'] :
		newsDict[count] = i
		count=count+1
	for i in range(len(newsDict)):
		z=newsDict[i]['content']
		try:
			z=z.replace('\"',"")
		except:
			a=1
		newsDict[i]['content']=z
	for i in range(len(newsDict)):
		z=newsDict[i]['title']
		try:
			z=z.replace('\"',"")
		except:
			a=1
		newsDict[i]['title']=z
	for i in range(len(newsDict)):
		z=newsDict[i]['description']
		try:
			z=z.replace('\"',"")
		except:
			a=1
		newsDict[i]['description']=z
	json_newsDict=json.dumps(newsDict,sort_keys=True)
	if request.method =='POST':
		if request.POST.get('search'):
			check= {
        		"variable": "0"
			}
			json2 =json.dumps(check,sort_keys=True)
			searchquery = request.POST.get('search')
			secret = 'f7aa83c2f6844c939839510e05fdb832'
			url = 'https://newsapi.org/v2/everything?'
			parameters = {
			    'q': searchquery, # query phrase
			    'pageSize': 20,  # maximum is 100
			    'apiKey': secret # your own API key
			}
			response = requests.get(url, params=parameters)
			response_json = response.json()
			search_json_output = json.dumps(response_json, indent=4)
			search_data=json.loads(search_json_output)
			y =len(search_data['articles'])
			searchDict ={}
			resultcount=0
			for i in search_data['articles'] :
				searchDict[resultcount] = i
				resultcount=resultcount+1
			for i in range(len(searchDict)):
				update=searchDict[i]['content']
				try:
					update=update.replace('\"',"")
				except:
					a=1
				searchDict[i]['content']=update
			for i in range(len(searchDict)):
				update=searchDict[i]['title']
				try:
					update=update.replace('\"',"")
				except:
					a=1
				searchDict[i]['title']=update
			for i in range(len(searchDict)):
				update=searchDict[i]['description']
				try:
					update=update.replace('\"',"")
				except:
					a=1
				searchDict[i]['description']=update
			json_searchDict=json.dumps(searchDict,sort_keys=True)
			return render(request,'homePage.html',{'searchnews':json_searchDict,'headlines':json_newsDict,'check':json2})
	return render(request,'homePage.html',{'headlines':json_newsDict})

def search(request):
	flag=0
	if request.method =='POST':
		if request.POST.get('search'):
			searchquery = request.POST.get('search')
			if searchquery != "null":
				flag=1
				secret = 'f7aa83c2f6844c939839510e05fdb832'
				url = 'https://newsapi.org/v2/everything?'
				parameters = {
				    'q': searchquery, # query phrase
				    'pageSize': 20,  # maximum is 100
				    'apiKey': secret # your own API key
				}
				response = requests.get(url, params=parameters)
				response_json = response.json()
				search_json_output = json.dumps(response_json, indent=4)
				search_data=json.loads(search_json_output)
				y =len(search_data['articles'])
				searchDict ={}
				resultcount=0
				for i in search_data['articles'] :
					searchDict[count] = i
					resultcount=resultcount+1
				for i in range(len(searchDict)):
					update=searchDict[i]['content']
					try:
						update=update.replace('\"',"")
					except:
						a=1
					searchDict[i]['content']=update
				for i in range(len(searchDict)):
					update=searchDict[i]['title']
					try:
						update=update.replace('\"',"")
					except:
						a=1
					searchDict[i]['title']=update
				for i in range(len(searchDict)):
					update=searchDict[i]['description']
					try:
						update=update.replace('\"',"")
					except:
						a=1
					searchDict[i]['description']=update
				json_searchDict=json.dumps(searchDict,sort_keys=True)
				return render(request,'',{'searchnews':json_searchDict})
