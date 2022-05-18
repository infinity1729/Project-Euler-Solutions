fn=1# n th fibonacci term
fp=1# previous (n-1 th) fibonacci term
n=1
ans=0
while fn<4_000_000:
    if n%3==2:
        ans+=fn
    n+=1
    fn=fn+fp
    fp=fn-fp
print(ans)
