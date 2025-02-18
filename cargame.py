command=""
started = False
while True:
    command=input("->").lower()
    if command=="start":
        if started:
            print("CAR IS  ALREADY STARTED..")
        else:
            started=True
            print("CAR STARTED, LETS GO..")
    elif command=="stop":
        if not started:
            print("CAR IS ALREADY STOPPED..")
        else:
            started=False
            print("CAR STOPPED..")
    elif command=="quit":
        print(" YOU QUIT THE GAME")
        break
    elif command=="help":
        print("""
    STOP -to stop the car
    START -to start the car
    QUIT- to quit the game
        """)
    else:
        print("invalid command")


