import re
count=0
line=input("ENter a string")
word=input("Enter a word to find")
pattern=re.compile(word)
matcher=pattern.finditer(line)
for match in matcher:
    count=count+1
    print(match.start(),"...",match.end()-1,"....",match.group())