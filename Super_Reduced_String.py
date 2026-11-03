def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        return "Empty String"

    return ''.join(stack)


if __name__ == '__main__':
    s = input().strip()
    result = superReducedString(s)
    print(result)