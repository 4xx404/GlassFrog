import sys
sys.dont_write_bytecode = True

import emojis
from .Colors import bc

class sd:
    iBan: str = emojis.encode(f" :star:{bc.BC}")
    sBan: str = emojis.encode(f" :white_check_mark:{bc.BC}")
    eBan: str = emojis.encode(f" :x:{bc.RC} ERROR:{bc.BC}")

    Author = f"{bc.BC}\n Author: {bc.RC}4{bc.GC}x{bc.BC}x{bc.RC}4{bc.GC}0{bc.BC}4\n"
    Version = f"{bc.BC} Version: {bc.RC}3{bc.GC}.{bc.BC}0\n"
    Github = f"{bc.BC} Github: {bc.RC}h{bc.GC}t{bc.BC}t{bc.RC}p{bc.GC}s{bc.BC}:{bc.RC}/{bc.GC}/{bc.BC}g{bc.RC}i{bc.GC}t{bc.BC}h{bc.RC}u{bc.GC}b{bc.BC}.{bc.RC}c{bc.GC}o{bc.BC}m{bc.RC}/{bc.GC}4{bc.BC}x{bc.RC}x{bc.GC}4{bc.BC}0{bc.RC}4\n"

    Logo = f'''{bc.RC}
    {bc.GC}   ___  __      __    ___  ___  ____  ____  _____  ___     _   _   
    {bc.BC}  / __)(  )    /__\  / __)/ __)( ___)(  _ \(  _  )/ __)   (.)_(.)  
    {bc.RC} ( (_-. )(__  /(__)\ \__ \\\__ \ )__)  )   / )(_)(( (_-.  (   _   ) 
    {bc.GC}  \___/(____)(__)(__)(___/(___/(__)  (_)\_)(_____)\___/  /`-----'\ 
    {Author}{Version}{Github}'''

    ComingSoon = f"{eBan} [{bc.GC} * * *{bc.BC} ] EXTENDER COMING SOON! [{bc.GC} * * *{bc.BC} ]\n"