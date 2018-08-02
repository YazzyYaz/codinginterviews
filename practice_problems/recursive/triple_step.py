#
# Triple Step: A child is running up a staircase 
# with n steps and can hop either 1 step, 2 steps, or 
# 3 steps at a time. Implement a method to count how 
# many possible ways the child can run up the stairs.
#

def triple_step(n, result=None):
    if not result:
        result = [-1] * (n + 1)
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        result[n] = triple_step(n - 1, result) + triple_step(n - 2, result) + triple_step(n - 3, result)
        return result

print(triple_step(10))
