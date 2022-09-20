import random
MIN=1
MAX=100
attempts=5
win=False
first_try=False
 
number= random.randint(MIN,MAX)
last_hint=f"{'EVEN' if number%2 == 0 else 'ODD'}"

#print guess instruction
def game_start():
    print(f"I have some money between Rs.{MIN} and Rs.{MAX}")
    print(f"If you can guess exactly how much it is (within {attempts} times),then I will five it to you.OK?")
    input("Press ENTER to start making money now... ")


#process user input 
def game_play():
    global number, attempts, last_hint, win, first_try
    max_guess= attempts

    while attempts>0:
        print()
        print(f"You  have {attempts} {'attempts' if attempts >1 else 'attempts'} left")
        if attempts ==1:
            print(f"This is your last chance chance. so i'll give you one more hint: It's a {last_hint} number")
        while True:
            try:
                guess=int(input("Try a luck number: "))
                if guess in range(MIN,MAX+1):
                    break
                else:
                    print(f"Please enter number {MIN} and {MAX} inclusive .")
            except ValueError:
                print("Please Enter number only ")
        if guess==number:
            win=True
            if max_guess==attempts:
                first_try=True
            break
        if attempts==1:
            break
        if guess >number:
            if guess-number>5:
                print("Too big.try something smaller")
            else:("Come on! you are very close. Just a bit smaller and you'll get it.")
        else:
            if number-guess> 5:
                print("Too small. try something bigger")
            else:
                print("Come on! you are very close. Just a bit bigger and you'll get it.")
        attempts -=1



#process game_result
def game_finish(win,first_try):
    if win:
        if first_try:
            print("Woo Hoo. you got it right at the first try! you must be a genius")
            print(f"Here your Rs.{number} plus Rs.{number//2} is bonus for you. ")
        else:
            print(f"Congrulation!!! You guessed it right.Here your Rs.{number}")
    else:
        print(f"The lucky number is {number}.\n Sorry you lost. Better luck next time. ")
if __name__=="__main__":
    game_start()
    game_play()
    game_finish(win,first_try)