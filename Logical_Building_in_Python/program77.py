def CheckPerfect(No):
   iSum = 0

   for i in range(1,int((No/2)+1)):
      if(No % i == 0):
         iSum += i 

   return (iSum == No)

def main():
   Value = 0

   print("Enter number : ")
   Value  = int(input())     

   iRet = CheckPerfect(Value)

   if(iRet == True):
      print("It is a perfect number")
   else:
      print("It is not a perfect number")   

if __name__ == "__main__":
   main() 