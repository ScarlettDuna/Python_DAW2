# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string (alphabetical ascending), the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    combined = a1 + a2
    unique_chars = set(combined)
    sorted_chars = sorted(unique_chars)
    final = "".join(sorted_chars)
    return final

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))

# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))