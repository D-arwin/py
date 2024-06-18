"""I need an index to pass the values of the iterator
3 variables for the calculators
a list to store the hamming numbers"""

n = 26
hamming_numbers = [1]
i = j = k = 0
ham2 = ham3 = ham5 = 0

while len(hamming_numbers) < n:
    ham2 = hamming_numbers[i]*2
    ham3 = hamming_numbers[j]*3
    ham5 = hamming_numbers[k]*5

    min_ham = min(ham2,ham3,ham5)

    hamming_numbers.append(min_ham)
    if min_ham == ham2:
        i += 1
    if min_ham == ham3:
        j += 1
    if min_ham == ham5:
        k += 1
    print(hamming_numbers)


