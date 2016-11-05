import time
from menu.ncolor import *
from menu.showMainMenu import *
from command.shell import *
from write.dnsmasq_write import *

class Sub_Menu():
    
    dns_message = """ you can add a redirect entry in this menu or edit the dnsmasq configuration 
 file located in""" + color.BLEU + """ '/etc/redirect/dnsmasq.host'\n """ + color.ENDC

    
    
    #the user choose a new name. the input of the user will be put in the user
    #object   

    
    def nameMenu(ssid):   
      while True:
         print ("\nthe current name of the access point is " + color.VERT + "'" + ssid + "'" + color.ENDC)
         print("")
         print("%49s" % ("current options" + color.ENDC))
         print("%58s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
         print("%48s" % ("(1) choose a new name."))
         print("%41s" % ("(5) main menu.\n"))

         
         while True:
           NameChoice = input(color.BLEU + "name > " + color.ENDC)

           if NameChoice == "1":                    
             print(color.DARKYELLOW + "enter the new name of the ap..." + color.ENDC)
             ssid = input(color.BLEU + "name > " + color.DARKROUGE + "new name > " + color.ENDC)
             print (color.VERT + "[+]" + color.ENDC + " changing the name for " + color.VERT + "'" + ssid + "'" + color.ENDC)
             time.sleep(1)
             return ssid

           elif NameChoice == "5":          
             print(color.VERT + "[+]" + color.ENDC + " going back to main menu.")
             time.sleep(0.3)
             return ssid

           else:           
             print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid option!")
             
      
    
    #taking the crypt variable object to check if an encryption have been chosen. If not
    #the user is ask to choose an encryption type. The PassHandle function will be called
    #to verify if the password respect the security exigence
      
    
    def PassordMenu(crypt, password):
      while True:
         if crypt != "N/A":          
            print("")
            print("%48s" % ("current options" + color.ENDC))
            print("%56s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
            print("%48s" % ("(1) choose new password."))
            print("%39s" % ("(5) main menu.\n"))
            
            while True:
              PasswordChoice = input(color.BLEU + "password > " + color.ENDC)
            
              if PasswordChoice == "1":
                 print(color.DARKYELLOW + "enter the new password for the ap..." + color.ENDC)
               
                 error = False
                 while error == False:
                    password = input(color.BLEU + "password > " + color.DARKROUGE + "new password > " + color.ENDC)
                    error = Sub_Menu.PassHandle(crypt, password)               

               
                 print (color.VERT + "[+]" + color.ENDC + " changing the password to " + color.VERT + "'" + password + "'" + color.ENDC)
                 time.sleep(1)
                 return password
            
              elif PasswordChoice == "5":
                 print(color.VERT + "[+]" + color.ENDC + " going back to main menu.")
                 time.sleep(0.3)
                 return password
            
              else:
                 print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid option!")
                 

         else:
            print(color.ROUGE + "[*]" + color.ENDC + " please select a security type if you want to choose a password.")
            time.sleep(1.5)
            return password   
    
    
    #take the security type and password in parameter. If a new password is chosen the old
    #password gonna be reset to zero.    

    
    def securityMenu(crypt, password):
      while True:
         security_text = color.BLEU + color.BOLD + """   
 -WPA2 """ + color.ENDC + """is the most advanced wifi security protocol curently used by most
       router by default. The passphrase must have a minimum of 8 character.""" + color.BLEU + color.BOLD + """\n
 -WPA""" + color.ENDC + """  wpa is older and less secure than wpa2. it is using an older 
       encryption (TKIP). Like wpa2 you need to put at least 8 charactere.  """ + color.BLEU + color.BOLD + """\n
 -WEP""" + color.ENDC + """  wep is deprecated and can be very easely cracked. your wep key must
       be at least 10 charactere and only contain hexadecimal character."""
      
         print(security_text)
      
         print ("\n - the current security of the access point is " + color.VERT + "'" + crypt + "'" + color.ENDC)
         print("")
         print("%53s" % ("current options" + color.ENDC))
         print("%61s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
         print("%38s" % ("(1) WPA2."))
         print("%44s" % ("(2) WPA (TKIP)."))      
         print("%47s" % ("(3) WEP (64 bits)."))
         print("%45s" % ("(4) no security."))
         print("%44s" % ("(5) main menu.\n"))

         while True:
           NameChoice = input(color.BLEU + "security > " + color.ENDC)      
           pwd = ""

           if NameChoice == "1":        
             Sec = "WPA2"
             crypt, password = Sub_Menu.AskPassword(Sec, pwd)
             return crypt, password  
                   
           elif NameChoice == "2":         
             Sec = "WPA"
             crypt, password = Sub_Menu.AskPassword(Sec, pwd)
             return crypt, password

           elif NameChoice == "3":
             Sec = "WEP"
             crypt, password = Sub_Menu.AskPassword(Sec, pwd)
             return crypt, password

           elif NameChoice == "4":
             print (color.VERT + "[+]" + color.ENDC + " deleting the " + color.VERT + crypt + color.ENDC + " security.")
             time.sleep(1)
             crypt = "N/A"
             password = "N/A"
             return crypt, password

           elif NameChoice == "5":
             print(color.VERT + "[+]" + color.ENDC + " going back to main menu.")
             time.sleep(0.3)
             return crypt, password
      
           else:
             print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid option!")
             

    
    #giving the option to decide if the dhcp server will be on or off. It will also 
    #give the option to change the dhcp pool adresse.


    def dhcpMenu(dhcp):
      while True:         
         #putting some information for the dhcp in variable
         couleur = color.Color_check(dhcp)
         dhcpPool = "10.0.0.10-250"
         dhcpLease = "12h"
      
         # show the appropriate option in the menu    
         if dhcp == "N/A":
            dhcpOPTION = "(1) set dhcp server to" + color.VERT + " 'on'" + color.ENDC
         else:
            dhcpOPTION = "%47s" % " (1) set dhcp server to" + color.ROUGE + " 'off'" + color.ENDC         
      
         print ("""\n the dhcp server should always be on. If the dhcp is set to 'N/A' the client
 will need to have is adresse, gateway and dns set manualy.\n""")

         print (color.BOLD + " dhcp status: " + color.ENDC + couleur + "'" + dhcp + "'" + color.ENDC)
         print (color.BOLD + " dhcp pool: " + color.ENDC + color.BLEU + dhcpPool + color.ENDC)
         print (color.BOLD + " dhcp lease: " + color.ENDC + color.BLEU + dhcpLease + color.ENDC)
         print("")
         print("%49s" % ("current options" + color.ENDC))
         print("%57s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
         print("%61s" % ( dhcpOPTION))
         print("%40s" % ("(5) main menu.\n"))
         
         while True:         
           DhcpChoice = input(color.BLEU + "dhcp > " + color.ENDC)
      
           #check the last dhcp value and take the decision to put it to on or off
           if DhcpChoice == "1":         
             if dhcp == "N/A":
                dhcp = "ON"
             else:
                dhcp = "N/A"       
         
             print (color.VERT + "[+]" + color.ENDC + " changing dhcp status to " + color.VERT + "'" + dhcp + "'" + color.ENDC)
             time.sleep(1) 
             return dhcp
      
           #if this option is chosen to go back to main menu
           elif DhcpChoice == "5":
             print(color.VERT + "[+]" + color.ENDC + " going back to main menu.")
             time.sleep(0.3)         
             return dhcp

           else:
             print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid option!")
                            
    
    
    #show the menu for chosing dns option. The dns object can be change to on or N/A.
    # I am planing to give the user the choice to put their dns redirect entry directly
    # in the program and in the config file.    
    

    def dnsMenu(dns):      

      while True:
         couleur = color.Color_check(dns)
      
         # show the appropriate option in the menu    
         if dns == "N/A":           
           dnsOPTION = "(1) set dns server to" + color.VERT + " 'on' " + color.ENDC
         else:           
           dnsOPTION =  "(1) set dns server to" + color.ROUGE + " 'off'" + color.ENDC      

         print ("""\n if dns fowarding is set to 'on' dnsmasq will start the dns server and 
 start fowarding all the request to the google dns server. When the dns 
 server is active its possible to redirect the client to the ip adresse
 of your choice """)
      
         print (color.BOLD + "\n dns status:" + color.ENDC + couleur + " '" + dns + "'" + color.ENDC)      
         print("%51s" % ("current options" + color.ENDC))
         print("%59s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
         print("%63s" % (dnsOPTION))
         print("%47s" % ("(2) redirect client."))
         print("%46s" % ("(3) cleaning entry."))
         print("%42s" % ("(5) main menu.\n"))
         
         while True:
           DnsChoice = input(color.BLEU + "dns > " + color.ENDC)

           if DnsChoice == "1":
              if dns == "N/A":
                dns = "ON"
              else:
                dns = "N/A"       
         
              print (color.VERT + "[+]" + color.ENDC + " changing dns status to " + color.VERT + "'" + dns + "'" + color.ENDC)
              time.sleep(1)
              return dns               

           if DnsChoice == "2":              
              while True:

                # read the dnsmasq.host file and print the message.
                print(Sub_Menu.dns_message)
                entry_number = read_dnsmasq_host()
              
                # give the user de choice to do a new entry.
                print(color.DARKYELLOW + "\ndo you want to write an entry in the file? (y/n)" + color.ENDC)
                choice = input(color.BLEU + "dns > " + color.ENDC)
              
                # if choice is yes, we ask the user to enter the entry withthe spicified format.
                if choice == "y":
                   error = False
                   print (color.DARKCYAN + "enter the new entry with the adresse and the domain separated only by a single")
                   print("space. Example: (192.168.1.60 www.google.com)")
                 
                   # if an error is detected in the checkup of the pattern, we stay in the loop.
                   while not error:
                     entry = input(color.BLEU + "dns > " + color.DARKROUGE + "entry > " + color.ENDC)
                     error = Entry_handeling(entry)

                else:
                   break

              break

           if DnsChoice == "3":
              
              # handle the delete of the entry.
              delete_handeling()
              break


           if DnsChoice == "5":
              print(color.VERT + "[+]" + color.ENDC + " going back to main menu.")
              time.sleep(0.3)         
              return dns

           else:
              print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid option!")
              
     
    
    #this function is allowing the user to chose the in and out interface. When the 
    #interface will be chosen it gonna allow the user to see the status. A refresh 
    #option will be included    

    def interfaceMenu(inside, outside):
      print("""\n Quick ap will use the interface that you have selected to apply the ip tables
 rules on them and make the hotspot working. The inside interface is the wifi 
 card that will be use whith hostapd for creating the hotspot. The outside
 interface will be use to share the connection with the victims. You need to
 make sure that the outside interface have an addresse if you want to share
 the Internet. \n""")
    
            
      
      while True:    
        
        #put genral status of the interface in the variables and return false if interface is down.
        addresse_in, addresse_out, check_in, check_out = command.nic_selectedStatus(inside, outside)

        #color status of the interface are put into varirables.
        color_in = color.color_checkINT(inside, check_in)
        color_out = color.color_checkINT(outside, check_out) 
      
        #show the status of the selected interface with the help of the method nic_selected
        print("%50s" % (" interface status" + color.ENDC))
        print("%59s" % (color.DARKCYAN + "=======================" + color.ENDC))
        print("\t\t\t   [" + color_in +  inside +  color.ENDC + "]" + " <-> " + addresse_in)
        print("\t\t\t   [" + color_out +  outside + color.ENDC + "]" + " <-> " + addresse_out + "\n")

        print("%50s" % ("current options" + color.ENDC))
        print("%59s" % (color.DARKCYAN + "-----------------------" + color.ENDC))
        print("%48s" % ("(1) choose interface."))
        print("%39s" % ("(2) refresh."))
        print("%41s" % ("(5) main menu."))

        #first menu choice.
        interfaceChoiceFirst = input(color.BLEU + "\nnetwork > " + color.ENDC)

        if interfaceChoiceFirst == "1":         
          
          Menu = True
          check_choice = False        
          while Menu == True:          
            
            print("%52s" % (" available interface" + color.ENDC))
            print("%59s" % (color.VERT + "=======================" + color.ENDC))
          
            #looping to all interface disponible and show their status and if they are selected 
            interface = command.nic_status(inside, outside)

            print("")
            print("%51s" % ("current options" + color.ENDC))
            print("%59s" % (color.VERT + "-----------------------" + color.ENDC))
            print("%49s" % ("(1) choose inside nic."))
            print("%50s" % ("(2) choose outside nic."))
            print("%48s" % ("(3) deselect all nic."))
            print("%39s" % ("(4) refresh."))
            print("%41s" % ("(5) main menu."))

            interfaceChoice = input(color.BLEU + "\nnetwork > " + color.ENDC + color.DARKROUGE + "nic > " + color.ENDC)
                   
           

           
            if interfaceChoice == "1":

              print(color.DARKYELLOW + "enter the name of the inside interface that you want to select..." + color.ENDC)
              insideChoice = input(color.BLEU + "network > " + color.ENDC + color.DARKROUGE + "inside > " + color.ENDC)
             
              #checking in the list of interface to see if the interface is in the choice
              interface_check = command.choice_check(insideChoice, interface)
             
              #make sure that the interface selected is not the same has the outside interface.
              duplicate = command.nic_duplicate("inside", insideChoice, "", inside, outside)
             
              # if the duplicate is detected the statement continu make the program skip the conditions
              # and go back to the start of the loop             
              if duplicate == True:
                continue

              #if interface_check return false, return the user to main menu.
              elif interface_check == False:                
                print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid interface. Press 'refresh' to scan interface again.")
                time.sleep(1.5)
                print("\n")
              
              #run sevral check to see if the choice is wireless compactible etc... If the choice is
              #not accepted the last_choice is returned by wifi check
              else:                
                last_choice_in = inside
                inside = command.wifi_check(insideChoice, last_choice_in)
          

            
            elif interfaceChoice == "2":               
               
               print(color.DARKYELLOW + "enter the name of the outside interface that you want to select..." + color.ENDC)
               outsideChoice = input(color.BLEU + "network > " + color.ENDC + color.DARKROUGE + "outside > " + color.ENDC)
             
               interface_check = command.choice_check(outsideChoice, interface)

               duplicate = command.nic_duplicate("outside", "", outsideChoice, inside, outside)

               if duplicate == True:
                  continue

               elif interface_check == False:
                  print(color.ROUGE + "[*]" + color.ENDC + " please enter a valid interface. Press 'refresh' to scan interface again.")
                  time.sleep(1.5)
                  print("\n")

               else:
                  outside = command.out_check(outsideChoice)      
         
            elif interfaceChoice == "3":
               inside = "N/A"
               outside = "N/A"

               print(color.VERT + "[+]" + color.ENDC + " unselecting all network interface!")
               time.sleep(1)
               print("\n")

            elif interfaceChoice == "4":
               print (color.VERT + "[+] " + color.ENDC + "refreshing!")
               time.sleep(0.3)

            
            elif interfaceChoice == "5":
               print (color.VERT + "[+] " + color.ENDC + "main menu.")
               time.sleep(0.3)               
               return inside, outside

            else:
               print (color.ROUGE + "[-] " + color.ENDC + "please enter a valid option!\n")
               time.sleep(0.3)
        

       

        elif interfaceChoiceFirst == "2":
           print (color.VERT + "[+] " + color.ENDC + "refreshing!")
           time.sleep(0.3)

        elif interfaceChoiceFirst == "5":
           print (color.VERT + "[+] " + color.ENDC + "main menu")
           time.sleep(0.3)
           return inside, outside           
           
        else:
           print(color.ROUGE + "[-] " + color.ENDC + "please enter a valid choice!\n")
           time.sleep(0.3)
           
      return inside, outside
       

    
    #this function take in parameter the security type and the actual password. If the
    #wpa key or the wep key is incorrect it gonna show an error message and send true or
    #false depending on the situation

    
    def PassHandle(handleSEC, handlePASS):      
      passLenght = len(handlePASS)
      allowed = set("123456789" + "abcdef")      
      
      if handleSEC == "WPA2" or handleSEC == "WPA":
         if passLenght < 8:
            print (color.ROUGE + "[*]" + color.ENDC + " the wpa password must be at least 8 charactere!")
            return False

         else:
            return True

      elif handleSEC == "WEP":         
         if set(handlePASS) <= allowed and passLenght == 10:
            return True

         else: 
            print (color.ROUGE + "[*]" + color.ENDC + " the wep password must have 10 charactere and use HEX only")
            return False

    
    #this function take the secutiry type and password in parameter and it check with a loop
    #if the password is following the rule.
    
    
    def AskPassword(Sec, pwd):
      error = False
      print(color.DARKYELLOW + "enter the new " + Sec + " password for the ap..." + color.ENDC)          
         
      while error == False:
            pwd = input(color.BLEU + "security > " + color.DARKROUGE + Sec + " > " + color.ENDC)
            error = Sub_Menu.PassHandle(Sec, pwd)
         
      print (color.VERT + "[+]" + color.ENDC + " changing the security to " + color.VERT + "'" + Sec + "'" + color.ENDC)
      print (color.VERT + "[+]" + color.ENDC + " changing the password to " + color.VERT + "'" + pwd + "'" + color.ENDC)
      time.sleep(1)
      return Sec, pwd


     

 





                   

      

      



    



         



               