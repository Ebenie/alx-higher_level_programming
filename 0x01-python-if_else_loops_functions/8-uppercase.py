def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - (ord('a') - ord('A'))), end='')
        else:
            print(char, end='')
    print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
