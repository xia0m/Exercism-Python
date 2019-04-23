def is_armstrong(number):
	number_digit = len(str(number))
	tempNumber = number
	result = 0
	while(tempNumber>=1):
		result += int((tempNumber % 10) ** number_digit)
		tempNumber = int(tempNumber/10)
	return result == number
