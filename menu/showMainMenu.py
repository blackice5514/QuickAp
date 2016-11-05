from menu.ncolor import *
from command.shell import command 
from menu.check_menu import startCheck



class Showstatus():
    crypt_color = ""
    password_color = ""
    dhcp_color = ""
    dns_color = ""
       

    def __init__(self, ssid, password, crypt, dhcp, dns, in_INT, in_OUT, attack):
        self.ssid = ssid
        self.password = password
        self.crypt = crypt
        self.dhcp = dhcp
        self.dns = dns
        self.in_INT = in_INT
        self.in_OUT = in_OUT
        self.attack = attack

    def MainMenuAttack(self):       
        
        print ("%74s" % (color.DARKGREY + "-=[" + color.dim + color.r +  self.attack + color.ENDC + color.DARKGREY + "]=-") + color.ENDC + " (1)\n")        
      
    #showing the main menu and the option chosen.
    def MainMenuStat(self):
        
        #put genral status of the interface in the variables and return false if interface is down.
        addresse_in, addresse_out, check_in, check_out = command.nic_selectedStatus(self.in_INT, self.in_OUT)

        #changing the color to red if N/A is return
        password_color = color.Color_check_pass(self.password)
        crypt_color = color.Color_check(self.crypt)        
        dhcp_color = color.Color_check(self.dhcp)
        dns_color = color.Color_check(self.dns)
        
        #color will be the color of the status returned by nic_selected.
        color1 = color.color_checkINT(self.in_INT, check_in)
        color2 = color.color_checkINT(self.in_OUT, check_out)        

        print("%64s" % ("hotspot name: <--> [" + color.DARKCYAN + self.ssid + "" + color.ENDC + "]" + " (2)"))
        print("%64s" % ("password: <--> [" + password_color + self.password + "" + color.ENDC + "]" + " (3)"))
        print("%64s" % ("security: <--> [" + crypt_color + self.crypt + "" + color.ENDC + "]" + " (4)"))
        print("%64s" % ("dhcp server: <--> [" + dhcp_color + self.dhcp + "" + color.ENDC + "]" + " (5)"))
        print("%64s" % ("dns fowarding: <--> [" + dns_color + self.dns + "" + color.ENDC + "]" + " (6)"))
        print("%73s" % ("network: <--> [" + color1 + self.in_INT + color.ENDC + " -- " + color2 + self.in_OUT + color.ENDC + "]" + " (7)"))
        print("")
        print("%66s" % (color.DARKGREY + color.BOLD + "default-config:(8) exit:(9)" + color.ENDC))

        print(color.DARKYELLOW + "\npress 'enter' to start the ap or chose an option..." + color.ENDC)


    def MainMenuChoice():
        Choice = input(color.BLEU + "menu > " + color.ENDC)        
        return Choice

    









    




