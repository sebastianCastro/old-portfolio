startButton = "start"
stopButton = "stop"
helpButton = "help"
quitButton = "quit"
inputButton = ""
started = False
while True:
    inputButton = input("> ").lower()
    if inputButton == startButton:
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif inputButton == stopButton:
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif inputButton == helpButton:
        print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif inputButton == quitButton:
        break
    else:
        print("I do not understand that...")
