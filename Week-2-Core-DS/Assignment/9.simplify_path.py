def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    res = '/'
    for t in path.split('/'):
        if t in ['', '.']:
            pass
        elif t == '..':
            if stack:
                stack.pop()   
            else:
                pass         
        else:
            stack.append(t)
    res += '/'.join(stack)
    return res