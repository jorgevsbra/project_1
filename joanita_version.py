def bottle():
    player = []
    answer = ['red','yellow']
    print('On the table of spell´s you have 3 bottles of 3 diferent colors; red, yellow and green. You have to choose the colors that make the right potion to open the door b.')
    while set(player)!= set(answer):
        player.append(input('Choose 2 diferent colors'))
        if len(player)==2:
            if set(player) !=set(answer):
                player=[]
                print('You’ve been turned into a frog, try again!')
    return('all right! You’re the master of witchcraft, you won!')

bottle()
