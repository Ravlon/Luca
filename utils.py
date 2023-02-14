def yes(question: str) -> bool:
    """Input a string that you want to prompt to the user to receive a yes or no.
    The function appends '[y/n]: ' ad the end of your string and prompts user to give an answer.
    It then checks for various iterations of yes.

    Returns False if answer was negative, and True if it was affirmative"""
    answer = input(question + " [y/n]: ")
    if answer.lower() == "y" or answer.lower() == "yes":
        return True
    else:
        return False

    return False

def progress(status,terms):
    """_summary_

    Args:
        status (_type_): _description_
        terms (_type_): _description_

    Returns:
        _type_: _description_
    """
    stat_bar = 75
    completion = float(status)*100.0/float(terms)
    if status%7==0:
        blink = 0
    else:
        blink = 1
    seg_fill = (int(stat_bar*(completion/100))+1)*blink
    if status >= terms:
        seg_fill = stat_bar
    seg_null = stat_bar-seg_fill
    print('['+'*'*(seg_fill)+' '*(seg_null)+']'+'{0:>6.2f}%\t'.format(completion), end = '\r', flush = True)
    return 0
