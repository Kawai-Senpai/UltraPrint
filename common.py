#? Print in different colors ----------------------------------------------
#! Red 
def red(*args, end="\n"):
    print("\033[91m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Green
def green(*args, end="\n"):
    print("\033[92m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Yellow
def yellow(*args, end="\n"):
    print("\033[93m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Blue
def blue(*args, end="\n"):
    print("\033[94m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Purple
def purple(*args, end="\n"):
    print("\033[95m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Cyan
def cyan(*args, end="\n"):
    print("\033[96m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Light Gray
def lgray(*args, end="\n"):
    print("\033[97m {}\033[00m".format(''.join(map(str, args))), end=end)

#! Dark Gray
def dgray(*args, end="\n"):
    print("\033[90m {}\033[00m".format(''.join(map(str, args))), end=end)

#? Print in different styles ---------------------------------------------
#! Bold
def bold(*args, end="\n"):
    print("\033[1m {}\033[0m".format(' '.join(map(str, args))), end=end)

#! Underline
def underline(*args, end="\n"):
    print("\033[4m {}\033[0m".format(' '.join(map(str, args))), end=end)

#! Negative
def negative(*args, end="\n"):
    print("\033[3m {}\033[0m".format(' '.join(map(str, args))), end=end)

#? Print in different background colors ----------------------------------

#! Red Background
def red_bg(*args, end="\n"):
    print("\033[41m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Green Background
def green_bg(*args, end="\n"):
    print("\033[42m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Yellow Background
def yellow_bg(*args, end="\n"):
    print("\033[43m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Blue Background
def blue_bg(*args, end="\n"):
    print("\033[44m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Purple Background
def purple_bg(*args, end="\n"):
    print("\033[45m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Cyan Background
def cyan_bg(*args, end="\n"):
    print("\033[46m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Light Gray Background
def lgray_bg(*args, end="\n"):
    print("\033[47m {}\033[00m".format(' '.join(map(str, args))), end=end)

#! Dark Gray Background
def dgray_bg(*args, end="\n"):
    print("\033[100m {}\033[00m".format(' '.join(map(str, args))), end=end)

#? Other -----------------------------------------------------------------

#! Easy New Line
def n(n=1):
    for i in range(n):
        print()

#? Screen Management ----------------------------------------------------

#! Clear Screen
def cls():
    """Clear the entire console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#! Clear Previous Line
def cls_prev():
    """Clear the previous line in the console."""
    print('\033[F\033[K', end='')
