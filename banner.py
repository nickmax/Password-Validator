import colored 
from colored import fg ,attr

yellow = fg("light_yellow")
red = fg("light_red")
green = fg("light_green")
reset = attr("reset")
cyan =fg("light_cyan")

def logo():
    print(red +" ____   _    ____ ______        _____  ____   ____          " + reset)
    print(red +"|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \ |  _  \         " + reset)
    print(green +"| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_)| | | |  _____ " + reset) 
    print(green +"|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _< | |_| | |_____| " + reset)
    print(cyan +"|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/  " + reset)      
                                                            
    print(cyan +"__     ___    _     ___ ____    _  _____ ___  ____   " + reset)
    print(cyan +"\ \   / / \  | |   |_ _|  _ \  / \|_   _/ _ \|  _ \  " + reset)
    print(yellow +" \ \ / / _ \ | |    | || | | |/ _ \ | || | | | |_) | " + reset)
    print(green +"  \ V / ___ \| |___ | || |_| / ___ \| || |_| |  _ <  " + reset)
    print(red +"   \_/_/   \_\_____|___|____/_/   \_\_| \___/|_| \_\ " + reset)
    print()