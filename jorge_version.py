def cat():
# import random module
    import random
# create a range of random numbers between 1-10
    n = random.randrange(1,100)
# take a user input to enter a number
    guess = int(input("\nThe cat says: miauuu, if you guess the right number, I will tell you, were the key for door e is!\nPlease enter any number: "))
    while n!= guess: # means if n is not equal to the input guess
# if guess is smaller than n
        if guess < n:
            print("Too low")
# again ask for input
            guess = int(input("Enter number again: "))
# if guess is greater than n
        elif guess > n:
            print("Too high!")
# to again ask for the user input
            guess = int(input("Enter number again: "))
# if guess gets equals to n terminate the while loop
        else:
            break
    print("Congratulations !!\nThe key is in Yoda lasersaber !!")

cat()

