def Minimum(Brr):
   iMin= Brr[0]

   for i in range(len(Brr)):
      if(Brr[i] < iMin):
         iMin = Brr[i]

   return iMin

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
   
   Ret = Minimum(Arr)

   print("Minimum is : ",Ret) 
   
if __name__ == "__main__":
   main()