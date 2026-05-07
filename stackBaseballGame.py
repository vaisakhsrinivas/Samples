'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

'''
from pip._internal import operations


def stackBaseballGame(operations):

    result = []
    for op in operations:
        if op.lstrip("-").isdigit():
            result.append(int(op))
        elif op == "+":
            result.append(result[-1] + result[-2])
        elif op == "C":
            result.pop()
        else:
            result.append(result[-1]*2)
    return sum(result)


ops = ["1", "2", "+", "C", "5", "D"]
ops1 = ["5","D","+","C"]
print(stackBaseballGame(ops))
print(stackBaseballGame(ops1))