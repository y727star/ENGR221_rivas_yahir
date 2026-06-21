"""
Name: yahir rivas
Last updated: 6/20/2026
Description: 
"""



def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: None (Printed text is not returned)
    """

    print()

    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")

    print()

    player_name, player_class ,player_attacklr, player_attacksr,ultimate = create_player()
   
    if player_class == "warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
        print( """  
                                    /)
                                   //
                 __*_             //
              /-(____)           //
             ////- -|\          //
          ,____o% -,_          //
         /  \    |||  ;       //
        /____\....::./\      //
       _/__/#\_ _,,_/--\    //
       /___/######## \/""-(\) 
     /___\  __  /___\/     |
 mrf/____ \ '__'//____\   __| 
               """)
        
    elif player_class == "mage":
        health = 50
        mana = 100

        print("A cunning mage, capable of outwitting the strongest foe.")
        print( """     
                                       .
                             /^\     .
                        /\   "V"
                       /__\   I      O  o
                      /|..|\  I     .
                      \].`[/  I
                      /l\/j\  (]    .  O
                     /. ~~ ,\/I          .
                     \ L__j^\/I       o
                      \/--v}  I     o   .
                      |    |  I   _________
                      |    |  I o(`       ')o
                      |    l  I   \.     ,/  
                    _/j  L l\_!  _/ ^---^ \_
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)
    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))
    print("short range attack:",player_attacksr)
    print("long range attack:",player_attacklr)
    print("--------------------------------------")


    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")

    while True:
        x=input("press f to continue")
        if x == "f":
            break
    print("""
                 ,-_                  (`  ).    
                 |-_'-,              (     ).   
                 |-_'-'           _(        '`. 
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.' 
      /-.-;,-,___|'          `(       ) )       
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )      
        x_( __`|_P_|`-;-;-;,|        `--'       
        |\ \    _||   `-;-;-'                   
        | \`   -_|.      '-'                    
        | /   /-_| `                            
        |/   ,'-_|  \                           
        /____|'-_|___\                          
 _..,____]__|_\-_'|_[___,.._                    
'                          ``'--,..,.           
      """)
    
    while True: 
        print("while exiting you home you see a poster saying where/when to meet the spartans")
        print("They're kingdom, you know exaclty where to go")
        decision_terrain =input("First,You must choose a path! desert or the forest?")
     # decision point where player will either go into desert or forest terrain
        if decision_terrain == "forest" or decision_terrain == "desert":
            break
    if decision_terrain== "desert":
        print("""
            .    _    +     .  ______   .          .
 (      /|\      .    |      \      .   +
     . |||||     _    | |   | | ||         .
.      |||||    | |  _| | | | |_||    .
   /\  ||||| .  | | |   | |      |       .
__||||_|||||____| |_|_____________\__________
. |||| |||||  /\   _____      _____  .   .
  |||| ||||| ||||   .   .  .         ________
 . \|`-'|||| ||||    __________       .    .
    \__ |||| ||||      .          .     .
 __    ||||`-'|||  .       .    __________
.    . |||| ___/  ___________             .
   . _ ||||| . _               .   _________
_   ___|||||__  _ \\--//    .          _
     _ `---'    .)=\oo|=(.   _   .   .    .
_  ^      .  -    . \.|  
you traverse the unforgiving desert and ponder your life for a while
thinking about the past...           
              """) 
        while True:
            x=input("press f to continue")
            if x == "f":
                break

        
        print(player_name,"while traversing the desert you.. find find a frog in a blender!?!? ")
        print("""
           ___
   _______|___|______
__|__________________|
\  ]________________[ `---.
 `.                   ___  L
  |   _              |   L |
  | .'_`--.___   __  |   | |
  |( 'o`   - .`.'_ ) |   F F
  | `-._      `_`./_ |  / /
  J   '/\\    ( .'/ )F.' /
   L ,__//`---'`-'_/J  .'
   J  /-'        '/ F.'
    L            ' J'
    J `.`-. .-'.'  F
     L  `.-'.-'   J
     |__(__(___)__|
     F            J
    J              L
    |______________|
              """)
        
        while True: 
            decision_fightd = input("DO YOU CHOOSE TO TOUCH IT!? y/n")
            if decision_fightd == "y" or decision_fightd == "n" :
                break
            
        if decision_fightd == "y":
            health = 0
            mana = 0
            print("This caused a chain reaction resulting in a NUCLEAR EXPLOSION")
            print("""
     _.-^^---....,,--
 _--                  --_
&lt;                        &gt;)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&amp;%$#=-'
          | ;  :|
 _____.,-#%&amp;$@%#~,._____                                
                  """)
            print("Health: {}".format(health))
            print("Mana: {}".format(mana))
            print("YOU HAVE DIED")
        if  decision_fightd == "n":
            print("it looked suspicous anyways you think to yourself")
            print("""
While walking you find a 4th dimensional object.
    _---_        _---_
_.-'     '-./\.-'     '-._
 '-._   _.-'\/'-._   _.-'
     `,` |__/\__| `,`
      |    /  \    |
      '---<    >---'
           \  /
            \/
you find it interesting and put it in your pocket.              
    
by Joan G. Stark (Spunk)  
  """)
            print("you keep walking for days and finally..")
            while True:
                x=input("press f to continue")
                if x =="f":
                    break
            
            print("""
                                                  !_        
                                                  |*~=-.,   
                                                  |_,-'`    
                                                  |         
                                                  |         
                                                 /^\        
                   !_                           /   \       
                   |*`~-.,                     /,    \      
                   |.-~^`                     /#"     \     
                   |                        _/##_   _  \_   
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]  
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|   
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |    
           |*`--,_- _        |            |*`~-.,= []  |    
           |.-'|=     []     |   !_       |_.-"`_-     |    
           |   |_=- -        |   |*`~-.,  |  |=_-      |    
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |    
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |    
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |    
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |    
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\   
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \  
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \ 
     | _- =-     |-_   | ((* |      |= _=       | -    |___\

     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/ 
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/  
     | _ ^^^^^   |= -  | |  | |     |=_=^^^^^   |_=-   |/   
     |=_ =       | =_-_| |  | |     |   =_      | -_   |    
     |_=-_       |=_=  | |  | |     |=_=        |=-    |           
       """)
            print("you ENTER and fight all the fodder and finally get to..")
            while True:
                x=input("press f to continue")
                if x == "f":
                    break
            print( """  
THE ONE TRUE SPARTAN. 
                  _,.
                ,` -.)
                ( _/-\-._
              /,|`--._,-^|            ,
              \_| |`-._/||          ,'|
                |  `-, / |         /  /
                |     || |        /  /
                `r-._||/   __   /  /
            __,-<_     )`-/  `./  /
            '  \   `---'   \   /  /
                |           |./  /
                /           //  /
            \_/' \         |/  /
            |    |   _,^-'/  /
            |    , ``  (\/  /_
            \,.->._    \X-=/^
            (  /   `-._//^`
            `Y-.____(__}
                |     {__)
                    ()     
this is all thats left between you and ally, 
                  
TIME TO FIGHT!!
            """)
            while True:
                print(player_attacklr)
                
                print(player_attacksr)
                
                attack=input("choose your attack!")

                if attack == player_attacklr or attack == player_attacksr:
                    break
            print("--------------------------")
            print("you have chosen",attack)
            print("this heavily damages the spartan and drops his health by half")
            while True:
                x=input("press f to continue")
                if x == "f":
                    break

            print("""
The sparten uses sword dance... 
                   _____   _____
                  /     \ /     \\

             ,   |       '       |
             I __L________       L__
       O====IE__________/     ./___   >
             I      \.       ./
             `        \.   ./
                        \ /
                         '
       
it lands and pierces your HEART! 
you take heavy bleeding damage and can't take anymore Hits!!       
                  """)
            
            health = 5
            mana = 15
            print("Health:",health)
            print("Mana:",mana)      
            while True:
                buff = input("you still have your 4ht dimensional object, do you use it? y/n")
                if buff == "y" or buff=="n" :
                    break
            if buff =="y":
                health = 10
                mana = 100000
                print("---------------------------------")
                print("YOU eat the strange object and find that it tasts like strawberry. you have unlocked,",ultimate)
                print("health:",health)
                print("mana:",mana)
                print("your options",
                    player_attacklr,
                    player_attacksr,
                    ultimate)
                while True:
                    attack = input("type your choice")
                    if attack == player_attacklr or attack == player_attacksr or attack == ultimate: 
                        break
                if attack == ultimate:
                    print("you use",ultimate)
                    print("The spartan trys to dodge as the attack goes towards him")
                    while True:
                        x= input("press f to continue")
                        if x == "f":
                            break
                    print("""
He fails and the attack lands on him perfectly instantly nullliflying him.        
     _______________
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .-'''''-.
      .'  * * *  `.
     :  *       *  :
    : ~S A V I O R ~:
    : ~ A W A R D ~ :
     :  *       *  :
jgs   `.  * * *  .'
        `-.....-'
      """)
                    print(player_name,"WINS.")
                if attack == player_attacklr or attack == player_attacksr :
                    print("-------------------------------")
                    print("you chose",attack)
                    print("The spartan attempts to dodge as the attack goes to him")
                    while True:
                        x=input("press f to continue")
                        if x == "f":
                            break
                    print("""
He succeded and counter attacks
   |   
 .'|'. 
/.'|\ \\     
| /|'.|
 \ |\/ 
  \|/  
   `                                          
With a swish of his sword he marks you with a curse stamp sealing you away, forever.
You have died.                     
                          """)


            if buff == "n":
                print("you chose not to use it")
                print("you have enough mana for",player_attacklr)
                while True:
                    attack2=input("do you use it? y/n")
                    if attack2 == "y" or attack2=="n":
                        break
                health = 0
                mana = 0
                print("""
Before you get to do anything the spartan strikes!                    
   |   
 .'|'. 
/.'|\ \\     
| /|'.|
 \ |\/ 
  \|/  
   `                                          
He marks you with a curse stamp sealing you away, forever.
You have died.
                """)
                print("mana:",mana)
                print("health:",health)

            

    elif decision_terrain == "forest":
        print(""" 
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
you go into the forest, you note that it seems different from the other times.
Like something that shouldn't be is living in it, you feel... uneasy.                         
              """)
        while True:
            x=input("press f to continue")

            if x == "f":
                break
        print("""
while traversing the forest you find an ALIEN!!
a 10 foot alien TOWERING over you.
    o   o
     )-(
    (O O)
     \=/
    .-"-.
   //\ /\\
              
 _// / \ \\_
=./ {,-.} \.=
    || ||
    || ||    hjw
  __|| ||__  `97
 `---" "---'  
luckily you hid in a bush before it spotted you              
              """)
        while True:
            decision_fightf = input("DO YOU CHOOSE TO go out and FIGHT IT!? y/n")
            if decision_fightf == "y" or decision_fightf == "n" :
                break
        print("----------------")
        if decision_fightf == 'y':
            health = 0
            mana = 0
            print("""
             o
            \_/\o
            ( Oo)                    \|/
            (_=-)  .===O-  ~~Z~A~P~~ -O-
            /   \_/U'                /|\
            ||  |_/
            \   |
            {K ||
            | PP
            | ||
            (__ \
            by: Andrew Carpenter """) 
               
            print("The alien zaps you")
            print("YOU HAVE DIED") 
            print("Health: {}".format(health))
            print("Mana: {}".format(mana))
        if decision_fightf == 'n':

            print("eh that alien looked scary anyways, thinks",player_name)
            print("""You sneak around it, noting the weird noises it's making
it sends a shiver down your spine""")

            while True:
                x=input("press f to continue")
                if x == "f":
                    break
            print("""
while sneaking around it you trip over some sourdough bread, you find it interesting 
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣔⣶⣎⠉⠉⠓⠦⡀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠋⠁⠀⠀⠀⠙⠻⢆⠀⠀⠀⣹⡄⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⠴⠿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀
            ⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⢀⢾⠟⠀⠀
            ⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⡀⣔⣿⠗⠀⠀⠀
            ⠀⠀⠀⡮⣝⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⣷⡟⠁⠀⠀⠀⠀
            ⠀⠀⡞⠀⠀⠁⠙⠀⠀⠀⠀⠀⠀⠀⠀⣠⢀⡯⡞⠁⠀⠀⠀⠀⠀⠀
            ⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢔⡱⡽⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⢸⡀⠀⠀⠀⠀⡠⡠⠦⢧⢯⣫⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠙⢷⣧⠭⢝⡻⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀

Enough that it makes you take it with you, perhaps it will be useful.  
                """)
            while True:
                x= input("press f to continue")
                if x == "f":
                    break
            print( """  
after a few days you get to the kingdom and defeat all the fodder,   
                  _,.
                ,` -.)
                ( _/-\-._
              /,|`--._,-^|            ,
              \_| |`-._/||          ,'|
                |  `-, / |         /  /
                |     || |        /  /
                `r-._||/   __   /  /
            __,-<_     )`-/  `./  /
            '  \   `---'   \   /  /
                |           |./  /
                /           //  /
            \_/' \         |/  /
            |    |   _,^-'/  /
            |    , ``  (\/  /_
            \,.->._    \X-=/^
            (  /   `-._//^`
            `Y-.____(__}
                |     {__)
                    ()     
all thats left between you and ally, is the one true spartan
TIME TO FIGHT!!
            """)
            while True:
                print(player_attacklr)
                
                print(player_attacksr)
                
                attack=input("choose your attack!")

                if attack == player_attacklr or attack == player_attacksr:
                    break
            print("--------------------------")
            print("you have chosen",attack)
            print("this heavily damages the spartan and drops his health by half")
            while True:
                x=input("press f to continue")
                if x == "f":
                    break

            print("""
The sparten uses sword dance... 
                   _____   _____
                  /     \ /     \\

             ,   |       '       |
             I __L________       L__
       O====IE__________/     ./___   >
             I      \.       ./
             `        \.   ./
                        \ /
                         '
       
it lands and pierces your HEART! 
you take heavy bleeding damage and can't take anymore Hits!!       
                  """)
            
            health = 5
            mana = 15
            print("Health:",health)
            print("Mana:",mana)      
            while True:
                buff = input("you still have your sourdough, do you use it? y/n")
                if buff == "y" or buff=="n" :
                    break
            if buff =="y":
                health = 10
                mana = 100000
                print("---------------------------------")
                print("YOU choose to eat the sourdough bread and have unlocked,",ultimate)
                print("health:",health)
                print("mana:",mana)
                print("your options",
                    player_attacklr,
                    player_attacksr,
                    ultimate)
                while True:
                    attack = input("type your choice")
                    if attack == player_attacklr or attack == player_attacksr or attack == ultimate: 
                        break
                if attack == ultimate:
                    print("you use",ultimate)
                    print("The spartan trys to dodge as the attack goes towards him")
                    while True:
                        x= input("press f to continue")
                        if x == "f":
                            break
                    print("""
He fails and the attack lands on him perfectly instantly nullliflying him.        
     _______________
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .-'''''-.
      .'  * * *  `.
     :  *       *  :
    : ~S A V I O R ~:
    : ~ A W A R D ~ :
     :  *       *  :
jgs   `.  * * *  .'
        `-.....-'
      """)
                    print(player_name,"WINS.")
                if attack == player_attacklr or attack == player_attacksr :
                    print("-------------------------------")
                    print("you chose",attack)
                    print("The spartan attempts to dodge as the attack goes to him")
                    while True:
                        x=input("press f to continue")
                        if x == "f":
                            break
                    print("""
He succeded and counter attacks
   |   
 .'|'. 
/.'|\ \\     
| /|'.|
 \ |\/ 
  \|/  
   `                                          
With a swish of his sword he marks you with a curse stamp sealing you away, forever.
You have died.                     
                          """)


            if buff == "n":
                print("you chose not to use it")
                print("you have enough mana for",player_attacklr)
                while True:
                    attack2=input("do you use it? y/n")
                    if attack2 == "y" or attack2=="n":
                        break
                health = 0
                mana = 0
                print("""
Before you get to do anything the spartan strikes!                    
   |   
 .'|'. 
/.'|\ \\     
| /|'.|
 \ |\/ 
  \|/  
   `                                          
He marks you with a curse stamp sealing you away, forever.
You have died.
                """)
                print("mana:",mana)
                print("health:",health)

    # Add branches to the adventure here!

    
    return 1


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
            -player_attacklr(string): sets the long range attack of the player
            -player_attacksr(string): sets the short range attack of the player
            -ultimate(string): sets the players strongest attack after taking a buff
    """
    player_name = input("Before we begin, what should I call you? ")

    while True :
        #loops until either "mage" or "warrior" is inputted
        player_class = input("What is your specialty? [warrior / mage] ")
        if player_class == "mage" or player_class == "warrior" :
            break 
# this sets the attacks that the player will have
    if player_class == "mage":
        player_attacklr = "hellforge"
        player_attacksr = "inferno"
        ultimate= "HOURS END"
    elif player_class =="warrior":
        player_attacklr = "omni-slash"
        player_attacksr = "star split"
        ultimate= "ONE LESS"


    return player_name, player_class,player_attacklr,player_attacksr,ultimate


win = 0
while win == 0:
    win = adventure()