# server_watch
Server_watch is an appindicator script that checks for server avalibility and displays connectivity through the use of icons and labels. This script works by pinging a single packet to the active connection ip found inside the settings.ini every 7 seconds, if the ping is successful the 'active.png' icon is displayed and if unsuccessful the 'inactive.png' is displayed. Upon connection switch from the menu the 'try.png' icon is displayed as a placeholder until the next ping replaces it. 

I took these icons from icons8.com so if you wish to replace these with your ones of your own choosing feel free to do so. You just need to make sure the icon names are identical to the originals and are of '.png' type.

The menu includes an open terminal option which opens a new terminal and starts a ssh connection with the active connection using the username for that connection (command  = 'ssh user@ip')

A wake option which will send a magic packet to the mac address of the active connection using the linux 'wakeonlan' you might need to install this package for this to work correctly by doing 'sudo apt-get install wakeonlan' (command = 'wakeonlan mac')

A refresh option that will send a ping upon being clicked and will update the icon accordingly if you do not want to wait for the next ping to be sent.

![](https://user-images.githubusercontent.com/64331791/91877366-e4969e80-ec4b-11ea-8be1-bc0e90ddba91.png)

This script can handle multiple different connections and can be configured through the settings.ini file by replacing the corresponding fields. If you want to track multiple connections you can add another connection block inside the settings.ini by adding the fields and increasing the connection identifier by 1. While there is no limit to the amount of connections as they are recursively added, it can be a pain to cycle through if you have an obscene amount of connections as you will have to keep clicking 'next' in the menu until you reach the one you want.

The default connection is identified in the settings.ini by using the number that follows the fields in the connection blocks. So '0' corresponds to the connection block that has 'ip-0, mac-0, user-0, label-0' and '1' corresponds to the block that has 'ip-1, mac-1, user-1, label-1'. This can be changed if you want to display a different connection on launch other than the first one.
 
single connection
--
![](https://user-images.githubusercontent.com/64331791/91896153-6398d080-ec66-11ea-9d7c-6195700c4a76.png)

multiple connections
--
![](https://user-images.githubusercontent.com/64331791/91896074-46fc9880-ec66-11ea-85e4-580fb3568746.png)






