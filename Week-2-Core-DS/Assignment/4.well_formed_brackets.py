def is_well_formed(string):
    unmatched_brackets = []
    bracket_pairings =  {"(": ")", "{": "}", "[": "]"}
    for char in string:
        if char in bracket_pairings.keys():
            unmatched_brackets.append(char)
        elif not unmatched_brackets or bracket_pairings[unmatched_brackets[-1]] != char:
            return False
        else:
            unmatched_brackets.pop()
    return len(unmatched_brackets) == 0
print(is_well_formed(args[0]))