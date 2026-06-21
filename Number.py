repitition = int(input("Nature of how many numbers do you want to find:"))

for x in range(repitition):
	pass
	while True:
		try:
			num = int(input("Enter the number: "))
			break
		except ValueError:
			print("Please enter a number")

	if num%2 == 0:
		print("Entered Number is Even Number.")
	else:
		print("Entered number is Odd number.")