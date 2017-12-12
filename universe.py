import time

class Planet:
    def __init__(self):
        ascii("circle")
        self.days = {
            "light": ("Let there be light!", "zeroth"),
            "valt": ("Let there be a vault between the waters to separate water from water.", "first"),
            "land-sea": ("Let the water under the sky be gathered to one place, and let dry ground appear", "second"),
            "sun": ("Let there be lights in the vault of the sky to separate the day from the night, and let them serve as signs to mark sacred times, and days and years, 15 and let them be lights in the vault of the sky to give light on the earth.", "third"),
            "birds-fish": ("Let the water teem with living creatures, and let birds fly above the earth across the vault of the sky.", "fourth"),
            "animals": ("Let the land produce living creatures according to their kinds: the livestock, the creatures that move along the ground, and the wild animals, each according to its kind.", "fifth"),
            "rest": ("")
        }
        self.orderedDays = ["light", "valt", "land-sea", "sun", "birds-fish", "animals","rest"]


    def letThereBe(self, key, speed=2):
        try:
            self.orderedDays.index(key)
        except:
            print("invalid day")
            return(None)

        if(key == "rest"):
            print("Then God blessed the seventh day and made it holy, because on it he rested from all the work of creating that he had done.")
            time.sleep(2)
            ascii("rest")
            exit()

        self.currentDay = key
        print('And God said "' + self.days[key][0] + '"')
        time.sleep(speed)
        ascii(key)
        time.sleep(2)
        print("And the evening and the morning were the " + self.days[key][1] + " day.")

    def letThereBeAutomation(self):
        if(not self.currentDay):
            print("You need to make at least one day")
            return(None)
        
        day = self.currentDay
        i = self.orderedDays.index(day)

        remaininDays = self.orderedDays[i+1:]

        for day in remaininDays:
            self.letThereBe(day, 0.5)



def help():
    print("light, valt, land-sea, sun, birds-fish, animals")


