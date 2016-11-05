from menu.ncolor import *
from write.misc import check_Choice
import time

############################################ save #################################################
#              module containing general function for handeling the save file .                   #                                                             
###################################################################################################

sign_blue = color.BLEU + "[+]" + color.ENDC

message = color.DARKYELLOW + "are you sure that you want to delete the current configuration? (y/n)."  
confirmation = sign_blue + " default configuration restored."

# write choice object to the save file.

def write_save(user):   
    
    file = open("write/config/save.txt", "w")    
    
    file.write("ssid=" + user.ssid + "\n") 
    file.write("password=" + user.password + "\n")  
    file.write("crypt=" + user.crypt + "\n")
    file.write("dhcp=" + user.dhcp + "\n")
    file.write("dns=" + user.dns + "\n")
    file.write("in_INT=" + user.in_INT + "\n")
    file.write("in_OUT=" + user.in_OUT + "\n")
    file.write("attack=" + user.attack + "\n")    


# read the saved file.

def read_save():  
    
    save_list = []  
    
    file = open("write/config/save.txt", "r")
    read = file.read()
        
    # splitting the output of the file into a list.
    string = "".join(read)    
    new_list = string.split("\n")        
    clean_list = filter(None, new_list) # remove empty entry from the list. 
    
    # iterating in the clean list and removing all input before the '=' and fill the new save list.
    for x in clean_list:       
        clean = x.split("=")
        del clean[0]
        
        # convert the clean list to a string, and add it to save list string.
        string = "".join(clean)       
        save_list.append(string)        

    file.close()    
    return save_list


# check if the save file exist.

def check_save():   
    
    try:    
        file = open("write/config/save.txt", "r")
        return True
    except IOError:
        return False

# restore quick ap to the default setting.

def restore_save(default, user):    
    
    print(message)
    
    # handle choice error.
    choice = check_Choice("menu")  
    
    if choice == "y":       
        print(confirmation)
        time.sleep(1)
        return default        
    else:
        return user 






        
        






