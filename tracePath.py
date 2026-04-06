def tracepath(trace):

    result = []

    rev_trace = dict()

    keys = trace.keys()

    for k in keys:

        rev_trace[trace.get(k)] = k

    from_loc = None

    revkeys = rev_trace.keys()


    for k in keys:

        if k not in rev_trace:

            from_loc = k

            break

    to_loc = trace.get(from_loc)

    while to_loc is not None:

        result.append([from_loc, to_loc])

        from_loc = to_loc
        to_loc = trace.get(to_loc)

    return result







my_dict = dict()
my_dict["NewYork"] = "Chicago"
my_dict["Boston"] = "Texas"
my_dict["Missouri"] = "NewYork"
my_dict["Texas"] = "Missouri"
print(tracepath(my_dict))