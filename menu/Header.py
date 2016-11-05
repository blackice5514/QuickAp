from menu.ncolor import *
import random

class banner:

    #chose a color and a banner to show    
    def Show_Banner():
        Banner_choice = random.randrange(1, 3)        
        if Banner_choice == 1:

            COLOR = Random_Color()
            Header = COLOR + r""" 
                       
                       
                        
                        ____        _      __   ___        
                       / __ \__  __(_)____/ /__/   |  ____ 
                      / / / / / / / / ___/ //_/ /| | / __ \
                     / /_/ / /_/ / / /__/ ,< / ___ |/ /_/ /
                     \___\_\__,_/_/\___/_/|_/_/  |_/ .___/ 
                                                  /_/ 
   """ + color.ENDC
            print(Header)

#############################################################       
     
       
        elif Banner_choice == 3:

            COLOR = Random_Color()
            Header = COLOR + r"""               
                      


                    ___        _      _         _          
                   / _ \ _   _(_) ___| | __    / \   _ __  
                  | | | | | | | |/ __| |/ /   / _ \ | '_ \ 
                  | |_| | |_| | | (__|   <   / ___ \| |_) |
                   \__\_\\__,_|_|\___|_|\_\ /_/   \_\ .__/ 
                                                    |_|   
    """ + color.ENDC
            print(Header) 

##############################################################
       
        elif Banner_choice == 2:

            COLOR = Random_Color()
            Header = COLOR + r""" 

                       
                         
                          _____     _     _   _____     
                         |     |_ _|_|___| |_|  _  |___ 
                         |  |  | | | |  _| '_|     | . |
                         |__  _|___|_|___|_,_|__|__|  _|
                            |__|                   |_| 
    
    """ + color.ENDC
            print(Header)          



#put the color from ncolor.py in the list and chose a random one 
def Random_Color():
    color_list = [color.MAUVE, color.ROUGE, color.JAUNE, color.CYAN, color.BLEU]
    i = random.randrange(0, 4)

    return color_list[i]




      