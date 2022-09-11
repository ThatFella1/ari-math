import random
import sys
import os

def create_number(digits):
	# print(digits)
	num = random.random()
	# print(num)

	places1 = random.randint(0,digits)
	# print(places1)

	num = num*pow(10,digits-places1)
	num = round(num,places1)
	return num

def create_problem(digits):
	num1 = create_number(digits)
	num2 = create_number(digits)
	answer = num1 * num2
	print(str(num1) + ' x ' + str(num2))
	# print("= " + str(answer))
	return answer

def is_number(s):
	try:
		float(s)
		return float(s)
	except ValueError:
		return False

def run(level):
	print("Hi, Ari!  Welcome to our game!")
	user_answer = ''
	score = 0
	nCorrect = 0

	while 1==1:
		print()
		print("Score: " + str(score))
		print("Level: " + str(level))
		answer = create_problem(level+1)

		#continue to try again/get another reponse.  break for next question.
		while 1==1:
			# print("Debug: answer is " + str(answer))
			user_answer = input("Enter Answer (or (s)kip question or (q)uit): ")
			# print("Debug: user_answer is " + str(user_answer))
			if is_number(user_answer) or user_answer == '0':
				if (abs(answer - float(user_answer))) < 0.01:
					print("CORRECT! +" + str(POINT_VALUE*level) + " points")
					score = score + POINT_VALUE*level
					nCorrect = nCorrect + 1

					#Check Level Up
					if nCorrect % LEVEL_THRESHOLD == 0:
						level += 1
						print("* * * * * * * * * * * * * * * * * * *")
						print("* LEVEL UP!!  You're now Level " + str(level) + "!   *")
						print("* Questions are now worth " + str(POINT_VALUE*level) + " points.*")
						print("* * * * * * * * * * * * * * * * * * *")
						os.system("pause")
					break
				else:
					print("Hmm, that's not quite right. Try again.")
					continue
			elif user_answer.lower() == 's':
				print("The answer was " + str(answer) + ".")
				print("No worries, let's try another one.")
				#TODO: os.system line is system-dependent
				os.system("pause")
				break
			elif user_answer.lower() == 'q':
				print("Your final score was: " + str(score))
				print("Thanks for playing, Ari!  GOODBYE!")
				print()
				return

POINT_VALUE = 10
LEVEL_THRESHOLD = 3 #number of correct answers before level up
level = 1

if len(sys.argv) > 1:
	if sys.argv[1].isnumeric():
		level = int(sys.argv[1])

run(level)