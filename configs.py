###CUT THE WIRES###

# #the pins used for the Cut The Wires module
wirePin1 = 4
wirePin2 = 5
wirePin3 = 6

wire1 = {'pin': wirePin1}
wire2 = {'pin': wirePin2}
wire3 = {'pin': wirePin3}


wireConfigs = [
    {
        'wire1' : wire1,
        'wire2' : wire2,
        'wire3' : wire3,
        'wiresToSolve' : [wire1],
        'wiresToLeave' : [wire2, wire3],
        'type': 'vowel'
    },
    {
        'wire1' : wire1,
        'wire2' : wire2,
        'wire3' : wire3,
        'wiresToSolve' : [wire1, wire3],
        'wiresToLeave' : [wire2],
        'type': 'odd'
    },
    {
        'wire1' : wire1,
        'wire2' : wire2,
        'wire3' : wire3,
        'wiresToSolve' : [wire1, wire2],
        'wiresToLeave' : [wire3],
        'type': 'even'
    }
]

#the basic wire setup for Cut The Wires
defaultWireConfig = wireConfigs[1]

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

keypadConfigs = [
    {
        'word' : "JANKY",
        "hint" : "KNEW",
        'sequence' : "51659"
    },
    {
        'word' : "MEMES",
        "hint" : "NEW",
        'sequence' : "63637"
    },
    {
        'word' : "JOCKO",
        "hint" : "BLUE",
        'sequence' : "56256"
    },
    {
        'word' : "WUMBO",
        "hint" : "BLEW",
        'sequence' : "98626"
    },
    {
        'word' : "KOPIE",
        "hint" : "FLU",
        'sequence' : "56743"
    },
    {
        'word' : "MUSIK",
        "hint" : "FLEW",
        'sequence' : "68745"
    },
    {
        'word' : "HUYAM",
        "hint" : "TO",
        'sequence' : "48926"
    },
    {
        'word' : "PUJAH",
        "hint" : "TOO",
        'sequence' : "78524"
    },
    {
        'word' : "JIGGY",
        "hint" : "TWO",
        'sequence' : "54449"
    },
    {
        'word' : "MUSAK",
        "hint" : "YOURE",
        'sequence' : "68725"
    },
    {
        'word' : "BROWS",
        "hint" : "YORE",
        'sequence' : "27697"
    },
    {
        'word' : "PRISE",
        "hint" : "UR",
        'sequence' : "77473"
    },
    {
        'word' : "PRIES",
        "hint" : "YOUR",
        'sequence' : "77437"
    },
    {
        'word' : "TERSE",
        "hint" : "YOU",
        'sequence' : "83773"
    },
    {
        'word' : "TERCE",
        "hint" : "U",
        'sequence' : "83723"
    },
    {
        'word' : "SLOES",
        "hint" : "EWE",
        'sequence' : "75637"
    },
    {
        'word' : "SLOWS",
        "hint" : "EW",
        'sequence' : "75697"
    }
]


###BUTTON###
#basic object for button
defaultButtonConfig = {
    "color" : "blue"
}

buttonColors = [
    {'color': 'red'},
    {'color': 'green'},
    {'color': 'blue'},
    {'color': 'purple'}
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
    "                GAME OVER",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "            _.-^^---....,,--._     ",
    "        _--                  --_  ",
    "       <                        >)",
    "       |                         | ",
    "        \._                   _./  ",
    "           ```--. . , ; .--'''       ",
    "                 | |   |             ",
    "              .-=||  | |=-.   ",
    "              `-=#$%&%$#=-'   ",
    "                 | ;  :|     ",
    "        _____.,-#%&$@%#&#~,._____"
]

bomb = "\
\n\
\n             DEFUSE THIS BOMB\
\n\
\n\
\n\
\n\
\n\
\n                   . . .\
\n                    \\|/\
\n                  `--+--'\
\n                    /|\\\
\n                   ' | '\
\n                     |\
\n                     |\
\n                 ,--'#`--.\
\n                 |#######|\
\n              _.-'#######`-._\
\n           ,-'###############`-.\
\n         ,'#####################`,\
\n        /#########################\\\
\n       |###########################|\
\n      |#############################|\
\n      |#############################|\
\n      |#############################|\
\n      |#############################|\
\n       |###########################|\
\n        \\#########################/\
\n         `.#####################,'\
\n           `._###############_,'\
\n              `--..#####..--'"
