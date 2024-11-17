def find_min_max(S):

    # Check min and max in a list of two values.
    if len(S) == 2:

        if S[0] < S[1]:
            return (S[0], S[1])
        else:
            return (S[1], S[0])

    # Recursive case.
    middle = len(S)//2
    left_min, left_max = find_min_max(S[:middle])
    right_min, right_max = find_min_max(S[middle:])

    return find_min_max([left_min, right_min])[0], find_min_max([left_max, right_max])[1]


S = [3, 9, 9, 2, 18, 93, 18, 20]

min_val, max_val = find_min_max(S)
print(f"min: {min_val}, max: {max_val}")
