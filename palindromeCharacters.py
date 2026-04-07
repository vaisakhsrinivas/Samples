def palindrome_locator(s):
    def palindrome_check(s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    if not palindrome_check(s):
        return "none"

    if len(s) % 2 == 0:
        middle = len(s) // 2
        return s[middle-1]+s[middle]

    if len(s) % 2 != 0:
        middle = len(s) // 2
        return s[middle]

palindrome_locator("noon")

if __name__ == "__main__":
    test_string = "noon"
    result = palindrome_locator(test_string)
    print(f"Palindrome locator for '{test_string}': {result}")