def ascii(key):
    light = """
      _.,----,._
    .:'        `:.
  .'              `.
 .'                `.
 :                  :
 `    .'`':'`'`/    '
  `.   \  |   /   ,'
    \   \ |  /   /
     `\_..,,.._/'
      {`'-,_`'-}
      {`'-,_`'-}
      {`'-,_`'-}
       `YXXXXY'
         ~^^~"""
    circle = """
        x  x
     x        x
    x          x
    x          x
     x        x
        x  x
        """
    valt = """
                           .')             _
                          (_  )        .+(`  ) ) -a:f-
                _                     :(    ) )
            .:(`  )  ) --        .--  `.  (    ) )  - --
           :(      )           .(   )   ` __.:'
    `.     `(       ) )       (      )
      )      ` __.:'   ))--- (       )) ----      _
    )  ) --         --'  _    `- __.'         .=(`  )
    .-'                (`  ).                :(      )
                     (       '`. .  --       `(       ) ) ) ----
                     (         ) ) ---         ` __.:'
                      ` __.:'-'






                    _
                  (`  ).                   _
                 (     ).              .:(`  )`.
    )           _(       '`.          :(   .    )
            .=(`(      .   )     .--  `.  (    ) )
           ((    (..__.:'-'   .+(   )   ` _`  ) )
    `.     `(       ) )       (   .  )     (   )  ._
      )      ` __.:'   )     (   (   ))     `-'.-(`  )
    )  )  ( )       --'       `- __.'         :(      ))
    .-'  (_.'          .')                    `(    )  ))
                      (_  )                     ` __.:'

    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.
    """

    landSea = """
    _      _      _      _      _      _      _      _
    )`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
    """

    sun = """
        .-''''`-
       F   .-'
      F   J
     I    I
      L   `.
       L    `-._,
        `-.__.-'

                ^^                   @@@@@@@@@
           ^^       ^^            @@@@@@@@@@@@@@@
                                @@@@@@@@@@@@@@@@@@              ^^
                               @@@@@@@@@@@@@@@@@@@@
     ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
     ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
       ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
       ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
     ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
           ~             ~        ~      ~      ~~   ~             ~
    pjb
    """
    birds = """
                         ___     ___
                  ,_    / _,\   /,_ \    _,
                  | \   \( \|   |/ )/   / |
                  |  \_  \\\\       //  _/  |
                  (_   \_) \     / ( /   _)
                  (\_   `   \   /   `   _/)
              jgs ,\   -=~  /   \  ~=-   /,
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             .               `         /
                              .    ,../...       .
              .                .  /       `\  /  .
         \    .        o         < '  )     =<
         /\  .                    \ \      /  \   .  __
       >=)'>                       `'\\'"'"'         /o \/
         \/ .    /         o              /,        \__/\    .:/
         /   .  /--\ /         /         <')=<     .      ,,///;,   ,;/
               ::::::::;;\\\\\\
                 \            \_/            .            ''\\\\\\\\\\' ';\\
        (                      \              .   __
         )                                       <'_><          (
        (          (                ,/..          `              )
         )     (    )             <')   `=<                )    (
        (       )  (               ``\```                 (      )
    _____)_____(____)______________________________________)____(_______jgs_
    """
    animals = """
           .        .
           \'.____.'/
          __'-.  .-'__                         .--.
          '_i:'oo':i_'---...____...----i''"-.-'.-"\\
            /._  _.\       :       /   '._   ;/    ;'-._
           (  o  o  )       '-.__.'       '. '.     '-."
            '-.__.-' _.--.                 '-.:
             : '-'  /     ;   _..--,  /       ;
             :      '-._.-'  ;     ; :       :
              :  `      .'    '-._.' :      /
               \  :    /    ____....--\    :
                '._\  :""' '    '.     !.   :
                 : |: :           'www'| \ '|
                 | || |              : |  | :
                 | || |             .' !  | |
                .' !| |            /__I   | |
               /__I.' !                  .' !
                  /__I                  /__I   fsc
                  __
           .-'  '-.
          /        )
          |  C   o(
           \       >
            )  \  /      ..`'
         .-._ / `'      /////
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'
    """

    rest = """
     .::""-,                       .::""-.
    /::     \                     /::     \\
    |::     |   _..--'""''--.._   |::     |
    '\:.__ /  .'              '.  \:.__ /
     ||____|.' _..---"````'---. '.||____|
     ||:.  |_.'                `'.||:.  |
     ||:.-'`       .-----.        ';:.  |
     ||/         .'       '.        \.  |
     ||         / '-.   '. \\\\       |.  |
     ||:.     _| '   \_\_\\\\/(        \  |
     ||:.\_.-' )     ||   m `\.--._.-""-;
     ||:.(_ . '\ __'// m ^_/ /    '.   _.`.
     ||:.  \__^/` _)```'-...'   _ .-'.'    '-.
     ||:..-'__  .'        '. . '      '.      `'.
     ||:(_.' .`'        _. ' '-.         '.   . ''-._
     ||:. :   '.     .'          '.  . ' ' '.`       '._
     ||:.  :    '. .'     .::""-: .''.        ' .   . ' ':::''-.
     ||:. .'    ..' .    /::     \    '.        . '.    /::     \\
     ||:.'    .'      '. |::     |    _.:---""---.._'   |::     |
     ||.      :          '\:.__ /   .'    -.  .-    '.   \:.__ /
     ||:     : '.       . ||____|_.'    .--.  .--.    '._||____|
     ||:'.___:   '.   .'  ||:.  |      (    \/    )      ||:.  |
     ||:___| \     '. :   ||:.  |       '-.    .-'       ||:.  |
     [[____]  '.     '.-._||:.  |      __  '..'  __      ||:.  |
                '.    :   ||:.  |     (__\ (\/) /__)     ||:.  |
                  '.  :   ||:.  |        `  \/  `        ||:.  |
                    '-:   ||:.  |           ()           ||:.  |
                       '._||:.  |________________________||:.  |
                      jgs ||:___|'-.-'-.-'-.-'-.-'-.-'-.-||:___|
                          [[____]                        [[____]
    """
    db = {
        "light": light,
        "circle": circle,
        "valt": valt,
        "sun": sun,
        "land-sea": landSea,
        "birds-fish": birds,
        "animals": animals,
        "rest": rest
    }
    print(db.get(key))
