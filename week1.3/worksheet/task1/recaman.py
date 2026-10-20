# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0]
for i in range(1, L):
    print(f'term before{sequence[i-1]}, counter{i}')
    equation = sequence[i-1] - (i)
    if equation > 0 and equation not in sequence:
        sequence.append(sequence[i-1] - (i))
    else:
        sequence.append(i + sequence[i-1])

  

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
