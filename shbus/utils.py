def unpad(s):
    if s[-1] != "\r":
        return s[0:-s[-1]]
    else:
        return s.rstrip()
