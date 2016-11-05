from menu.ncolor import *
from menu.showMainMenu import *
from menu.showSubMenu import *
from menu.Header import banner
from menu.check_menu import *
from command.shell import check_command
from write.hostapd_write import *
from write.dnsmasq_write import *
from write.save_write import *
import subprocess
from dependency import *
import readline

close_message = color.VERT + "[*] saving the configuration before exiting quick ap!"
close_message2 = color.JAUNE + "[*] thank you for using quick ap!"
valid_choice = color.ROUGE + "[-]" + color.ENDC + " please enter a valid choice!"



def Main():   
    
    # object for the the current missing dependency
    miss_pkg = dependency_check()    
    
    # checking what are the missing dependency.
    miss_pkg.dependency_chk()    
    
    # check if missing mandatory package are in the list.  
    if miss_pkg.missing_man:      
       try:
          if not miss_pkg.menu_missing_man():
             print (color.y + "[*] exiting the program!")
             return # if the install fail we exit the program.

       except (KeyboardInterrupt):
          print(color.y + "\n[*] exiting the program!")
          return



    # object for the current user choice.
    default = Showstatus("Quick Ap", "N/A", "N/A", "ON", "N/A", "N/A", "N/A", " NOT WEAPONIZED ")
    user = default    
  
    # if the save file exist we change the user object with the attribute comming from the the save file.
    
    if check_save():
      
      obj = read_save()       
      user = Showstatus(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6], obj[7])
    
    
    while True:

        banner.Show_Banner()
        user.MainMenuAttack()
        user.MainMenuStat()            
        
           
        try:
           Menu_choice = Showstatus.MainMenuChoice()
        
           if Menu_choice == "2":
              user.ssid = Sub_Menu.nameMenu(user.ssid)               
            
           elif Menu_choice == "3":
              user.password = Sub_Menu.PassordMenu(user.crypt, user.password)

           elif Menu_choice == "4":
              user.crypt, user.password = Sub_Menu.securityMenu(user.crypt, user.password)

           elif Menu_choice == "5":
              user.dhcp = Sub_Menu.dhcpMenu(user.dhcp)

           elif Menu_choice == "6":
              user.dns = Sub_Menu.dnsMenu(user.dns)

           elif Menu_choice == "7":
              user.in_INT, user.in_OUT = Sub_Menu.interfaceMenu(user.in_INT, user.in_OUT)

           elif Menu_choice == "8":
              # change object to default if needed.
              user = restore_save(default, user)

           elif Menu_choice == "9":
               # closing the program
               print(close_message)
               print(close_message2)
               write_save(user)
               break
           
           elif Menu_choice == "":              
              
              # writing the configuration in hostapd.conf.
              hostapd_write(user.ssid, user.in_INT, user.crypt, user.password)

              # writing the configuration in hostapd.conf.
              dnsmasq_write(user.in_INT, user.dns, user.dhcp)
              
              # status menu.
              handle = startCheck.show_result(user.in_INT, user.in_OUT)
              
              # starting the hostspot.
              start_quickAP.start(handle, user.in_INT, user.in_OUT, user.ssid, user.crypt, user.attack, user.password, user.dns)               
           
           else:
              print(valid_choice)
              time.sleep(1)
    

        except (KeyboardInterrupt):
           print ("\n" + close_message)
           print (close_message2)
           write_save(user)
           break

    
          
        



if __name__ == "__main__":
     Main()