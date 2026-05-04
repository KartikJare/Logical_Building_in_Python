def CountCapital(Brr):
   iCount = 0

   for ch in Brr:
      if(ch >= 65 and ch <= 90):   # Issue
         iCount += 1

   return iCount
      
def main():
   print("Enter string : ")
   Arr = input()

   Ret = CountCapital(Arr)

   print("Number of captial characters are : ",Ret)
   
if __name__ == "__main__":
   main()