
############################################# config_write ################################################
#                   module containing the code to write in the hostapd configuration file                  #                                                                  
############################################################################################################

# append before
nic = "interface="
name = "ssid="

# append before 'wpa'
inplement = "\nwpa="
passd = "wpa_passphrase="

# append before 'wep'
wep_key = "wep_key0="

# constant
driver = "driver=nl80211\n"
channel = "channel=1\n"
wifi_type = "ieee80211n=1\n"

# constant wpa
key_manage = "wpa_key_mgmt=WPA-PSK\n"
tkip = "wpa_pairwise=TKIP\n"
ccmp = "rsn_pairwise=CCMP\n"

# constant wep
default_key = "\nwep_default_key=0\n"




# this function write the config of hostapd in hostapd.conf

def hostapd_write(ssid, in_int, security, password):

    file = open("write/config/hostapd.conf", "w")
    
    # appending the string. 
    inside_w = nic + in_int + "\n" 
    name_w = name + ssid + "\n"
    
    # puting variable into a list and converting it back to a string.
    hostapd_list = [inside_w, name_w, driver, channel, wifi_type]
    hostapd_string = "".join(hostapd_list)

    # calling functions to get the appriopriate string to be put into configuration.
    wpa_string = wpa_write(security, password)
    wep_string = wep_write(security, password)
    
    # writing the string to the file and closing it.
    file.write(hostapd_string)
    file.write(wpa_string)
    file.write(wep_string)
    
    file.close


# check the type of wpa and return the appropritate string for the security configuration.

def wpa_write(security, password):
     
    # append the password.
    pass_w = passd + password + "\n"
    
    if security == "WPA2":   
        # append the implementation.
        implement_w = inplement + "3\n"      
        
        # puting variable into a list and converting it back to a string and return it. 
        wpa2_list = [implement_w, pass_w, key_manage, tkip, ccmp]
        wpa2_string = "".join(wpa2_list)
        return wpa2_string

    elif security == "WPA":
        # append the implementation.
        implement_w = inplement + "1\n" 

        wpa2_list = [implement_w, pass_w, key_manage, tkip]
        wpa2_string = "".join(wpa2_list)
        return wpa2_string      
    
    else:
        return ""  # return an empty string is nothing is chosen


# check if the security is wep and return the appropriate string for the security configuration.

def wep_write(security, password):
    
    # return the configuration to be put in the file.
    if security == "WEP":
        return default_key + wep_key + password

    else:
        return "" # return an empty string is nothing is chosen



       


