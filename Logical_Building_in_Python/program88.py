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
   
   print(Arr)
   
if __name__ == "__main__":
   main()