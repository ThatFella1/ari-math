from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import random

POINT_VALUE = 10
LEVEL_THRESHOLD = 3 #number of correct answers before level up


# Create your views here.
def index(request):
	response = request.POST.get('response', None)
	user_answer = request.POST.get('user_answer', None)
	num1 = request.POST.get('num1', None)
	num2 = request.POST.get('num2', None)
	answer = request.POST.get('answer', None)
	level = request.POST.get('level', 1)
	score = request.POST.get('score', 0)
	nCorrect = request.POST.get('nCorrect', 0)

	context = {
		'level': level,
		'score': score,
		'nCorrect': nCorrect,
		'num1': num1,
		'num2': num2,
		'answer': answer,
		'message': ''
	}

	# if request.method == 'Post':
	if response is not None:
		if response == 'user_answer':
			if user_answer is None or user_answer == '':
				context['message'] = 'Try entering something before you submit'
			else:
				# print('DEBUG: We got an Answer: ' + user_answer)
				# print('DEBUG: Original problem was ' + num1 + ' + ' + num2 + ' = ' + answer)

				if is_number(user_answer) or user_answer == '0':
					if (abs(float(answer) - float(user_answer))) < 0.01:

						print("CORRECT! +" + str(POINT_VALUE*level) + " points")
						context['message'] = "CORRECT! +" + str(POINT_VALUE*int(context['level'])) + " points"
						context['score'] = int(context['score']) + POINT_VALUE*int(context['level'])
						context['nCorrect'] = int(context['nCorrect']) + 1

						create_problem(int(context['level'])+1, context)

						#Check Level Up
						if context['nCorrect'] % LEVEL_THRESHOLD == 0:
							context['level'] = int(context['level']) + 1
							context['message'] = "LEVEL UP!!  You're now Level " + str(context['level']) + "!  Questions are now worth " + str(POINT_VALUE*int(context['level'])) + " points."
							# print("* * * * * * * * * * * * * * * * * * *")
							# print("* LEVEL UP!!  You're now Level " + str(level) + "!   *")
							# print("* Questions are now worth " + str(POINT_VALUE*level) + " points.*")
							# print("* * * * * * * * * * * * * * * * * * *")
						# 	os.system("pause")
						# break
						create_problem(int(context['level'])+1, context)
					else:
						print("Hmm, that's not quite right. Try again.")
						context['message'] = "Hmm, that's not quite right. Try again."

		elif response == 'skip':
			context['message'] = "The answer was " + context['answer'] + ". No worries, let's try this new problem!"
			create_problem(int(context['level'])+1, context)

		elif response == 'quit':
			print('DEBUG: User is a quitter!')
	else:
		create_problem(int(context['level'])+1, context)

	template = loader.get_template('mult/index.html')
	return HttpResponse(template.render(context, request))
	# return render(request, 'mult/index.html', context)

def example(request):
	return HttpResponse("Hello, world!  You are at the mult index.")

def is_number(s):
	try:
		float(s)
		return float(s)
	except ValueError:
		return False

def create_number(digits):
	# print(digits)
	num = random.random()
	# print(num)

	places1 = random.randint(0,digits)
	# print(places1)

	num = num*pow(10,digits-places1)
	num = round(num,places1)
	return num

def create_problem(digits, context):
	num1 = create_number(digits)
	num2 = create_number(digits)
	answer = num1 * num2
	context['num1'] = num1
	context['num2'] = num2
	context['answer'] = answer