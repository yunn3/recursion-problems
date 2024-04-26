def validEmailList(emailList: list) -> list:
    result = []

    for mail in emailList:
        if isValidEmail(mail):
            result.append(mail)

    return result


def isValidEmail(mail: str) -> bool:
    if mail.find(" ") != -1:
        return False

    at_mark_index = mail.find("@")

    if at_mark_index == -1:
        return False

    if mail.find("@", at_mark_index + 1) != -1:
        return False

    if mail.find(".", at_mark_index + 1) == -1:
        return False

    if at_mark_index == 0:
        return False

    return True
