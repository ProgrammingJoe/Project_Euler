def main():
	add = 0
	top = 4000000
	num1 = 1
	num2 = 2
	temp = 0
	while(num1 < top and num2 < top):
		if(num2%2 == 0):
			add += num2
		temp = num1
		num1 = num2
		num2 = num2 + temp
	print(add)
main()
