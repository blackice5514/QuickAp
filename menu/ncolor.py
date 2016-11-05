

class color():

    MAUVE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLEU = '\033[94m'
    VERT_OK = '\033[92m'
    JAUNE = '\033[93m'
    ROUGE = '\033[91m'
    BOLD = '\033[1m'
    SOULIGNE = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'
    VERT = '\033[32m'
    DARKYELLOW = '\033[33m'
    DARKGREY = '\033[90m'
    DARKROUGE = '\033[34m'
    t = '\033[36m'#darkscyan
    d = '\033[33m'#darkyellow
    r = '\033[91m'
    rr = '\033[31m'
    dim = '\033[2m'
    y = '\033[33m'
    v = '\033[92m'

    err = ROUGE + "[-]" + ENDC



    #check the status of the dhcp object and return the good color 
    def Color_check(option):
        if option == "N/A":
            option = '\033[91m'
            return option
        
        else:
            option = '\033[32m'
            return option

    def Color_check_pass(option):
        if option == "N/A":
            option = '\033[91m'
            return option
        
        else:
            option = '\033[36m'
            return option

    def color_checkINT(option, int_stat):
        if option == "N/A":
            option = '\033[90m'
            return option

        elif int_stat == False:
            option = '\033[90m'
            return option
        
        else:
            option = '\033[94m'
            return option

    def check_notselect(option, name):
        if "'N/A'" in option:            
            new = color.ENDC + '\033[90m' + " 'N/A'" + color.ENDC
            option = color.dim + " " + name + new
            return option
        
        else:            
            return option

    def check_dns(option):
        if "N/A" in option:
            return "# dns: " + color.ENDC + "\033[90m" + "'not fowarding'" + color.ENDC
        else:
            return "# dns: " + "\033[92m" + "'fowarding'" + color.ENDC

    def check_attack(option):
        if option == " NOT WEAPONIZED ":
            return color.DARKGREY + "'" + "not weaponised" + "'" + color.ENDC

        else:
            return color.VERT + "weaponised" + color.ENDC







            






    





