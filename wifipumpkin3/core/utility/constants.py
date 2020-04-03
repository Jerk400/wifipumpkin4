import os

"""
Description:
    This program is a module for wifi-pumpkin.py file which includes functionality
    declare constants .

Copyright:
    Copyright (C) 2015-2017 Marcos Nesster P0cl4bs Team
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

dir_of_executable = os.path.dirname(__file__)
dir_path          = os.getcwd()
user_config_dir   = os.path.expanduser("~")

# window constants
GEOMETRYH = 820
GEOMETRYW = 500

SYSTEMCOMMAND = ['ifconfig','iw','iwconfig', 'route']

MENU_STYLE = 'QListWidget::item {border-style: solid; border-width:1px; ' \
             'border-color:#3A3939;}QListWidget::item:selected {border-style:' \
             ' solid;color:#ff6600;  background-color: #3A3939; border-width:1px; border-radius: 2px; border: 1px solid #ff6600;}QListWidget ' \
             '{background-color: #302F2F; border-radius 2px; border-width:1px;border-color:#201F1F;} QListWidget:item:hover'\
'{color: #ff6600;border-radius: 2px; }'
GTKTHEME = 'Plastique'

NOTIFYSTYLE = "; ".join((
    "color: #302F2F",
    'background-color: #996633',
    "border-color: #996633",
    "border: 1dpx solid #996633",
    "padding: 5px"))


#DHCP logger connected 
CLIENTS_CONNECTED = user_config_dir + '/.config/wifipumpkin3/config/session/connected.json'

DHCPSERVERBINARY = 'core/packets/binary/dhcpserver'

PUMPKINPROXY_notify = 'the package requirement mitmproxy==0.18.2 is ' \
                      'not satisfied.'

#DNS file hosts
DNSHOSTS = user_config_dir+ '/.config/wifipumpkin3/config/app/dns_hosts.ini'

#donation button
DONATE = 'https://github.com/P0cL4bs/WiFi-Pumpkin#donation'
DONATE_TXT = 'Consider donating to support the development and maintenance of WiFi-Pumpkin. '

#settings DHCP
DHCPLEASES_PATH = '/var/lib/dhcp/dhcpd.leases'
DHCPCONF_PATH   = 'core/config/dhcpd_wp.conf'

# settings HOSTAPD
HOSTAPDCONF_PATH    = user_config_dir+ '/.config/wifipumpkin3/config/hostapd/hostapd.conf'
HOSTAPDCONF_PATH2   = user_config_dir+ '/.config/wifipumpkin3/config/hostapd/hostapd+.conf'
ALGORITMS = ('TKIP','CCMP','TKIP + CCMP')

#system configs
NETWORKMANAGER = '/etc/NetworkManager/NetworkManager.conf'
IPFORWARD      = '/proc/sys/net/ipv4/ip_forward'

# Docker settings 
DOCKERIPTABLESPATH = '/etc/iptables.ipv4.nat'
DOCKERHOSTAPDCONF_PATH = '/etc/hostapd/hostapd.conf'

#logging
LOG_PUMPKINPROXY = user_config_dir+ '/.config/wifipumpkin3/logs/ap/pumpkin_proxy.log'
LOG_PYDNSSERVER  = user_config_dir+'/.config/wifipumpkin3/logs/ap/pydns_server.log'
LOG_SNIFFKIN3    = user_config_dir+'/.config/wifipumpkin3/logs/ap/sniffkin3.log'
LOG_CAPTIVEPO    = user_config_dir+'/.config/wifipumpkin3/logs/ap/captiveportal.log'
LOG_RESPONDER3   = user_config_dir+'/.config/wifipumpkin3/logs/ap/responder3.log'
LOG_HOSTAPD      = user_config_dir+'/.config/wifipumpkin3/logs/ap/hostapd.log'
LOG_ALL          = user_config_dir+'/.config/wifipumpkin3/logs/everything.log'



#APP SETTINGS
CONFIG_INI          = user_config_dir+'/.config/wifipumpkin3/config/app/config.ini'
CONFIG_SK_INI       = user_config_dir + '/.config/wifipumpkin3/config/app/sniffkin3.ini'
CONFIG_PP_INI       = user_config_dir +'/.config/wifipumpkin3/config/app/pumpkinproxy.ini'
CONFIG_CP_INI       = user_config_dir +'/.config/wifipumpkin3/config/app/captive-portal.ini'

TEMPLATES           = 'templates/fakeupdate/Windows_Update/Settins_WinUpdate.html'
TEMPLATE_PH         = 'templates/phishing/custom/index.html'
TEMPLATE_CLONE      = 'templates/phishing/web_server/index.html'
EXTRACT_TEMP        = 'cd templates/ && tar -xf fakeupdate.tar.gz'
LCOMMITS            = 'https://raw.githubusercontent.com/P0cL4bs/WiFi-Pumpkin/master/Core/config/commits/Lcommits.cfg'
SOURCE_URL          = 'https://github.com/P0cL4bs/WiFi-Pumpkin.git'



#settings template
TEMPLATES_FLASK     = user_config_dir+ '/.config/wifipumpkin3/config/'
TEMP_CUSTOM = dir_path+'/templates/phishing/custom'
TEMP_Win    = dir_path+'/templates/fakeupdate/Windows_Update'
TEMP_Java   = dir_path+'/templates/fakeupdate/Java_Update'

#plugins path
RESPONDER_EXEC  = 'plugins/external/Responder/Responder.py'
DNS2PROXY_EXEC  = 'plugins/external/dns2proxy/dns2proxy.py'
BDFPROXY_EXEC   = 'plugins/external/BDFProxy-ng/bdf_proxy.py'

#colors
YELLOW = '\033[33m'
RED = '\033[91m'
ENDC = '\033[0m'