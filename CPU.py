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

RAM.writeToAddress(None, simpleCounter, 1, 1)  # Writes the data to RAM overwriting any exisiting data

clock = 2  # CPU Clock
PC = 0  # Programme Counter
IR = None  # Instruction Register
AC = None  # Accumulator
AV = None  # Address/Value
action = None  # What to do
value = None  # Temp Value to use


while True:
    AV = RAM.readFromAddress(PC)  # Reads RAM at address of the Programme Counter
    if AV[0] == 1:  # converts the RAM instructions to a simple int
        action = 0
    elif AV[0] == "B":
        action = 1
    elif AV[0] == 4:
        action = 2
    elif AV[0] == "D":
        action = 3
    else:
        action = 4
    IR = [action, AV[1]]  # Sets the Instruction Register to the action and the value
    if IR[0] == 0:  # Load
        AC = RAM.readFromAddress(IR[1])[1]  # Load the value from RAM to Accumulator
        PC += 1  # Increase Programme Counter by 1
    elif IR[0] == 1:  # ADD
        AC += RAM.readFromAddress(IR[1])[1]  # Adds value from RAM to Accumulator
        PC += 1  # Increase Programme Counter by 1
    elif IR[0] == 2:  # Store
        RAM.writeToAddress(IR[1], [0, AC], 0 ,0)
        PC += 1  # Increase Programme Counter by 1
    elif IR[0] == 3:  # Jump
        PC = IR[1]  # Sets Programme Counter to value from RAM
    clock += 1  # Increase Clock by one
    if clock % 3 == 0:  # If clock is devisable by 3, or every 3 times
        print(AC)  # Print the Accumulator
    sleep(.05)  # Sleep for 50ms
