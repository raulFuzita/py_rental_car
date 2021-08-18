
def fmt_card_number(number: int, cardlengh: int=16, separator: str='-') -> str:
    number = str(number).rjust(cardlengh, '0')
    formatedNum = ''
    for i in range(0, len(number)):
        if (i+1) != 0 and (i+1) % 4 == 0:
            formatedNum += number[i] + separator
        else:
            formatedNum += number[i]
    return formatedNum[:-1]

def fmt_card_cvv(cvv: int, cardlength: int=3) -> str:
    return str(cvv).rjust(cardlength, '0')

