from collections import Counter
import sys
lines = [tuple(map(int, line.strip().split())) for line in sys.stdin]

list1, list2 = zip(*lines)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# p1
abs_diff_sum = sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))
print(abs_diff_sum)

# p2
list2_counts = Counter(list2)
weighted_sum = sum(n1 * list2_counts[n1] for n1 in list1)
print(weighted_sum)