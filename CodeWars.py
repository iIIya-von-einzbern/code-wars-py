'''Number of people in the bus

There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.
'''
def number(bus_stops):

    output = 0
    for i in range(len(bus_stops)):
    	output = output + bus_stops[i][0] - bus_stops[i][1]
    	i += 1
    return output

'''Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.'''
def binary_array_to_number(arr):
	return int(''.join([str(item) for item in arr]), 2)

'''There is an array with some numbers. All numbers are equal except for one. Try to find it! It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:'''

def find_uniq(arr):

	arr.sort()
	if arr[0] != arr[1]:
		return arr[0]
	elif arr[-1] != arr[-2]:
		return arr[-1]
