def LindIter(System, N):
    if System == "Koch":
        LindenmayerString = "S"
    elif System == "Sierpinski":
        LindenmayerString = "A"

    rules = {"S": "SLSRSLS", "L": "L", "R": "R", "A": "BRARB", "B": "ALBLA", "D": "DLDDRDL"}

    def LindString(start):
        output = ''
        for letter in start:
            LindenmayerString = rules[letter]
            output += LindenmayerString
        return output
