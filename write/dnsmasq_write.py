from menu.ncolor import *
import os
import ipaddress

############################################# config_write ################################################
#                   module containing the code to write in the dnsmasq configuration file                  #                                                                  
############################################################################################################

# constant dhcp
dhcp_config = """
dhcp-range=10.0.0.10,10.0.0.250,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1\n"""
log_dhcp = "log_dhcp"

# constant dns
dnsmasq_host = "\naddn-hosts=/etc/redirect/dnsmasq.host\n"
log_dns = "log-queries\n"
dns_server = "server=8.8.8.8\n"


#other
path = "/etc/redirect"
file_dnsmasqhost = "dnsmasq.host"
file_directory = "/etc/redirect/dnsmasq.host"


dnsmasq_host_banner = """                             [current file entry] """ + color.DARKROUGE + """
                     ********************************** """ + color.ENDC

separator = color.r + " <--> " + color.ENDC
space = "    "

# append
interface = "interface="



# this function write the config of hostapd in hostapd.conf

def dnsmasq_write(inside, dns, dhcp):
    
    file = open("write/config/dnsmasq.conf", "w")

    # append 'interface=' to the inside interface. 
    interface_w = interface + inside + "\n"

    # calling functions to get the appriopriate string to be put into configuration.
    dhcp = dhcp_write(dhcp)
    dns = dns_write(dns)

    # putting all the string into one string and writing to the configuration file.
    string = interface_w + dhcp + dns
    file.write(string)

    file.close()



# this function is looking if the dhcp is activated and return the appropritate string.

def dhcp_write(dhcp):

    if dhcp == "N/A":
        return "" # if no dhcp return empty string.

    else:
        return dhcp_config # if dhcp is on, return the global string for dhcp.



# this function is looking if the dns fowarding is activated and return the appropriate string.

def dns_write(dns):

    if dns == "N/A":
        return "" # if no dns return empty string.

    else:
        dns_config = dnsmasq_host + log_dns + dns_server        
        return dns_config # if dns is on, return the global string for dns.



######################################### DNS Redirecting ################################################



# this function is reading the output of dnsmasq.host line by line

def read_dnsmasq_host():
    number = 0    
   
    # if the file open we get out of the loop with break and we do not try to open it again. 
    while True:      
      try:
         file = open("/etc/redirect/dnsmasq.host", "r")
         break   
    
    # if exeption, creating the hostfile with file_error()
      except IOError:
         file_error()        
    
    check_dnsmasq_host() # if the file is not in the correct format we handle it.       
    
    print (dnsmasq_host_banner) 
        
    for line in file: # reading the file line by line.
        li = line.strip("\n")
            
        if not li.startswith("#") and li: # if the line do not start with # and is not empty we show it.
            number += 1
            print("\t\t " + space + color.BOLD + str(number) + color.ENDC + ". " + li.replace(" ", separator))

    if number == 0: # if number have not been incremented we show no entry.
        print (color.DARKGREY + "\t\t    No entry in the 'dnsmasq.host' file." + color.ENDC)
        return False

    return number # return the number of entry.



# this function is removing line by line all the entry of dnsmasq.host except commentary.

def delete_dnsmasq_host():
    number = 0
    entry = ""
    
    file = open("/etc/redirect/dnsmasq.host", "r")
    line = file.readlines() # put each line into one big list.

    # interating in the list and checking for line with a '#'
    for x in line:
       if x.startswith("#"):
          entry += x # adding the content of this line in the string
       
       else:
          number += 1 # number of line not commented.       

    # rewrite the file only with the commented line.
    file = open("/etc/redirect/dnsmasq.host", "w")   
    file.write(entry)
    file.close
    
    number -= 1
    return number



# check if the entry in the file are in the appropriate format.

