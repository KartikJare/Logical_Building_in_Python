def DisplayDigit(No):
   Digit = 0

   while(No != 0):
      Digit = No % 10
      print(Digit)
      No = No / 10  # Issue

def main():
   No = 0

   print("Enter Number :")
   No = int(input())

   DisplayDigit(No)


if __name__ == "__main__":
   main() 