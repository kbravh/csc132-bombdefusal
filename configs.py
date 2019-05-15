###CUT THE WIRES###

# #the pins used for the Cut The Wires module
wirePin1 = 4
wirePin2 = 5
wirePin3 = 6

wire1 = {'pin': wirePin1}
wire2 = {'pin': wirePin2}
wire3 = {'pin': wirePin3}


wireConfigVowel = {
    'wire1' : wire1,
    'wire2' : wire2,
    'wire3' : wire3,
    'wiresToSolve' : [wire1],
    'wiresToLeave' : [wire2, wire3],
    'type': 'vowel'
}
wireConfigOdd = {
    'wire1' : wire1,
    'wire2' : wire2,
    'wire3' : wire3,
    'wiresToSolve' : [wire1, wire3],
    'wiresToLeave' : [wire2],
    'type': 'odd'
}
wireConfigEven = {
    'wire1' : wire1,
    'wire2' : wire2,
    'wire3' : wire3,
    'wiresToSolve' : [wire1, wire2],
    'wiresToLeave' : [wire3],
    'type': 'even'
}

#the basic wire setup for Cut The Wires
defaultWireConfig = wireConfigVowel

wireConfigs = [
    wireConfigVowel, wireConfigOdd, wireConfigEven
]

vowelSerialNumbers = [
    'XJD45E23',
    'TU69H2A0',
    'SY54RU7X',
    'RTYI4532',
    'AK89F3OD',
    'M0OR17LG'
]
oddSerialNumbers = [
    'XJD45123',
    'T269H229',
    'SY54RT77',
    'RTYS4533',
    'QK89F3M1',
    'M00R17L5'
]
evenSerialNumbers = [
    'XJD45124',
    'T269H222',
    'SY54RT78',
    'RTYS4536',
    'QK89F3M4',
    'M00R17L2'
]

###KEYPAD###
#basic object for keypad module
defaultKeypadConfig = {
    'word' : "HELLO",
    "hint" : "YORE",
    'sequence' : "43556"
}

keypadConfig1 = {
    'word' : "JANKY",
    "hint" : "KNEW",
    'sequence' : "51659"
}

keypadConfig2 = {
    'word' : "MEMES",
    "hint" : "NEW",
    'sequence' : "63637"
}

keypadConfig3 = {
    'word' : "JOCKO",
    "hint" : "BLUE",
    'sequence' : "56256"
}

keypadConfig4 = {
    'word' : "WUMBO",
    "hint" : "BLEW",
    'sequence' : "98626"
}

keypadConfig5 = {
    'word' : "KOPIE",
    "hint" : "FLU",
    'sequence' : "56743"
}

keypadConfig6 = {
    'word' : "MUSIK",
    "hint" : "FLEW",
    'sequence' : "68745"
}

keypadConfig7 = {
    'word' : "HUYAM",
    "hint" : "TO",
    'sequence' : "48926"
}

keypadConfig8 = {
    'word' : "PUJAH",
    "hint" : "TOO",
    'sequence' : "78524"
}

keypadConfig9 = {
    'word' : "JIGGY",
    "hint" : "TWO",
    'sequence' : "54449"
}

keypadConfigs = [
    keypadConfig1, keypadConfig2, keypadConfig3, keypadConfig4, keypadConfig5, keypadConfig6, keypadConfig7, keypadConfig8, keypadConfig9
]

###BUTTON###
#basic object for button
defaultButtonConfig = {
    "color" : "blue"
}

buttonColors = [
    {'color': 'red'},
    {'color': 'green'},
    {'color': 'blue'}
]

console_texts = [
    "system boot",
    "\nrw init=/sysroot/bin/bash",
    "\nrd.lvm.lv=centos/root/swap crash",
    "\nvolume serial number: querying...",
    "\ninitrd16 /initramfs-4.10.1-1.e17.e1repo.x86_64.img",
    "\n-----------------------",
    "\n./init_modules.sh",
    "\nLoaded: /opt/config/configs.sys",
    "\nkeypad initiated; config[key.set] => search -cf \"keyword\"",
    "\nkeyword: querying...",
    "\n-----------------------",
    "\nBootup successful; process initializing...",
    "\ntime left: --:--:--",
    "\nfatal_strikes = 3 => : "
]

console_full_text = "system boot\
                \nrw init=/sysroot/bin/bash\
                \nrd.lvm.lv=centos/root/swap crash\\\
                \nvolume serial number: {}\
                \ninitrd16 /initramfs-4.10.1-1.e17.e1repo.x86_64.img\
                \n-----------------------\
                \n./init_modules.sh\
                \nLoaded: /opt/config/configs.sys\
                \nkeypad initiated; config[key.set] => search -cf \"keyword\"\
                \nkeyword: {}\
                \n-----------------------\
                \nBootup successful; process initializing...\
                \ntime left: {}:{}:{}\
                \nfatal_strikes = 3 => : {}"

explosion = [
    "              GAME OVER",
    "",
    "",
    "",
    "          _.-^^---....,,--._     ",
    "      _--                  --_  ",
    "     <                        >)",
    "     |                         | ",
    "      \._                   _./  ",
    "         ```--. . , ; .--'''       ",
    "               | |   |             ",
    "            .-=||  | |=-.   ",
    "            `-=#$%&%$#=-'   ",
    "               | ;  :|     ",
    "      _____.,-#%&$@%#&#~,._____"
]

bomb = "\
\n\
\n                      DEFUSE THIS BOMB\
\n\
\n\
\n\
\n\
\n\
\n                            . . .\
\n                             \\|/\
\n                           `--+--'\
\n                             /|\\\
\n                            ' | '\
\n                              |\
\n                              |\
\n                          ,--'#`--.\
\n                          |#######|\
\n                       _.-'#######`-._\
\n                    ,-'###############`-.\
\n                  ,'#####################`,\
\n                 /#########################\\\
\n                |###########################|\
\n               |#############################|\
\n               |#############################|\
\n               |#############################|\
\n               |#############################|\
\n                |###########################|\
\n                 \\#########################/\
\n                  `.#####################,'\
\n                    `._###############_,'\
\n                       `--..#####..--'"