def reverse_string(string:str, start: int, stop: int):
    if start >= stop-1:
        return string if len(string) == 1 else string[stop]+string[start]
    new_string = string[stop] + reverse_string(string[start+1:stop],start, stop-2) + string[start]

    return new_string


a = 'metronome'  # even
print(reverse_string(a, 0, len(a)-1))

b = 'freedom'  # uneven
print(reverse_string(b, 0, len(b)-1))
