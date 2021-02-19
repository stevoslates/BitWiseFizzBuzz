m = [None, "Fizz", "Buzz", "FizzBuzz"]
v = 810092048  #Denary number of binary value
for i in range(1, 101):
    j = v & 3
    print(m[j] if j else i)
    v = v >> 2 | j << 28 #this answer in the sequence gets put at the end and the new one is moved up. 

