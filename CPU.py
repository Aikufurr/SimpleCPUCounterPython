import RAM
from time import sleep


simpleCounter = {
0: [1, 6], # Load
1: ["B", 7], # Add
2: [4, 6], # Store
3: ["D", 1], # Jump
4: [0, 0],
5: [0, 0],
6: [0, 1],
7: [0, 1],
}

RAM.writeToAddress(None, simpleCounter, 1, 1)

clock = 2  # CPU Clock
PC = 0  # Programme Counter
IR = None  # Instruction Register
AC = None  # Accumulator
AV = None  # Address/Value
action = None  # What to do
value = None  # Temp Value to use

"""
KEY:
action:
 0 - LOAD
 1 - ADD
 2 - STORE
 3 - JUMP
 4 - VAR
"""


while True:
    AV = RAM.readFromAddress(PC)
    if AV[0] == 1:
        action = 0
    elif AV[0] == "B":
        action = 1
    elif AV[0] == 4:
        action = 2
    elif AV[0] == "D":
        action = 3
    else:
        action = 4
    IR = [action, AV[1]]
    if IR[0] == 0:
        AC = RAM.readFromAddress(IR[1])[1]
        PC += 1
    elif IR[0] == 1:
        AC += RAM.readFromAddress(IR[1])[1]
        PC += 1
    elif IR[0] == 2:
        RAM.writeToAddress(IR[1], [0, AC], 0 ,0)
        PC += 1
    elif IR[0] == 3:
        PC = IR[1]
    clock += 1
    if clock % 3 == 0:
        print(AC)
    sleep(.05)
