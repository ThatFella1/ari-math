from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import random

POINT_VALUE = 10
LEVEL_THRESHOLD = 3 #number of correct answers before level up
level = 1
score = 0
nCorrect = 0

# Create your views here.
def index(request):
	if request.method == 'Post':
		return
	else:	
		num1 = create_number(level+1)
		num2 = create_number(level+1)
		answer = num1 * num2
		# template = loader.get_template('mult/index.html')
		context = {
			'level': level,
			'score': score,
			'num1': num1,
			'num2': num2,
			'answer': answer
		}
	template = loader.get_template('mult/index.html')
	return HttpResponse(template.render(context, request))
	# return render(request, 'mult/index.html', context)

def example(request):
	return HttpResponse("Hello, world!  You are at the mult index.")


def create_number(digits):
	# print(digits)
	num = random.random()
	# print(num)

	places1 = random.randint(0,digits)
	# print(places1)

	num = num*pow(10,digits-places1)
	num = round(num,places1)
	return num