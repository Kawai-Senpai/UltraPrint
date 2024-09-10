
#? Print in different colors ----------------------------------------------
#! Red 
def red(*args):
    print("\033[91m {}\033[00m".format(''.join(map(str, args))))

#! Green
def green(*args):
    print("\033[92m {}\033[00m".format(''.join(map(str, args))))

#! Yellow
def yellow(*args):
    print("\033[93m {}\033[00m".format(''.join(map(str, args))))

#! Blue
def blue(*args):
    print("\033[94m {}\033[00m".format(''.join(map(str, args))))

#! Purple
def purple(*args):
    print("\033[95m {}\033[00m".format(''.join(map(str, args))))

#! Cyan
def cyan(*args):
    print("\033[96m {}\033[00m".format(''.join(map(str, args))))

#! Light Gray
def lgray(*args):
    print("\033[97m {}\033[00m".format(''.join(map(str, args))))

#! Dark Gray
def dgray(*args):
    print("\033[90m {}\033[00m".format(''.join(map(str, args))))

#? Print in different styles ---------------------------------------------
#! Bold
def bold(*args):
    print("\033[1m {}\033[0m".format(' '.join(map(str, args))))

#! Underline
def underline(*args):
    print("\033[4m {}\033[0m".format(' '.join(map(str, args))))

#! Negative
def negative(*args):
    print("\033[3m {}\033[0m".format(' '.join(map(str, args))))

#? Print in different background colors ----------------------------------

#! Red Background
def red_bg(*args):
    print("\033[41m {}\033[00m".format(' '.join(map(str, args))))

#! Green Background
def green_bg(*args):
    print("\033[42m {}\033[00m".format(' '.join(map(str, args))))

#! Yellow Background
def yellow_bg(*args):
    print("\033[43m {}\033[00m".format(' '.join(map(str, args))))

#! Blue Background
def blue_bg(*args):
    print("\033[44m {}\033[00m".format(' '.join(map(str, args))))

#! Purple Background
def purple_bg(*args):
    print("\033[45m {}\033[00m".format(' '.join(map(str, args))))

#! Cyan Background
def cyan_bg(*args):
    print("\033[46m {}\033[00m".format(' '.join(map(str, args))))

#! Light Gray Background
def lgray_bg(*args):
    print("\033[47m {}\033[00m".format(' '.join(map(str, args))))

#! Dark Gray Background
def dgray_bg(*args):
    print("\033[100m {}\033[00m".format(' '.join(map(str, args))))

#? Other -----------------------------------------------------------------

#! Easy New Line
def n(n=1):
    for i in range(n):
        print()