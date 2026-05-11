#approach 1

'''def oldest_people(people):
    if not people:
        return []
    max_age = max(p["age"] for p in people)
    return [p["name"] for p in people if p["age"] == max_age]'''

#approach 2

def oldest_people2(people):
    if not people:
        return []

    oldest_age = people[0]["age"]
    for p in people:
        if p["age"] > oldest_age:
            oldest_age = p["age"]

    return [p["name"] for p in people if p["age"] == oldest_age]


print(oldest_people2([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]))
#print(oldest_people2({ "name": "Alice", "age": 30 }))
print(oldest_people2([{ "name": "George", "age": 50 },
            { "name": "Shirley", "age": 42 },
            { "name": "Beth", "age": 48 },
            { "name": "Holly", "age": 50 },
            { "name": "Kevin", "age": 44 },
            { "name": "Frank", "age": 47 },
            { "name": "Zach", "age": 50 },
            { "name": "Jennifer", "age": 43 }]))