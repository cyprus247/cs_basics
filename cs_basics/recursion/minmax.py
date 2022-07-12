def minmax(sequence, start, stop):
    min = sequence[start]
    max = sequence[start]
    if start >= stop:
        return min, max
    lower_min, lower_max = minmax(sequence, start+1, stop)
    if lower_min < min:
        min = lower_min
    if lower_max > max:
        max = lower_max
    return min, max


a = [ 31,2435,63,146,6,515,2876, 1526, 999, -123, 0]
print(minmax(a, 0, len(a)-1))