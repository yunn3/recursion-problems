class RGB:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def getHexCode(self):

        hexColorCode = ""

        hexColorCode += self.getHexCodeHelper(self.red)
        hexColorCode += self.getHexCodeHelper(self.green)
        hexColorCode += self.getHexCodeHelper(self.blue)

        return "#" + hexColorCode

    def getHexCodeHelper(self, decimalNum):

        if decimalNum < 10:
            return "0" + str(decimalNum)

        hexNum = ""

        decimalToHexList = "0123456789abcdef"

        while decimalNum >= 1:
            hexNum = decimalToHexList[decimalNum % 16] + hexNum
            decimalNum = decimalNum // 16

        return hexNum

    def getBits(self):

        stringHexNum = self.getHexCode()
        hexToDecimalList = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]
        hasMeaningNum = False
        bitNum = ""

        for hexNum in stringHexNum:

            if hexNum == "#":
                continue

            elif not hasMeaningNum and hexNum == "0":
                continue

            elif hasMeaningNum and hexNum == "0":
                bitNum += "0000"

            elif not hasMeaningNum and hexNum != "0":
                decimalNum = hexToDecimalList.index(hexNum, 1, 16)

                bitNum += self.getBitsHelper(decimalNum, hasMeaningNum)
                hasMeaningNum = True

            else:
                decimalNum = hexToDecimalList.index(hexNum, 1, 16)
                bitNum += self.getBitsHelper(decimalNum, hasMeaningNum)

        return bitNum

    def getBitsHelper(self, decimalNum, hasMeaningNum):

        bitNum = ""

        while decimalNum >= 1:
            bitNum = str(decimalNum % 2) + bitNum
            decimalNum = decimalNum // 2

        # もし、hasmeaningNumがFalseであれば、出力された二進数の先頭の"0"は省略されたままにする。
        # もし、hasmeaningNumがTrueであれば、必要数の "0" を付ける。
        if hasMeaningNum:
            toAddZero = 4 - len(bitNum)
            if toAddZero > 0:
                bitNum = "0" * toAddZero + bitNum

        return bitNum

    def getColorShade(self):

        if self.red == self.green == self.blue:
            return "grayscale"

        elif (
            self.red >= self.green
            and self.red > self.blue
            or self.red >= self.blue
            and self.red > self.green
        ):
            return "red"

        elif (
            self.green >= self.red
            and self.green > self.blue
            or self.green >= self.blue
            and self.green > self.red
        ):
            return "green"

        return "blue"


color1 = RGB(0, 153, 255)
color2 = RGB(255, 255, 204)
color3 = RGB(0, 87, 0)
gray = RGB(123, 123, 123)

print(color1.getHexCode())
print(color1.getBits())
print(color1.getColorShade())
print(color2.getHexCode())
print(color2.getBits())
print(color2.getColorShade())
print(color3.getHexCode())
print(color3.getBits())
print(color3.getColorShade())
print(gray.getHexCode())
print(gray.getBits())
print(gray.getColorShade())
