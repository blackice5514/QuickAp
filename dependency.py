from menu.ncolor import *
from write.misc import check_Choice
import subprocess
import os

######################################### dependency_check ###############################################
#       module containing the code to check if the necessary package are installed on the system.        #                                                                                        #
##########################################################################################################


class dependency_check():

    def __init__(self):
        self.missing_man = []
        self.dnsmasq = True
        self.hostapd = True
    
    
    # check if mandatory dependency are installed.

    def dependency_chk(self):

        # check if dnsmasq is installed.
        if not os.path.exists("/usr/share/dnsmasq"):
           self.dnsmasq = False
           self.missing_man.append("dnsmasq")

         # check if hostapd is installed.
        if not os.path.exists("/usr/sbin/hostapd"):
           self.hostapd = False
           self.missing_man.append("hostapd")
    
    # handle the missing mandatory package menu.
    
    def menu_missing_man(self):        

        print(color.r + "# the following mandatory package are missing!" + color.ENDC)
        dependency_check.iterating(self.missing_man, color.t)
        
        print("\n" + "do you want to install the following package? (y/n).")               
        choice = check_Choice("install") # handle choice and error.

        if choice == "y":
            # install package and check if successful.            
            install_chk = dependency_check.install_package(self) 
            return install_chk

        else:
            print(color.r + "[*] quick ap will not start if the necessary package are not installed!")
            return False

   # install the missing mandatory package.

    def install_package(self):
        fail_install = []       
       
        # for each package in the list we try to install it.
        for x in self.missing_man:            
            try:
               print(color.VERT + "# installing " + x + "!" + color.ENDC)
               subprocess.check_call(['apt-get', 'install', x])
            
            except subprocess.CalledProcessError:
                fail_install.append(x) # if error detected, the package not installed is stored in 'fail_install'.
        
        if fail_install: # if one package in the list is detected.
            print (color.r + "# the following package were not installed!" + color.ENDC)
            dependency_check.iterating(fail_install, color.t)         
            print(color.r + "\n[*] restart quick ap or try to install the package manually!")
            return False

        else:
            print (color.v + "# all the package were successfuly installed!" + color.ENDC)
            input(color.y + "\npress enter to continue...")
            return True


    # show all the missing package in the list.
    
    def iterating(depen_list, couleur):        
        i = 0        
        
        for x in depen_list:
            i += 1
            print(str(i) + "." + couleur + " " + "'" + x + "'" + color.ENDC)


        

  
    