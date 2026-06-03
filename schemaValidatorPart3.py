'''Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
Extra keys are allowed'''


def is_valid_schema(obj):

    Roles = {"user","creator","moderator","staff","admin"}

    return (isinstance(obj.get('username'), str) and
            isinstance(obj.get('posts'), int) and
            isinstance(obj.get('verified'), bool) and
            obj.get('role') in Roles)


print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"})) # should return True.
print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70})) #should return True.
print(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"})) #should return True.
print(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"})) #should return True.
print(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"})) #should return True.
print(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"})) #should return False.
print(is_valid_schema({"username": "wendy", "posts": 10, "verified": True})) #should return False.
print(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True})) # should return False.
print(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"})) # should return False.
print(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"})) # should return False
print(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"})) # should return False