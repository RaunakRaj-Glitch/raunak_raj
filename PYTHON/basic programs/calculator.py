# I am making the calculator as a function.
def calculator():
  # making the first function to add two numbers.
  def add():
    a = int(input("Enter the first number :"))
    b = int(input('Enter the second number :'))
    c = a+b
    print(f"Current result :{c}")
  # making the second function to subtrat two numbers.
  def subtract():
    a = int(input("Enter the first number :"))
    b = int(input('Enter the second number :'))
    c = a-b
    print(f"Current result :{c}")
  # making the third function to multiply two numbers.
  def multiply():
    a = int(input("Enter the first number :"))
    b = int(input('Enter the second number :'))
    c = a*b
    print(f"Current result :{c}")
    # making the fourth function to divide the two numbers.
  def divide():
    a = int(input("Enter the first number :"))
    b = int(input('Enter the second number :'))
    c = a/b
    print(f"Current result :{c}")
  # making the main to execute the whole code.
  def main():
    # using the while loop.
    while True:
      # providing the instructions.
      print("press 'a' for addition.")
      print("press 's' for subtraction.")
      print("press 'd' for multiplication.")
      print("press 'f' for dividion.")
      print("press 'g' for quit.")
      # taking the user input.
      user = input("Enter your choice :")
      # checking the conditions what is able to equate the code.
      if user != 'g':
        if user == 'a':
          print("add :-")
          add()
        elif user == 's':
          print("Subtract :-")
          subtract()
        elif user == 'd':
          print("Multiply:-")
          multiply()
        elif user == 'f':
          print("Divide :-")
          divide()
        else:
          list = ['q','w','e','r','t','y','u','i','o','p','g','h','j','k','l','z','x','c','v','b','n','m']
          # raising error when user entered unwanted digits.
          if user == list:
            raise ValueError("Enter accourding to our instructions.")
      else:
        # providiing thank you massage which is given by coder to user.
        print("Thanks for using me !")
        break
  # Executing our main function of the calculor.
  main()
# wxecuting our calculator.
calculator()