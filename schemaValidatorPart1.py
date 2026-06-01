'''
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string
}
Extra keys are allowed
'''

def is_valid_schema(obj):

    for key, value in obj.items():
        if key == 'username' and isinstance(value, str):
            return True
    return False


print(is_valid_schema({"username": "bob"}) ) # should return True.
print(is_valid_schema({"username": "jen", "posts": 30})) # should return True.
print(is_valid_schema({"username": ""})) # should return True.
print(is_valid_schema({"username": 7})) # should return False.
print(is_valid_schema({"posts": 25})) # should return False.
