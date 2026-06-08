def is_valid_schema(obj):
    Roles = {"user", "creator", "moderator", "staff", "admin"}

    if not (isinstance(obj.get('username'), str) and
            isinstance(obj.get('posts'), int) and not isinstance(obj.get('posts'), bool) and
            isinstance(obj.get('verified'), bool) and
            obj.get('role') in Roles and
            isinstance(obj.get('badges'), list) and
            all(isinstance(b, str) for b in obj.get('badges'))):  # ← fixed
        return False

    if "supporter" in obj and not isinstance(obj.get('supporter'), bool):
        return False

    return True




print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]})) # should return True.
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233})) #should return True.
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []})) #should return True.
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]})) #should return False.
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False})) # should return False.
print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}))  #should return False.
print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]})) # should return False.
print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]})) # should return False.
print( is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]})) # should return False.
print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]})) # should return False.