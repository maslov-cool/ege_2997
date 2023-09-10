with open('17_2997.txt') as f:
    A = [int(i) for i in f]
three_digit_nums = [int(str(i)[1]) for i in A if 99 < i < 1000]
average_digit = max(three_digit_nums, key=lambda x:three_digit_nums.count(x))
B = []
for i in range(len(A) - 1):
    s = (int(str(A[i])[-1]) == average_digit) + (int(str(A[i + 1])[-1]) == average_digit)
    if s >= 1:
        B.append(A[i] + A[i + 1])
print(len(B), max(B))





