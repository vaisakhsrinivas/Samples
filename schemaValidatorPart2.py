'''
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string,
  posts: number,
  verified: boolean
}
Extra keys are allowed
'''

def is_valid_schema(obj):
    return (isinstance(obj.get('username'), str) and
            isinstance(obj.get('posts'), int) and
            isinstance(obj.get('verified'), bool))



print(is_valid_schema({"username": "alice", "posts": 10, "verified": False})) # should return True.
print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25})) # should return True.
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True})) # return False.
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"})) # return False.
print(is_valid_schema({"username": "bill", "verified": True})) #should return False.
print(is_valid_schema({"username": "fred", "verified": True})) # return False.
print(is_valid_schema({"username": 5, "posts": 10, "verified": True})) # return False.