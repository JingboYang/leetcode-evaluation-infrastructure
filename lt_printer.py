from colorama import init
init(autoreset=True)

from colorama import Fore, Back, Style

def string_to_color(color, fb='for'):
    if color is None:
        return ''
    
    for_dict = {'red': Fore.RED,
                'green': Fore.GREEN,
                'black': Fore.BLACK,
                'blue': Fore.BLUE,
                'yellow': Fore.YELLOW,
                'cyan': Fore.CYAN,
                'white': Fore.WHITE,
                'magenta': Fore.MAGENTA}
    
    back_dict = {'red': Back.RED,
                'green': Back.GREEN,
                'black': Back.BLACK,
                'blue': Back.BLUE,
                'yellow': Back.YELLOW,
                'cyan': Back.CYAN,
                'white': Back.WHITE,
                'magenta': Back.MAGENTA}
    
    if fb == 'for':
        return for_dict[color]
    else:
        return back_dict[color]


def cprint(string, fcolor=None, bcolor=None):
    print(cstring(string, fcolor=None, bcolor=None))

def cstring(string, fcolor=None, bcolor=None):
    return string_to_color(fcolor, 'for') + string_to_color(bcolor, 'back')  + str(string) + Style.RESET_ALL

if __name__ == '__main__':
    cprint('Hello World!', 'red', 'green')
