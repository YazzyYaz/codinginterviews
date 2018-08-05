def parens(n, results):
    if str[0] == "(" and str[-1] == ")":
        return str
    if n > 0:
        results += ["(" + parens(n-1, results) + ")"]
        return results

def recurse(n, left, right, results):
    
print(parens(3, []))
