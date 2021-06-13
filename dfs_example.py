
import sys
r = sys.stdin.readline

def dfs(v,nets, ans):
    for i in nets[v]:
        if i not in ans:
            ans.append(i)
            dfs(i,nets,ans)
    return ans

n = int(r())
net = [[] for _ in range(n+1)]
for _ in range(1,int(r())+1):
    e1, e2 = map(int, r().split())
    net[e1].append(e2)
    net[e2].append(e1)

print(len(dfs(1,net,[1]))-1)
