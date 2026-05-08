s=["ABC","ARC","AGC","AHC"]
for i in range(3):
    sin=input()
    if sin in s:
        s.remove(sin)
print(s[0])