'''
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.

Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:

---
title: My Post
draft: false
views: 100
---
Should return:

{
  title: "My Post",
  draft: false,
  views: 100
}
Numbers, Booleans, and Strings should all be returned as their respective type.
The given string will have new lines separated with the newline character ("\n").
The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".
'''


def parsefrontmatter(string):

    result = {}
    s = string.strip().split('\n')
    line = [line for line in s if line.strip() != "---"]

    for l in line:
        key, value = l.split(': ', 1)

        if value == 'true':
            value = True
        elif value == 'false':
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        result[key] = value
    return result



print(parsefrontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
#should return { title: "My Post", draft: False, views: 100 }
print(parsefrontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))
#should return { id: "6a174db57256a112f932195c", title: "My Book", locale: "en", wordCount: 10000, published: False }.
print(parsefrontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))
#should return { version: "1.0.0", url: "https://example.com", private: True }.
print(parsefrontmatter("---\nrating: 4.5\nprice: 9.99\n---"))
#should return { rating: 4.5, price: 9.99 }.
