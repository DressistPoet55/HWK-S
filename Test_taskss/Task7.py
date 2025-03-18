# Task 7
def preobraz(strok, n):
    simv = ''
    for i in range(n):
        simv += strok[i]
    reverse_simv = "".join(reversed(simv[:-1]))
    return simv + reverse_simv


s = "abcdefxyz"

print(preobraz(s, 1))
print(preobraz(s, 2))
print(preobraz(s, 3))
print(preobraz(s, 4))
