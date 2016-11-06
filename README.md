# QuickAp

QuickAp is a script with the goal of letting you make a wifi hotspot quickly. It will allow you to choose different option and different
attack based on your security testing need.

## Platform

Currently the script is is being developed for `kali-linux 2.0.` Their is no guarantee that QuickAp will work in older version of kali
linux or in other distribution at the moment. More support will be added in the next version of the script.

## Installation

Clone the repository `git clone` https://github.com/blackice5514/QuickAp.git. Quick ap will need python3 to run. To check if python3
is installed on your system run the command `python3 -V`.

To lauch the script run the following command in the main directory `python3 quick_ap.py`. QuickAp will install the missing dependency automatically.

## Usage

![alt text](screenshot.PNG "Description goes here")

### Main menu

```
1) Let you choose the attack that you want to use. (attack will be added further into development.)

2) Let you choose the name of your wifi hotspot.

3) if a security have been chosen you will be able to change the password in this menu.

4) Let you choose the security protection that you want to use with the access point. (wpa/wpa2/wep)

5) Let you turn on/off the dnsmasq dhcp service if you want to use an other dhcp server.

6) Let you turn on/off the dnsmasq dns service. When dns fowarding is set to 'on' dnsmasq will be configured to 
   foward all the dns request to the google dns server (8.8.8.8). In this menu you also have the option to add a
   A record entry in the host file of dnsmasq for redirecting the client on the ip address of your choice.

7) Let you choose the interface for creating the the wifi hotspot an the interface for sharing the internet with
   the client.
   
8) Restoring the default configuration of Quick ap.

9) exiting the script and saving the configuration. (ctrl + c can also be use.)
