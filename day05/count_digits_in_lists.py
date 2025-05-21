numbers = [1203, 1256, 312456, 98]

digit_counts = [0] * 10

for num in numbers:
    for digit_char in str(num):
        digit = int(digit_char)   
        digit_counts[digit] += 1

for digit in range(10):
    print(f"{digit}  {digit_counts[digit]}")
