def SumFactor(No):
   iSum = 0

   for i in range(1,int((No/2)+1)):
      if(No % i == 0):
         iSum += i 

   return iSum

def main():
   Value = 0
   iRet = 0

   print("Enter number : ")
   Value  = int(input())     

   iRet = SumFactor(Value)

   print("Summation of factors is : ",iRet)

if __name__ == "__main__":
   main()