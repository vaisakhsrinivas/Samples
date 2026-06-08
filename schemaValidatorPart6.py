'''
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
Extra keys are allowed '''



def is_valid_profile(profile):
    Roles = {"user", "creator", "moderator", "staff", "admin"}

    if not (
            isinstance(profile, dict) and
            isinstance(profile.get('username'), str) and
            isinstance(profile.get('posts'), int) and not isinstance(profile.get('posts'), bool) and
            isinstance(profile.get('verified'), bool) and
            profile.get('role') in Roles and
            isinstance(profile.get('badges'), list) and
            all(isinstance(b, str) for b in profile.get('badges'))):  # ← fixed
        return False

    if "supporter" in profile and not isinstance(profile.get('supporter'), bool):
        return False

    return True

def is_valid_schema(obj):

    return( isinstance(obj, dict) and
            isinstance(obj.get("users"), list) and
            all(is_valid_profile(p) for p in obj.get("users"))
            )


print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]})) # should return True.
print(is_valid_schema({"users": []})) # should return True.
print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}})) # should return False.
print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]})) # should return False.
print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]})) # should return False.
print(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]})) # should return False.
print(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False, "badges": ["superstar"]}]})) # should return False.
print(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]})) # should return False.
print(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]})) # should return False.
print(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]})) # should return False