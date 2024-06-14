def validEmailList(emailList):
    result = []

    for mail in emailList:
        if isValidEmail(mail):
            result += mail

    return result


def isValidEmail(mail):
    count_loop = 0
    count_at = 0
    at_position = 0
    dot_position = 0

    for character in mail:
        if character == "@":
            count_at += 1
            at_position = count_loop
            count_loop += 1

        elif character == ".":
            dot_position = count_loop
            count_loop += 1

    if count_at != 1:
        return False
    elif at_position == 0:
        return False
    elif dot_position < at_position:
        return False

    return True
