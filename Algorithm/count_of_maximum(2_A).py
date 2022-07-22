sequence = []
seq_dict = {}
a = None
max_elem = 0
while a != 0:
    a = int(input())
    sequence.append(a)
for i in set(sequence):
    if i > max_elem:
        max_elem = i
seq_dict[max_elem] = 0
for j in sequence:
    if j == max_elem:
        seq_dict[max_elem] += 1
print(seq_dict[max_elem])
