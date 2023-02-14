"""
Various format settings automatically formatting given numbers,string and other objects.
Returning string in the desired format.
"""

def thousands(num):
    """Insert the dot and commas where appropriate in the number.

    Args:
        num (int): scalar to be formatted
    
    Returns: string
    """
    units = str(int(num))
    # decimals = str(num - int(num))
    # decimals = list(decimals)[2:2+5]
    # if int(decimals[-1]) > 4:
    #     decimals[-2] = str(int(decimals[-2])+1)
    #     decimals.pop()
    # decimals = int("".join(decimals))
    result = ''
    while units:
        ...

    return result

def money(N, cur="€"):
    """Scalar at the moment.
        Format is:  '€ (t,ggg,mmm,kkk,uuu.dddd)'

    Args:
        N (scalar,list): list of numbers, float or ints, or a scalar.
        cur (str, optional): Currency symbol to be used for the formatted string. Defaults to "€".
    
    Returns: string
    """
    if N:
        ...

class row ():
    def form(self, format_array = (" ",">","5")) -> str:
        fill, align, width = format_array
        return "{0:"+str(fill)+str(align)+str(width)+"}"

    def __init__(self, content:list, formats: list) -> None:
        divider = " | "
        self.line = ""
        for col in range(len(content)):
            forma = self.form(formats[col])
            self.line += divider + forma.format(content[col])
        self.line += divider
    
    def __repr__(self) -> str:
        return self.line
    
    def __str__(self) -> str:
        return self.line

class grid():
    def __init__(self, matrix, formats = [], header = []) -> None:
        self.line = []
        self.matrix = matrix
        self.header = row(header, formats)
        self.make_formatter(formats)
        for r in range(len(matrix)):
            text = str(row(matrix[r], formats))
            self.line.append(text)
    
    def __str__(self) -> str:
        table = str(self.header) + "\n"
        for l in self.line:
            table += l + "\n"
        return table

    def make_formatter(self, formats:list):
        pass


# Use Unicode to enter other currencies.
if __name__ == "__main__":
    header = ["WORDS","NUMBS","RANDOM"]
    forms = [(" ",">","6"),(" ",">","5"),(" ","<","10")]
    content = [["FJORD","10500","FN394FMCM"],["BEVER","203","°çé*"],["LUCIA","20.5","£$fWD"],["MAXER","-10*","F34F5"],["FIGAO","88888","D23FJ239"],["KAKAO","1","23D"],["WHISKY","","FER"]]
    table = grid(content, forms, header)
    print(table)
    # print(u"\xA3")
    # print(u"\u00A5")
    # print(b"\xA3".decode("latin-1"))
    # print(u"\u20AC")
    # print(b"\xA4".decode('iso-8859-15'))
    # print(b"\xA4".decode("latin-1"))


