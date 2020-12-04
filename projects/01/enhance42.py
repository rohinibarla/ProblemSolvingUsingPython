def e42_add(number1, number2):
    return number1 + number2


def e42_substract(number1, number2):
    return number1 - number2


def e42_show(number):
    # the message we wish to print
    message = str(number)

    # the printed banner version of the message
    # this is a 7-line display, stored as 7 strings
    # initially, these are empty.
    printedMessage = ["", "", "", "", "", "", ""]

    # a dictionary mapping letters to their 7-line
    # banner display equivalents. each letter in the dictionary
    # maps to 7 strings, one for each line of the display.
    characters = {" ": [" ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " "],

                  "-": ["       ",
                        "       ",
                        "       ",
                        " ----- ",
                        "       ",
                        "       ",
                        "       "],

                  "1": ["   *   ",
                        "   *   ",
                        "   *   ",
                        "   *   ",
                        "   *   ",
                        "   *   ",
                        "   *   "],

                  "2": [" ***** ",
                        "      *",
                        "      *",
                        " ***** ",
                        "*      ",
                        "*      ",
                        " ***** "],

                  "3": [" ***** ",
                        "      *",
                        "      *",
                        " ***** ",
                        "      *",
                        "      *",
                        " ***** "],

                  "4": ["*      ",
                        "*      ",
                        "*      ",
                        "*   *  ",
                        "*******",
                        "    *  ",
                        "    *  "],


                  "5": [" ***** ",
                        "*      ",
                        "*      ",
                        " ***** ",
                        "      *",
                        "      *",
                        " ***** "],

                  "6": [" ******",
                        "*      ",
                        "*      ",
                        " ***** ",
                        "*     *",
                        "*     *",
                        " ***** "],

                  "7": ["*******",
                        "      *",
                        "     * ",
                        "    *  ",
                        "   *   ",
                        "  *    ",
                        " *     "],

                  "8": [" ***** ",
                        "*     *",
                        "*     *",
                        " ***** ",
                        "*     *",
                        "*     *",
                        " ***** "],

                  "9": [" ***** ",
                        "*     *",
                        "*     *",
                        " ***** ",
                        "      *",
                        "      *",
                        " ***** "],

                  "0": [" ***** ",
                        "*     *",
                        "*     *",
                        "*     *",
                        "*     *",
                        "*     *",
                        " ***** "],
                  }

    # build up the printed banner. to do this, the 1st row of the
    # display is created for each character in the message, followed by
    # the second line, etc..
    for row in range(7):
        for char in message:
            printedMessage[row] += (str(characters[char][row]) + "  ")
    print("")
    # print each line of the message, including the offset.
    for row in range(7):
        print(printedMessage[row])
    print(" ")
