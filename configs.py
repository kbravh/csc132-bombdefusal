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