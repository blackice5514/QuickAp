import subprocess
from menu.showMainMenu import *
from quick_ap import *
from command.shell import *
from menu.showSubMenu import Sub_Menu
import write.misc


go_back = color.DARKGREY + "  [ctrl + c] for going back!" + color.ENDC

class startCheck():
    



    # look at the status of the interface and return the appropriate decision.

    def situation(inside, outside):
        
        # adresse variable are getting the adresse, and check variable are getting the status.
        in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside)        

        #if one of the interface is not select return the appropriate situation.
        if inside == "N/A" and outside == "N/A":                   
            return "no interface"

        elif inside == "N/A" and outside != "N/A":
            return "only out selected"
        
        if inside != "N/A" and outside == "N/A":

            if in_ip == color.DARKGREY + "down" + color.ENDC:
                return "only in down"
            
            else:
                return "in up"

        
        # if all the interface are selected, return the appropriate situation
        if inside != "N/A" and outside != "N/A":

            #this is just horrible sorry for this. will have to fix this later.
            if in_ip == color.DARKGREY + "down" + color.ENDC and in_out == color.DARKGREY + "down" + color.ENDC:
                return "down down"
            
            elif in_ip != color.DARKGREY + "down" + color.ENDC and in_out != color.DARKGREY + "down" + color.ENDC:
                return "up up"
            
            elif in_ip != color.DARKGREY + "down" + color.ENDC and in_out == color.DARKGREY + "down" + color.ENDC:
                return "up down"

            elif in_ip == color.DARKGREY + "down" + color.ENDC and in_out != color.DARKGREY + "down" + color.ENDC:
                return "down up"
    


    


    

    def action_before_start(inside, outside, situation):

        if situation == "in up":        
            return situation
            
        elif situation == "only in down":
            situation = check_command.bring_interface_up(inside, outside)            
            return situation            
            
        elif situation == "down down":
            stat1 = check_command.bring_interface_up(inside, outside)            
            stat2 = check_command.bring_outside_up(inside, outside) 

            situation = startCheck.action_condition(stat1, stat2)
            return situation

        elif situation == "up up":
            return situation

        elif situation == "up down":
            stat1 = "in up"
            stat2 = check_command.bring_outside_up(inside, outside)

            situation = startCheck.action_condition(stat1, stat2)
            return situation

        elif situation == "down up":
            stat1 = check_command.bring_interface_up(inside, outside)
            stat2 = "out up"

            situation = startCheck.action_condition(stat1, stat2)
            return situation
        
        else:
            return situation
    

    

    


    def action_condition(stat1, stat2):
        
        if stat1 == "in up" and stat2 == "out up":
            return "up up"

        elif stat1 == "in up" and stat2 == "out down":
            return "up down"

        elif stat1 == "only in down" and stat2 == "out up":
            return "down up"

        elif stat1 == "only in down" and stat2 == "out down":
            return "down down"




    

    #taking the result of the situation function and show the appropriate message depending on the situation.

    def check_message(situation, inside, outside):

        try:

            if situation == "no interface":
               print (color.ROUGE + "\n[-]" + color.ENDC + " interfaces are not selected. please choose your interface before lauching")
               print ("    the access point!")
               stop = input(color.d + "\npress enter to continue..." + color.ENDC)
               return False

            elif situation == "only out selected":
               print (color.ROUGE + "\n[-]" + color.ENDC + " only the outside interface is selected. please choose the inside interface")
               print ("    if you want to start the access point!")
               stop = input(color.d + "\npress enter to continue..." + color.ENDC)
               return False

            elif situation == "only in down":
               print (color.ROUGE + "\n[-]" + color.ENDC + " the inside interface is down and the outside interface is not selected.")
               print ("    Quick ap will not be able start the access point!")
               stop = input(color.d + "\npress 'enter' to continue..." + color.ENDC)
               return False

            elif situation == "in up":
               print (color.BLEU + "\n[+]" + color.ENDC + " quick ap is ready. Only the inside interface will be use and the internet")
               print ("    will not be shared.")
               print(color.d + "\ndo you want to run quick ap with this configuration? (y/n)." + color.ENDC)

               choice = startCheck.check_choice("menu")
               share = startCheck.accept_config(choice)
               return share

            elif situation == "down down":
               print (color.ROUGE + "\n[-]" + color.ENDC + " the inside and the outside interface are down. Quick ap will not be able")
               print ("    to start the access point!")
               stop = input(color.d + "\npress enter to continue..." + color.ENDC)
               return False

            elif situation == "up up":
               print (color.VERT + "\n[+]" + color.ENDC + " quick ap is ready. the inside interface and the outside interface are all")
               print ( "    up and selected!")
               print(color.d + "\ndo you want to share the internet? (y/n)." + go_back)

               choice = startCheck.check_choice("menu")
               share = startCheck.out_checkup(choice, inside, outside)
               return share

            elif situation == "up down":
               print (color.BLEU + "\n[+]" + color.ENDC + " quick ap is ready. Only the inside interface is up. the internet will not")
               print ("    be shared.")
               print(color.d + "\ndo you want to run quick ap with this configuration? (y/n)." + color.ENDC)

               choice = startCheck.check_choice("menu")
               share = startCheck.accept_config(choice)
               return share

            elif situation == "down up":
               print (color.ROUGE + "\n[-]" + color.ENDC + " the inside interface is down. Quick ap will not be able to start the")
               print ("    access point.")
               stop = input(color.d + "\npress enter to continue..." + color.ENDC)
               return False

        except (KeyboardInterrupt):
               return False





    def status_start(inside, outside):       
        
        
        # adresse variable are getting the adresse, and check variable are getting the status.
        in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside)
        
        # the variable are getting the status color.
        c1 = color.color_checkINT(inside, check_in)
        c2 = color.color_checkINT(outside, check_out) 
 
        # base on color_check return, stat_in and out take the inerface status
        if c1 == '\033[90m':
            stat_in = color.DARKGREY + "down" + color.ENDC
        else:
            stat_in = color.VERT + "active" + color.ENDC

        if c2 == '\033[90m':
            stat_out = color.DARKGREY + "down" + color.ENDC
        else:
            stat_out = color.VERT + "active" + color.ENDC
        
        # getting the organisation name for each interface.
        in_OUI = OUI_search(inside)
        out_OUI = OUI_search(outside) 
        
        # print stat befor lauching hotspot.
        test = color.DARKGREY + " " + "OUI:" " unknown" + color.ENDC
        
        print("")
        print ("%27s" % (color.t + " (inside)" + color.ENDC + " interface: [" + c1 + inside + color.ENDC + "]" + " " + in_OUI))           
        print ("%10s" % (" adresse: " + in_ip))
        print ("%10s" % (" status: " + stat_in))       
        print("")
        print ("%27s" % (color.t + " (outside)" + color.ENDC + " interface: [" + c2 + outside + color.ENDC + "]" + " " + out_OUI))           
        print ("%10s" % (" adresse: " + in_out))
        print ("%10s" % (" status: " + stat_out))       
                    
               
   
    
    # if choice is yes, check if the outside interface have an ip and perform a test of connection.

    def out_checkup(choice, inside, outside):
        
        if choice == "y" or choice == "":
            share = startCheck.out_check(choice, inside, outside)
            share = startCheck.ping_check(share, outside)
            return share
        
        elif choice == "no":            
            return "only_in"  

   
    
   
    
    # the user get the choice to try again if the outside interface do not get an ip adresse. If the
    # user got an ip adresse or chose not to share we get out of the loop.
    
    def out_check(choice, inside, outside):
        choice2 = ""
        
        # adresse variable are getting the adresse, and check variable are getting the status.
        in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside) 
       
        while in_out == color.r + "no ip" + color.ENDC  and choice2 != "n":     
                        
            if in_out == color.r + "no ip" + color.ENDC: 
               print (color.ROUGE + "\n[-]" + color.ENDC + " the outside interface do not have and ip address. Make sure that you are") 
               print ("    connected to the network.")
               print(color.d + "\ntry to share the internet again? (y/n)." + color.ENDC)
               choice2 = input(color.BLEU + "lauch > " + color.ENDC)

               if choice2 == "n":
                  return False
            
            # check again if ip before returning in the loop.
            in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside)
        
        #we got an ip share gonna be true.
        return True
    

    

    
    # if we want to share, the connection to the internet will be tested and give a warning if the 
    # ping is not reaching google dns server, 

    def ping_check(share, outside):

        if share == True:
            print(color.BLEU + "[*]" + color.ENDC + " testing the connection from the outside interface to the internet...")

            try:
                subprocess.check_call(['ping', '-c', '1', '-I', outside, '8.8.8.8'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                print(color.VERT + "[+]" + color.ENDC + " connexion to the internet from " + color.VERT + "'" + outside + "'" + color.ENDC + " is good!")
                time.sleep(1)
                start_command.error = False
                return True

            except subprocess.CalledProcessError:
                print (color.ROUGE + "[-]" + color.ENDC + " !! WARNING !! the internet connection from " + color.t + "'" + outside + "'" + color.ENDC + " seem not to work!")
                start_command.error_message()
                time.sleep(3)
                
                return True
        
        elif share == False:            
            return False

    


    
    def check_choice(menu):     
        
        while True:                   
            choice = input(color.BLEU + menu + " > " + color.ENDC)
            
            if choice == "y" or choice == "n" or choice == "":
                return choice
            else:
                print(color.ROUGE + "[-]" + color.ENDC + " please enter a valid choice!")


    
    
    
    def accept_config(choice):

        if choice == "" or choice == "y":
            return "only_in"

        else:
            return False

     

    

    def Menu_back():        
        print (color.VERT + "[+]" + color.ENDC + " main menu.")
        time.sleep(0.3) 



    
    # regrouping all the funtion together to handle the checkup menu.
    
    def show_result(inside, outside):      
        

        # look the interface status and return the appropriate decision.
        situation = startCheck.situation(inside, outside)
       
        # do some action before the checkup.
        situation = startCheck.action_before_start(inside, outside, situation)
        
        # check the status and show the appriopriate result. 
        startCheck.status_start(inside, outside) 
             
        # receive the decision and execute or give the choice to execute the appropriate action.
        handle = startCheck.check_message(situation, inside, outside)

        return handle




class start_quickAP():

    # execute all the specific command for starting the access point with the appropriate
    # configuration.
    
    def start(net_share, inside, outside, ssid, crypt, attack, password, dns):
        
        if net_share == False:
            return

        else:            
            start_quickAP.internet_seq(inside, outside, ssid, crypt, attack, net_share, password, dns)            
                  


    
    # regrouping all the function from the shell module for the sequence with no internet.
    
    def internet_seq(inside, outside, ssid, crypt, attack, net_share, password, dns):
        
        # make sure that the old configuration of networkmanager.conf is remember.
        old_config = read_default_netmanager()
        
        try:
            # tell the network manager to ignore the inside interface and start it with the new ip addresse.
            net_manager_old = start_command.network_manager(inside, outside)       
       
            # if we are sharing the internet the iptables rule will be apply.
            if net_share == True:
              start_command.ip_tables(outside)        

            # starting the dnsmasq server (dhcp - dns).
            start_command.start_dnsmasq()
        
            # stating hotapd for starting the wireless hotspot.
            start_command.start_hostapd()

        # handeling the exeption if this important section is interupted.
        except (KeyboardInterrupt):
            print (color.ROUGE + "\n# the starting sequence was interrupted! quick ap will kill the remaining")            
            print ("  process and go back to the main menu!")
            time.sleep(3)
            default_netmanager(old_config)
            start_command.killing_process()
            
        
        else:         
            # check the if hostapd and dnsmasq are running correctly. 
            start_command.execution(net_share, ssid, crypt, attack, net_manager_old, password, dns)








    
       

       

                             
