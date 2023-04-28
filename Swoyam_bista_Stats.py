# For mean
def Mean(numbers):
	return sum(numbers) / len(numbers)
	
	
# For Median
def Median(numbers):
	numbers = sorted(numbers)
	n = len(numbers)
	if n%2 == 0:
		return (numbers[n//2-1] + numbers[n//2]) /2
	else:
		return numbers[n//2]
		
		
		
# For Mode
def Mode(numbers):
    freq = {}
    for number in numbers:
        freq[number] = freq.get(number, 0) + 1
    max_freq = max(freq.values())
    modes = [number for number, freq in freq.items() if freq == max_freq]
    return modes
