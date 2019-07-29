DATA = {}

def writeToAddress(address, value, dict, overwrite):
    if overwrite:
        for k in DATA:
            DATA[k] = [0, 0]
    if dict:
        for k in value:
            DATA[k] = value[k]
    else:
        DATA[address] = value

def readFromAddress(address):
    return DATA[address]
