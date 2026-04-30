'''

Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

The query string begins after the "?",
each parameter is separated by "&",
each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:

{
  "name": "Alice",
  "age": "30"
}

'''


def parseUrlQuery(url):
    parts = url.split("?")
    if len(parts) < 2:
        return {}
    else:
        return dict(parts.split("=") for parts in parts[1].strip().split("&"))


url = "https://example.com/search?name=Alice&age=30"

parsedresult = parseUrlQuery(url)
print(parsedresult)