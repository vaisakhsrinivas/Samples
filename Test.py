import sys

def main():
    print ('Hello there', sys.argv[1])


def repeat (s, exclaim):

    result = s + s + s
    if exclaim:
        result =  result + '!!!'
    return result


if __name__ == '__main__':
    main()
    s = repeat('Python',True)
    print(s)
