from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from datetime import date
import requests

def index(request):
	if request.method == "GET":
		today = date.today().strftime('%d.%m.%Y')
		url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="+today
		page = requests.get(url)
		if page.status_code == 200:
			soup = BeautifulSoup(page.text, 'html.parser')
			course = soup.find_all(id="R01235")[0].value.string
			print(course)
			course = float(course.replace(",","."))
			result = float(request.GET["val"])
			result = result*course
			print(result)
		return HttpResponse(result)
	else:
		return HttpResponse(11111)
	
# Create your views here.
