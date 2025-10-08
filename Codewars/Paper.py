# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
def paperwork(n, m):
    if n <= 0 or m <= 0: return 0
    return n * m