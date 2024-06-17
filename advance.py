while(True):
    print("press q to quit")
    a= input("enter a number")
    if a== 'q':
        break
    a= int(a)
    try:
        if a>=6:
            print ("you enter a number greater then 6")
        else:
            print("you enter a less number")
    except Exception as e:
        print(f"your input resulted in a essor: {e}")
print("thanks for playing this game")