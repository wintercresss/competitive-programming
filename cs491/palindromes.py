n = int(input())
s = input()

total = 0

for i in range(len(s)):
    left, right = i, i
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            total += 1
        else:
            break
        left -= 1
        right += 1
    
    left, right = i-1, i
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            total += 1
        else:
            break
        left -= 1
        right += 1

print(total)