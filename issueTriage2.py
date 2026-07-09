'''
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:

"bug" and "needs triage" if the title contains "error" or "bug"
"enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:

"needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
"discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:

"security", add a "critical" label

'''


def triage_issue(title,labels):

    title = title.lower()
    labels = labels.copy()

    if not labels:
        if any(word in title for word in ["error", "bug"]):
            labels += ["bug", "needs triage"]
        elif any(word in title for word in ["feature", "add"]):
            labels += ["enhancement", "discussing"]
    elif "needs triage" in labels and any(word in title for word in ["simple", "easy"]):
        labels.remove("needs triage")
        labels.append("good first issue")
    elif "discussing" in labels and any(word in title for word in ["planned", "next"]):
        labels.remove("discussing")
        labels.append("on the roadmap")
    elif "needs triage" in labels or "discussing" in labels:
        if "needs triage" in labels:
            labels.remove("needs triage")
        if "discussing" in labels:
            labels.remove("discussing")
        labels.append("help wanted")
    if "security" in title:
        labels.append("critical")
    return labels



print(triage_issue("app crashes with error", [])) # should return ["bug", "needs triage"].
print(triage_issue("app crashes with error", ["bug", "needs triage"])) # should return ["bug", "help wanted"].
print(triage_issue("add dark mode", [])) # should return ["enhancement", "discussing"].
print(triage_issue("add dark mode", ["enhancement", "discussing"])) # should return ["enhancement", "help wanted"].
print(triage_issue("xss security bug", [])) # should return ["bug", "needs triage", "critical"].
print(triage_issue("security vulnerability in auth", [])) # should return ["critical"].
print(triage_issue("easy a11y fix", ["bug", "needs triage"])) # should return ["bug", "good first issue"].
print(triage_issue("planned api migration", ["enhancement", "discussing"])) # should return ["enhancement", "on the roadmap"].
print(triage_issue("improve security", ["enhancement", "discussing"])) # should return ["enhancement", "help wanted", "critical"]