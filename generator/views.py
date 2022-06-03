from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def password(request):
	length = int(request.GET.get('length', 12))

	is_uppercase = {"on": True, None: False}.get(request.GET.get('uppercase'))
	is_numbers = {"on": True, None: False}.get(request.GET.get('numbers'))
	is_special = {"on": True, None: False}.get(request.GET.get('special'))

	generated_password = []

	lowercase = list("qwertyuiopasdfghjklzxcvbnm")
	uppercase = list("QWERTYUIOPASDFGHJKLZXCVBNM")
	numbers = list("1234567890")
	special_symbols = list("!@#$%^&*()_+?<>-=")

	character_list = [lowercase]

	if is_uppercase:
		character_list.append(uppercase)

	if is_numbers:
		character_list.append(numbers)

	if is_special:
		character_list.append(special_symbols)

	for i in range(length):
		generated_password.append(random.choice(random.choice(character_list)))

	return render(request, 'generator/password.html', {'password': "".join(generated_password)})