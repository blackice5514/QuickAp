from menu.ncolor import *
import time
import subprocess

############################################## misc ##################################################
#                  module containing general function for writing into files.                        #
######################################################################################################

emp = color.DARKGREY + "unknown" + color.ENDC

# read the actual configuration of network-manager.conf and store the new interface to be ignore
# by the network manager.

def write_netmanager(inside, outside):
    
    # getting the inside interface mac adresse.
    mac_adresse = check_mac(inside, outside)    
    
    # if error while fetching the inside interface we stop the function and return "error"
    if mac_adresse == "error":
        time.sleep(0.5)
        print (color.ROUGE + "[-]" + color.ENDC + " was not able read the information on " + color.BLEU + "'" + inside + "'" + color.ENDC + "!")
        time.sleep(0.5)
        return "error"
    
    # store the mac adresse and the configuration into the non managed variable    
    non_managed = """\n[keyfile]\nunmanaged-devices=mac:""" + mac_adresse 

    try:

       # open the the network manager configuration file and put the configuration in a variable.
       file = open("/etc/NetworkManager/NetworkManager.conf", "r")
       net_manager_old = file.read() # this variable is remembering the old config.
       file.close

       # net_manager_new have the unmanaged line added.
       net_manager_new = net_manager_old + non_managed 

       file = open("/etc/NetworkManager/NetworkManager.conf", "w")
       file.write(net_manager_new)

       file.close
       return net_manager_old

    # handeling the exeption if quick ap is not capable to write in the configuration file! 
    except IOError:
       time.sleep(1)
       print (color.ROUGE + "\n#  quick was not able to have access the network manager file. The inside")
       print ("   interface will be controled by the network manager and it might cause") 
       print ("   the access point to not work!\n")       
       return "error"



# this function is only reading 

def read_default_netmanager():
    
    try:
        file = open("/etc/NetworkManager/NetworkManager.conf", "r")
        net_manager_old = file.read() # this variable is remembering the old config.
        file.close
        
        return net_manager_old

    except IOError:
        return "error"



# writing the old configuration back to network-manager.conf if no error ocured.

def default_netmanager(net_manager_old):    
    
    if net_manager_old != "error":        
        
        file = open("/etc/NetworkManager/NetworkManager.conf", "w")
        file.write(net_manager_old)
        file.close


# get mac adresse of each interface.

def get_mac(inside, outside):

  # getting the mac adresse with grep, cleaning the output with 're' and add it to new_mac.                      
  mac_in = subprocess.check_output(["ifconfig " + inside + "  | grep 'ether' | awk '{ print $2}'"], shell = True, stderr = subprocess.PIPE)
  mac_out = subprocess.check_output(["ifconfig " + inside + "  | grep 'ether' | awk '{ print $2}'"], shell = True, stderr = subprocess.PIPE)
  
  # cleaning output.
  new_mac_in = mac_in.decode().replace("\n", "") 
  new_mac_out = mac_out.decode().replace("\n", "")

  return new_mac_in, new_mac_out


# get the mac adresse of the inside interface and return an error if nothing is found.
    
def check_mac(inside, outside):
    
  # getting mac adresse of interface with getmac.                      
  mac_in, mac_out = get_mac(inside, outside)
 
  # if new_mac is empty ifconfig was not able to do is job.
  if mac_in == "":      
    return "error"           
  else:
    return mac_in


# Find the OUI and give the organisation name for a specific interface.

def OUI_search(interface):
  
  line = ""  
  
  # get the mac adresse for the interface and replacing ':' by '-'
  mac, empty = get_mac(interface, "") 
  mac_clean = mac.replace(":", "-")  
  
  # converting all lower case to upper case.  
  mac_up = mac_clean.upper()  
  OUI = mac_up[0:8]
  
  try:
    file = open("write/config/oui.txt", "r")  
  
  except IOError:
    return emp # if file error, unknown is show to the user.
  
  # each line are now in the list.
  oui_list = file.readlines()  
    
  for x in oui_list:        
    if OUI in x: # if the OUI is in the line, entry is getting the line string.
       line = x      
  
  # cleaning '\n' in the file and line taking the number of charactere in the string.
  line_clean = line.strip("\n")
  line_len = len(line_clean)
  
  # organisation start at the 18 charactere an stop at the last charactere.
  organisation = line_clean[18:line_len]
  
  # check if organisation is not empty.
  if not organisation:
    return emp 

  else:
    return color.DARKGREY + organisation + color.ENDC


# handle error in the choice  

def check_Choice(menu):     
        
  while True:                   
    choice = input(color.BLEU + menu + " > " + color.ENDC)
            
    if choice == "y" or choice == "n" or choice == "":
       return choice
    else:
       print(color.ROUGE + "[-]" + color.ENDC + " please enter a valid choice!")





  
  
  










    


