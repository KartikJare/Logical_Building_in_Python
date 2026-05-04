def Maximum(Brr):

   iMax = Brr[0]

   for i in range(len(Brr)):
      if(Brr[i] > iMax):
         iMax = Brr[i]

   return iMax

def main():
   Size = 0
   Arr = []

   print("Enter number of element : ")
   Size  = int(input())

   print("Enter the element : ")

   value = 0

   for i in range(Size):
      value = int(input())
      Arr.append(value)
   
   Ret = Maximum(Arr)

   print("Maximum is : ",Ret) 
   
if __name__ == "__main__":
   main()