def check_dnsmasq_host():
    
    i = 0
    space = 1
    
    bad_format = False
    yes_no = "False"

    file = open("/etc/redirect/dnsmasq.host", "r")
    line = file.readlines() # put each line into one big list.

    for x in line:        
        if not x.startswith("#"): 
            i += 1
            space = x.count(" ") # getting number of space for each line.           
               
            # if to much space is detected in a line we detect it.
            if space > 1:
                bad_format = True
                line[i] = ""
    
    if bad_format:
        file = open("/etc/redirect/dnsmasq.host", "w")
        line_string = "".join(line)
        file.write(line_string)
        
        print(color.ROUGE + "[-]" + color.ENDC + " some lines in the file were removed for not respecting the format!\n")
        file.close()               
         

# if an aception occur, quick ap is trying to create back the path and the file.

def file_error():

    print (color.BLEU + "[*]" + color.ENDC + " created the host file " + color.VERT + "'" + file_dnsmasqhost + "'" + color.ENDC + "\n")
    
    # if the path do not exits create the file and the path
    if not os.path.exists(path):
       os.makedirs(path)
       file = open(file_directory, "w")
    
    # only writing the file in the specific directory.
    else:
       file = open(file_directory, "w")



# handle the entry in the dnsmasq.host file.

def Entry_handeling(entry_string):

    yes_no = "False"
    
    # check if their is one space in the string.
    space = entry_string.count(" ")

    if space != 1:
        print(color.r + "[-]" + color.ENDC + " please follow the appropriate pattern!")        
        return False

    else:
        entry_list = entry_string.split(" ") # split when space detected.
        
        # extract the adresse and domain form the list.
        addresse = entry_list[0] 
        domaine = entry_list[1]
        
        # check if the domaine string is not empty.
        if domaine == "":
            print (color.r + "[-]" + color.ENDC + " the domain cannot be an empty string!")
            return False

        # check if the ipv4 address is valid.
        elif not Address_Check(addresse):
            print (color.r + "[-]" + color.ENDC + " please enter a valid ipv4 address!")
            return False

        else:          
            # appending the new entry in the file.
            file = open("/etc/redirect/dnsmasq.host", "a")
            entry = "\n" + addresse + " " + domaine
            
            # adding the entry.
            file.write(entry)
            file.close

            print(color.VERT + "[+]" + color.ENDC + " entry successfully added!")           
            print (color.DARKYELLOW + "do you want to add an other entry? (y/n)" + color.ENDC)
            
            while not choice(yes_no): # if choice not valid choice we stay in the loop. 
               yes_no = input(color.BLEU + "dns > " + color.ENDC)     
                                   
        # if the choice is yes, we return False to stay in the loop an ask for the entry again. 
        if yes_no == "y":
            print (color.DARKYELLOW + "enter the new entry.")
            return False

        elif yes_no == "n":                
            return True


# deleting all the entry the dnsmasq.host file.

def delete_handeling():
    
    yes_no = "False"    
    
    while True:

        # check if their at least one entry in the file.
        if not read_dnsmasq_host():        
           stop = input(color.d + "\npress enter to continue..." + color.ENDC)
           break # get out of the main loop.
    
        # we ask if the user want to erase the content of the file.
        else:   
           print (color.DARKYELLOW + "\ndo you want to delete all the entry in the dnsmasq.host file? (y/n)" + color.ENDC)
        
           while not choice(yes_no): # if choice not valid choice we stay in the loop and ask again.
              yes_no = input(color.BLEU + "dns > " + color.ENDC)

        if yes_no == "y":      
        
           # remove all the entry and return the number of line removed.
           del_line = delete_dnsmasq_host()        
           print(color.BLEU + "[*] " + color.ENDC + color.VERT + str(del_line) + color.ENDC + " entry deleted.")

        else:
           return
            


# check if the addresse is a valid ipv4 address.

def Address_Check(addresse):
    
    try:
       ipaddress.ip_address(addresse)
       return True

    except ValueError:
       return False


# check if the choice is valid.

def choice(yes_no):   
    
    if yes_no == "False": # make sure to get in the loop one time.
        return False   
    
    elif yes_no == "y" or yes_no == "n" or yes_no == "":
        return True
   
    else:
        print (color.ROUGE + "[-]" + color.ENDC + " please enter a valid choice!")
        return False












