#asks user for the input
# First no
while True:
 try:
		num1 = int(input("Enter the first no: "))
		break
 except ValueError:
 		print("Please enter a number.")
#Second no
while True:
 try:
		num2 = int(input("Enter the Second no: "))
		break
 except ValueError:
 		print("Please enter a number.")

print("The entered no are", num1,"and", num2)

#list of oprator
opera = ["*", "+", "-", "/", "//", "%"] 

# asking user what to perform
oper = input("what do you want to perform amoung(+,-,/,*,%,//(for rounded values)) : ")

# This will happen if the user enters the wrong operator
while oper not in opera:
	print("you chose the wrong operator")
	oper = input("what do you want to perform amoung(+,-,/,*,%,//(for rounded values)) : ")

# Now for the calculators main body
# sum
if oper == "+":
	result = num1+num2
	print("The sum is given as: ", result)
#div
elif oper == "/":
	result = num1/num2
	print("The qoutient is given as: ", result)
# product
elif oper == "*":
	result = num1*num2
	print("The product is given as: ", result)
# Difference
elif oper == "-":
	result = num1-num2
	print("The sum is given as: ", result)
# Remainder
elif oper =="%":
	result = num1%num2
	print("The sum is given as: ", result)
#rounded qoutient(incase of decimal)
elif oper =="//":
	result = num1//num2
	print("The sum is given as: ", result)
#if the user does not select any of the operator
else:
	print("Sorry wrong operator selected")