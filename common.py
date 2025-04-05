#? Print in different colors ----------------------------------------------
#! Red 
def red(*args, end="\n", flush=False):
    print("\033[91m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Green
def green(*args, end="\n", flush=False):
    print("\033[92m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Yellow
def yellow(*args, end="\n", flush=False):
    print("\033[93m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Blue
def blue(*args, end="\n", flush=False):
    print("\033[94m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Purple
def purple(*args, end="\n", flush=False):
    print("\033[95m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Cyan
def cyan(*args, end="\n", flush=False):
    print("\033[96m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Light Gray
def lgray(*args, end="\n", flush=False):
    print("\033[97m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#! Dark Gray
def dgray(*args, end="\n", flush=False):
    print("\033[90m{}\033[00m".format(''.join(map(str, args))), end=end, flush=flush)

#? Print in different styles ---------------------------------------------
#! Bold
def bold(*args, end="\n", flush=False):
    print("\033[1m{}\033[0m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Underline
def underline(*args, end="\n", flush=False):
    print("\033[4m{}\033[0m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Negative
def negative(*args, end="\n", flush=False):
    print("\033[3m{}\033[0m".format(' '.join(map(str, args))), end=end, flush=flush)

#? Print in different background colors ----------------------------------

#! Red Background
def red_bg(*args, end="\n", flush=False):
    print("\033[41m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Green Background
def green_bg(*args, end="\n", flush=False):
    print("\033[42m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Yellow Background
def yellow_bg(*args, end="\n", flush=False):
    print("\033[43m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Blue Background
def blue_bg(*args, end="\n", flush=False):
    print("\033[44m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Purple Background
def purple_bg(*args, end="\n", flush=False):
    print("\033[45m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Cyan Background
def cyan_bg(*args, end="\n", flush=False):
    print("\033[46m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Light Gray Background
def lgray_bg(*args, end="\n", flush=False):
    print("\033[47m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#! Dark Gray Background
def dgray_bg(*args, end="\n", flush=False):
    print("\033[100m{}\033[00m".format(' '.join(map(str, args))), end=end, flush=flush)

#? Other -----------------------------------------------------------------

#! Easy New Line
def n(n=1, flush=False):
    for i in range(n):
        print(flush=flush)

#? Screen Management ----------------------------------------------------

#! Clear Screen
def cls():
    """Clear the entire console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#! Clear Previous Line
def cls_prev(flush=False):
    """Clear the previous line in the console."""
    print('\033[F\033[K', end='', flush=flush)
