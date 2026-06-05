def is_valid_schema(obj):
    Roles = {"user", "creator", "moderator", "staff", "admin"}

    if not (isinstance(obj.get('username'), str) and
            isinstance(obj.get('posts'), int) and not isinstance(obj.get('posts'), bool) and
            isinstance(obj.get('verified'), bool) and
            obj.get('role') in Roles):
        return False
    if "supporter" in obj and not isinstance(obj.get('supporter'), bool):
        return False
    return True


print(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}))
print(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"})) # should return True.
print(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55})) # should return True.
print(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"})) #should return False.
print(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True})) #should return False.
print(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False})) #should return False.
print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True})) #should return False.
print(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False})) #should return False.