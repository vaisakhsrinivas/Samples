def minimumRemove(s):


    open_stack = []
    close_stack = []

    for i in range(len(s)):


        if s[i] == '(':

            open_stack.append(i)

        elif s[i] == ')':

            if open_stack : open_stack.pop()

            else: close_stack.append(i)

    for i in reversed(close_stack+open_stack):

        s = s[:i]+s[i+1:]

    return s






print(minimumRemove("(a)b(c)d)"))