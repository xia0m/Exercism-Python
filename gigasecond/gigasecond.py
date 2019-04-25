from datetime import timedelta

gigasecond = 1000000000

def add_gigasecond(moment):
	return moment + timedelta(seconds = gigasecond)

# print(add_gigasecond(datetime(1977, 6, 13))==datetime(2009, 2, 19, 1, 46, 40))

