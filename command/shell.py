import subprocess
from menu.ncolor import *
import re 
import time
from write.misc import *



class command():   



    def nic_status(inside, outside):
        #finding all the interface with ifconfig. The result is converted to a list named interface.
        interface = subprocess.check_output(["ifconfig | grep 'mtu' | awk '{ print $1}'"], shell = True)
        interface = interface.decode().split()         
        
        #reading the list with the loop and show the ip adresse of each interface by using grep and awk
        #for each interface in ifconfig.
        for nic in (interface):         
            nic_strip = nic.replace(":", "")
            add = subprocess.check_output(["ifconfig " + nic_strip + " | grep -w 'inet' | awk '{ print $2}'"], shell = True)
            addresse = add.decode().replace("\n", "")            
            
            #check the string if empty! when false entering condition and adding "no ip"
            if not addresse:
                addresse = color.ROUGE + "no ip" + color.ENDC

            #checking if the definitive choice is matching one of the entry in the list. If yes
            #we print (in) to tell that this interface was chosen.
            if inside == nic_strip:
                in_chosen = color.DARKGREY + " (in)" + color.ENDC
            
            elif outside == nic_strip:
                in_chosen = color.DARKGREY + " (out)" + color.ENDC
            
            else:
                in_chosen = ""                 
            
            #showing the output with interfaces chosens in the loop.
            print ("\t\t\t   [" + color.BLEU + nic_strip + color.ENDC + "]" " <-> " + addresse + in_chosen)
        return interface                
   



    def choice_check(choice, interface):
        #check the adresse list to see if the user choice is in the list
        result = ""
        choice += ":"
        for check in (interface):
            if choice == check:
                result = True
        
        # if not in the list return false
        if result == "":
            result = False
        return result   
   



    def wifi_check(choice, last_choice):
        
        #check to see if the card have a wireless extenssion. If true is returned from the list, the card support wifi.
        card = True
        try:
            wifiByte = subprocess.check_call(['iwconfig', choice], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            print (color.VERT + "[+] " + color.ENDC + "valid wireless card.")
            time.sleep(0.3)
        
        #if iw config return an error code the program will refuse to let the user choose this interface. the variable "card"
        #will be put the false to prevent entering in the reste of the method.
        except subprocess.CalledProcessError:
            print (color.ROUGE + "[*] " + color.ENDC + "the card is not wireless compactible please choose a valid card!")
            time.sleep(2)
            print ("\n")            
            card = False
            return last_choice
        
        if card == True:
            try:
                wifiMode = subprocess.check_output("iw list | grep -A 9 'Supported interface'", shell = True)
                wifiMode_split = wifiMode.decode().split()
                output = "AP" in wifiMode_split
               
                #checking the output of iw list to check if the interface can be put in ap mode. depending
                #if output is true or not the script will tell if the interface is compactible with ap mode.
                #we return the choice even if the interface is not able to go in ap mode.
                if output == True:                    
                    print (color.BLEU + "[*] " + color.ENDC + "the interface seem to be capable of 'ap' mode.\n")
                    time.sleep(0.3)
                    return choice
                else:
                    print (color.BLEU + "[" + color.ROUGE + "-" + color.ENDC + color.BLEU + "]" + color.ENDC + "the interface might not be able to switch to ap mode\n")
                    return choice
            
            #if iw list fail the subprocess will handle the error.
            except subprocess.CalledProcessError:
               print ("not able to check if the interface can be switch to ap mode\n")



    

    def out_check(choice):
        print (color.VERT + "[+] " + color.ENDC + "the new outsides interface is '" + color.VERT + choice + color.ENDC + "'\n")
        time.sleep(0.3)
        return choice


    

    def nic_selectedStatus(inside, outside):      
       #initialising interface status check.           
       color_checkIN = True
       color_checkOUT = True

       #if the interface is not selected, "not selected" is show instead of an ip adresse. if the 
       #interface is not show to N/A the the ip adresse will be show. if their no ip adresse the empty
       #string is detected and the message "no ip" is show.

       if inside == "N/A":
          addresse_in = color.ROUGE + "not selected" + color.ENDC            

       else:
            add = subprocess.check_output(["ifconfig | grep -A 4 -w " + inside + " | grep -w 'inet' | awk '{ print $2}'"], shell = True)                                
            addresse_in = add.decode().replace("\n", "")            
            
            if not addresse_in:
                addresse_in = color.ROUGE + "no ip" + color.ENDC

       if outside == "N/A":
           addresse_out = color.r + "not selected" + color.ENDC

       else:
           out = subprocess.check_output(["ifconfig | grep -A 4 -w " + outside + " | grep -w 'inet' | awk '{ print $2}'"], shell = True)                                
           addresse_out = out.decode().replace("\n", "")

           if not addresse_out:            
               addresse_out = color.r + "no ip" + color.ENDC      
       
       
       #do a checkup in ifconfig config to see if the interface is up. If the interface is down
       #the message "down" is show. Since grep return a error code of 1 when no string is found
       #the exception is handle to see if no interface were found.      
              
       if inside != "N/A":
          try:      
             in_check = subprocess.check_call(["ifconfig | grep -q " + inside], shell = True)

          except subprocess.CalledProcessError:
             addresse_in = color.DARKGREY + "down" + color.ENDC
             color_checkIN = False
        
       if outside != "N/A":
          try:      
             out_check = subprocess.check_call(["ifconfig | grep -q " + outside], shell = True)

          except subprocess.CalledProcessError:
             addresse_out = color.DARKGREY + "down" + color.ENDC
             color_checkOUT = False         
     
       
       return addresse_in, addresse_out, color_checkIN, color_checkOUT



    def nic_duplicate(status, inside_C, outside_C, inside, outside):
        
        # if the interfaces are not equal to "N/A", the choice is comparated to the outside or
        # inside interface. If the match is true "TRUE" is returned to indicate that the interface
        # are the same. 
        
        if outside == "N/A" and inside == "N/A":
            return False

        else:            
            
            if status == "inside":
               if inside_C == outside:
                  print(color.ROUGE + "[-] " + color.ENDC + "the inside interface cant be the same has the outside interface!\n")
                  time.sleep(0.3)
                  return True

               else:
                  return False      
             
            if status == "outside":
                if outside_C == inside:
                   print(color.ROUGE + "[-] " + color.ENDC + "the outside interface cant be the same has the inside interface!\n")
                   time.sleep(0.3)
                   return True





class check_command():     
    
  
    

   


    #detect if the interface is downa nd try to bring the interface up

    def bring_interface_up(inside, outside):
       
        #adresse variable are getting the adresse, and check variable are getting the status.
        in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside)
       
        
        try:
            print (color.BLEU + "[*]" + color.ENDC + " trying to bring up the inside interface...")
            test = subprocess.check_call(['ifconfig', inside, 'up'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)            
                       
            print (color.VERT + "[+]" + color.ENDC + " the inside interface " + color.BLEU + "'" + inside + "'" + color.ENDC + " is up!")
            time.sleep(1.5)            

        #exeption if the interface is not existing
        except subprocess.CalledProcessError:
            time.sleep(1)
            print (color.ROUGE + "[-]" + color.ENDC + " quick ap is not able to bring up the inside interface. Make sure that")
            print ("    your wireless interface is connected!")
            time.sleep(2.5)
            return "only in down"

        else:                        
            return "in up"

    
    



    def bring_outside_up(inside, outside):

        #adresse variable are getting the adresse, and check variable are getting the status.
        in_ip, in_out, check_in, check_out = command.nic_selectedStatus(inside, outside)
        

        try:
            print (color.BLEU + "[*]" + color.ENDC + " trying to bring up the outside interface...")
            test = subprocess.check_call(['ifconfig', outside, 'up'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)            
                       
            print (color.VERT + "[+]" + color.ENDC + " the outside interface " + color.t + "'" + outside + "'" + color.ENDC + " is up!")
            time.sleep(1.5)            

        except subprocess.CalledProcessError:
            time.sleep(1)
            print (color.ROUGE + "[-]" + color.ENDC + " quick ap is not able to bring up the outside interface. Make sure that your")
            print ("    interface exist!")
            time.sleep(2.5)
            return "out down"

        else:
            return "out up"







class start_command():

    error = False    


    def error_message():

        error = color.rr + """\n# a problem with the internet connection from the outside interface was
  detected! It is possible that the iptable rules failed to be apply by the 
  script or the connection to the internet was not detected from the outside
  interface. Quick ap will start the wifi hotspot without internet!\n  """ + color.ENDC
        
        start_command.error = True
        print(error)
        
        time.sleep(2)


    
    
    def internet_status(net_share):
        
        if net_share == True and start_command.error == False:
          return "# internet: " + color.ENDC + color.VERT_OK + "'shared'" + color.ENDC

        else:
          return "# internet: " + color.ENDC + color.rr + "'not shared'" + color.ENDC



    

    # telling network manager to ignore the inside interface and start it back up with the new adresse.    

    def network_manager(inside, outside):      
      
        print (color.BLEU + "[*]" + color.ENDC + " telling the network manager to ignore the inside interface and change")
        print ("    the ip to" + color.VERT + " '10.0.0.1/24'" + color.ENDC + " to match the network of the wifi hotspot!")
        
        # writing in networkmanager.conf to tell network manager to ignore the inside interface. 
        net_manager_old = write_netmanager(inside, outside)
        time.sleep(1.5)
        
        # manually restarting the interface.
        try:           
           subprocess.check_call(['ifconfig', inside, "up", "10.0.0.1/24"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
           return net_manager_old
        
        except subprocess.CalledProcessError:           
           time.sleep(0.5)
           print (color.ROUGE + "[-]" + color.ENDC + " quick ap was not able to take control of " + color.BLEU + "'" + inside + "'" + color.ENDC + "!" )
           time.sleep(0.5)
           return net_manager_old        
    
  

      
      
    def ip_tables(outside):         
      
      try:
          test = subprocess.check_call(['sysctl', '-w', 'net.ipv4.ip_forward=1'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
          test = subprocess.check_call(['iptables', '-P', 'FORWARD', 'ACCEPT'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
          test = subprocess.check_call(['iptables', '-F', 'FORWARD'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
          test = subprocess.check_call(['iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o' , outside, '-j', 'MASQUERADE'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
          
          print(color.BLEU + "[*]" + color.ENDC + " activating the ipv4 forwarding and configuring the nat.")
          
      except subprocess.CalledProcessError:
          print (color.ROUGE + "[-]" + color.ENDC + " quick ap was not able sucessfuly configure the nat rule for the outside")
          print ("    interface. The internet will not be shared!")

          start_command.error = True
          
          

                                                   
          
   
    # starting the dnsmasq server (dhcp - dns).
    
    def start_dnsmasq():        
                      
            print (color.VERT + "[+]" + color.ENDC + " starting the dhcp/dns server!")
            dns = subprocess.Popen(['xterm -e "dnsmasq -C write/config/dnsmasq.conf -d"'], shell = True)

    
    # stating hotapd for starting the wireless hotspot.
   
    def start_hostapd():        
                 
            print (color.VERT + "[+]" + color.ENDC + " starting the access point!")
            subprocess.Popen(['pkill', 'wpa_supplicant'])
            wifi = subprocess.Popen(['xterm -e "hostapd write/config/hostapd.conf"'], shell = True)

        
            
    
       
    
    # killing all the process.
    
    def killing_process():

        subprocess.Popen(['pkill', 'dnsmasq'])
        subprocess.Popen(['pkill', 'hostapd'])

   

    # checking if the hostapd and the dnsmasq process are still running.
    
    def proccess_check():        
        hostapd = True
        dnsmasq = True
    
        try:
           subprocess.check_output(['pgrep', '-l', 'dnsmasq'])
    
        except subprocess.CalledProcessError:
           dnsmasq = False

        try:
           subprocess.check_output(['pgrep', '-l', 'hostapd'])

        except subprocess.CalledProcessError:
           hostapd = False   
       
        return dnsmasq, hostapd


    
    # check the if hostapd and dnsmasq are correctly from the function process check and take a decision
    # based on the status of the process.
   
    def execution_error():
        
        time.sleep(2)
        dnsmasq, hostapd = start_command.proccess_check()     
        
        if dnsmasq == True and hostapd == True:
           return True

        elif dnsmasq == False and hostapd == False:
           print (color.ROUGE + "\n[-]" + color.ENDC + " dnsmasq and hostapd were not able to start! one of the config file might")
           print ("    have been moved.")
           return False
        
        elif dnsmasq == False and hostapd == True:
           print (color.ROUGE + "\n[-]" + color.ENDC + " dnsmasq was not able to start! The config file might have been moved.")
           return False

        elif dnsmasq == True and hostapd == False:
           print (color.ROUGE + "\n[-]" + color.ENDC + " hostapd was not able to start! The config file might have been moved.")
           return False

    
     

    
    # handeling what is happening after the execution of all the mandatory program for the access point.

    def execution(net_share, ssid, encryption, attack, net_manager_old, password, dns):      
      
      # adding color to variable.      
      Ssid = color.dim + "# ssid: " + color.BLEU + "'" + ssid + "'" + color.ENDC
      Encryption = color.dim + " encryption: " + color.BLEU + "'" + encryption + "'" + color.ENDC
      Password = color.dim + " password: " + color.BLEU + "'" + password + "'" + color.ENDC
      
      # append the good color
      Ssid = color.check_notselect(Ssid, "ssid:")
      Encryption = color.check_notselect(Encryption, "encryption:")
      Password = color.check_notselect(Password, "password:")
      dns = color.check_dns(dns)
      attack = color.check_attack(attack)
      
      # checking if dnsmasq and hostapd are executed.
      exect = start_command.execution_error()

      if exect == True:      
        
        # printing choice
        print (color.DARKCYAN + "\n# quick ap is currently running! Press 'ctrl + c' to close the access point." + color.ENDC)
        print (Ssid + Encryption + Password)
        
        # checking if internet is share and print option
        share = start_command.internet_status(net_share)        
        print("")
        print(dns)
        print(share)
        print("# attack: " + attack)        
        
        time.sleep(2)

        dnsmasq = True
        hostapd = True

        # checking if dnsmasq and hostapd are still up. if someting is closed unexpectly the script will
        # get out of the loop and close the remaining process.
        try:         
         
           while dnsmasq == True and hostapd == True:
             dnsmasq, hostapd = start_command.proccess_check()

           print (color.ROUGE + "\n[-]" + color.ENDC + " !! WARNING !! " + "one of the mandatory process got kill!")
           time.sleep(1)
         
           print (color.BLEU + "[-]" + color.ENDC + " quick ap is closing all the remaining process... ")
           start_command.killing_process()
           default_netmanager(net_manager_old)           
           
           stop = input(color.DARKYELLOW + "\npress 'enter' to continue..." + color.ENDC)         
         
      
        # detect ctrl + c and close all the process working with quick ap     
        except (KeyboardInterrupt):
         
           print (color.BLEU + "\n[*]" + color.ENDC + " closing the dnsmasq and hostapd process!")
           time.sleep(1)
         
           start_command.killing_process()
           default_netmanager(net_manager_old)
           print (color.VERT + "[+]" + color.ENDC + " the access point is now close.")           
         
           stop = input(color.DARKYELLOW + "\npress 'enter' to continue..." + color.ENDC)

      
      else:
         print (color.ROUGE + "\n# quick ap was not able to start the wifi hotspot. All the remaining proccess")
         print ("  will be shut down." + color.ENDC)         
         start_command.killing_process()
         default_netmanager(net_manager_old)

         stop = input(color.DARKYELLOW + "\npress 'enter' to continue..." + color.ENDC)






    



      




         


        
   
     




        



        


        



               




            




        
        





