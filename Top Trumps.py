player1 = 0
player2 = 0

while True:
    emoti1 = input("Player 1: Which emoti do you have? ")
    emoti2 = input("Player 2: Which emoti do you have? ")
    stat = input("Which stat is being tested? ")

    emoti1 = emoti1.lower()
    emoti2 = emoti2.lower()
    stat = stat.lower()

    if emoti1 == "heart":
        emoti1 = {"friendliness" : (50), "fury" : (1), "Tweet Rank" : (1), "colour" : (4)} #Heart
    elif emoti1 == "poop":
        emoti1 = {"friendliness" : (30), "fury" : (2), "Tweet Rank" : (88), "colour" : (2)} #Poop
    elif emoti1 == "sunglasses":
        emoti1 = {"friendliness" : (39), "fury" : (2), "Tweet Rank" : (23), "colour" : (5)} #Sunglasses
    elif emoti1 == "expressionless":
        emoti1 ={"friendliness" : (20), "fury" : (3), "Tweet Rank" : (26), "colour" : (2)} #Expressionless

    if emoti2 == "heart":
        emoti2 = {"friendliness" : (50), "fury" : (1), "Tweet Rank" : (1), "colour" : (4)} #Heart
    elif emoti2 == "poop":
        emoti2 = {"friendliness" : (30), "fury" : (2), "Tweet Rank" : (88), "colour" : (2)} #Poop
    elif emoti2 == "sunglasses":
        emoti2 = {"friendliness" : (39), "fury" : (2), "Tweet Rank" : (23), "colour" : (5)} #Sunglasses
    elif emoti2 == "expressionless":
        emoti2 ={"friendliness" : (20), "fury" : (3), "Tweet Rank" : (26), "colour" : (2)} #Expressionless


    if stat == "tweet rank":
        if emoti1["Tweet Rank"] < emoti2["Tweet Rank"]:
            print("\nEmoti 1 wins\n")
            player1 +=1
        elif emoti1["Tweet Rank"] > emoti2["Tweet Rank"]:
            print("\nEmoti 2 wins\n")
            player2 +=1
        else:
            print("\nIt is a tie\n")
    else:
        if emoti1[stat] > emoti2[stat]:
            print("\nEmoti 1 wins\n")
            player1 +=1
        elif emoti1[stat] < emoti2[stat]:
            print("\nEmoti 2 wins\n")
            player1 +=1
        else:
            print("\nIt is a tie\n")

    print("Player 1:", player1)
    print("Player 2:", player2)
    print("")
