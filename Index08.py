def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    idx = False
    if s[0] == '*':
        idx = 0

    if s[1] == '*':
        idx = 1
    
    if s[2] == '*':
        idx = 2
    
    if s[3] == '*':
        idx = 3
    
    if s[4] == '*':
        idx = 4
    return idx
