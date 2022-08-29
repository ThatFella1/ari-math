import random
import sys

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

def run(digits):
	print("Hi, Ari!  Welcome to our game!")
	user_answer = ''
	score = 0
	while 1==1:
		print()
		print("Score: " + str(score))
		answer = create_problem(digits)
		while 1==1:
			# print("Debug: answer is " + str(answer))
			user_answer = input("Enter Answer: ")
			# print("Debug: user_answer is " + str(user_answer))
			if is_number(user_answer):
				if (abs(answer - float(user_answer))) < 0.01:
					print("CORRECT! +" + str(POINT_VALUE) + " points")
					score = score + POINT_VALUE
					break
				else:
					print("WRONG! The answer is " + str(answer))
					break
			elif user_answer == 'q':
				print("Your final score was: " + str(score))
				print("Thanks for playing!  GOODBYE!")
				print()
				return

POINT_VALUE = 10
POINT_THRESHOLD = POINT_VALUE * 5
level = 1

if len(sys.argv) > 1:
	if sys.argv[1].isnumeric():
		level = int(sys.argv[1]) - 1
		run(int(sys.argv[1]))
else:
	run(2)