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
	print("Hi, Ari!  Can you solve this problem?")
	user_answer = ''
	while 1==1:
		print()
		answer = create_problem(digits)
		while 1==1:
			# print("Debug: answer is " + str(answer))
			user_answer = input("Enter Answer: ")
			# print("Debug: user_answer is " + str(user_answer))
			if is_number(user_answer):
				if (abs(answer - float(user_answer))) < 0.01:
					print("CORRECT!")
					break
				else:
					print("WRONG! The answer is " + str(answer))
					break
			elif user_answer == 'q':
				print("Thanks for playing!  GOODBYE!")
				print()
				return

	# user_answer = float(input("Enter Answer: "))
	# if (answer - user_answer) < 0.01:
	# 	print("Correct!")
	# else:
	# 	print("The answer is " + str(answer))

if len(sys.argv) > 1:
	if sys.argv[1].isnumeric():
		run(int(sys.argv[1]))
else:
	run(2)