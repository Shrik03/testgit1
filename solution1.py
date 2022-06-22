indata = "I am going to school."
#   vowels : aeiou
vowels = "aeiouAEIOU"
#   problem : count the vowels

# step 2: 
count = 0

for i in range(len(indata)):
  if indata[i] in vowels:
    count+=1

count

