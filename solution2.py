list1=[5,1,4,2,8]
def bubbleSort(list1):
  n=len(list1)
  for i in range(0,n):
    for j in range(0,n-1):
      if list1[j]>list1[j+1]:
        list1[j],list1[j+1]=list1[j+1],list1[j]
      print(*list1, sep=",")

bubbleSort(list1)
print("the sorted list is")
for i in range(len(list1)):
  print(list1[i], end=',')

