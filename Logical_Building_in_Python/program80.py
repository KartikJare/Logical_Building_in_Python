def SumDigit(No):
   Digit = 0
   iSum = 0

   while(No != 0):
      Digit = No % 10
      iSum += Digit
      No = No // 10

   return iSum
   
def main():
   No = 0

   print("Enter Number :")
   No = int(input())

   iRet = SumDigit(No)

   print("Summation of digit is : ",iRet)

if __name__ == "__main__":
   main()