# server_watch
Server_watch is an appindicator script that checks for server avalibility and displays connectivity through the use of icons and labels. This script works by pinging a single packet to the active connection ip found inside the settings.ini every 7 seconds, if the ping is successful the 'active.png' icon is displayed and if unsuccessful the 'inactive.png' is displayed. Upon connection switch from the menu the 'try.png' icon is displayed as a placeholder until the next ping replaces it. 

I took these icons from icons8.com so if you wish to replace these with your ones of your own choosing feel free to do so. You just need to make sure the icon names are identical to the originals and are of '.png' type.

![](https://user-images.githubusercontent.com/64331791/91877366-e4969e80-ec4b-11ea-8be1-bc0e90ddba91.png)

This script can handle multiple different connections and can be configured throught the settings.ini file by replacing the corresponding fields like-so

![](https://user-images.githubusercontent.com/64331791/91896153-6398d080-ec66-11ea-9d7c-6195700c4a76.png)

If you want to track multiple connections you can add another connection block inside the settings.ini by adding the fields and increasing the connection identifier by 1. 

![](https://user-images.githubusercontent.com/64331791/91896074-46fc9880-ec66-11ea-85e4-580fb3568746.png)

There is no limit to the amount of connections as they are recursively added but can be a pain to cycle through if you have an obscene amount.





