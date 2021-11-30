def myencode(message, coding):
    Language = 'ABCDEFGHIGKLMNOPQRSTUVWXYZDEFGHIGKLMNOPQRSTUVWXYZABC abcdefghigklmnopqrstuvwxyzdefghigklmnopqrstuvwxyzabc'
    result = ''
    for i in message:
        shifr = Language.find(i)
        new_shifr = shifr + coding
        if i in Language:
            result += Language[new_shifr]
        else:
            result += i
    return result

