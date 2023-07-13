combinations = []
def combinationSum(k, n):
    backtrack([], 1, k, n)
    return combinations

def backtrack(currCombinations, start, count, target):
    if target == 0 and count == 0:
        combinations.append(list(currCombinations))
        return
    
    if target < 0 or count == 0:
        return

    for i in range (start, 10):
        currCombinations.append(i)
        backtrack(currCombinations, i + 1, count - 1, target - i)
        currCombinations.pop()

# combinationSum(k, n)
print(combinationSum(k=3, n=7))