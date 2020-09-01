# server_watch
Appindicator script that checks for server avalibility and displays connectivity through the use of icons and labels.

![](https://user-images.githubusercontent.com/64331791/91877366-e4969e80-ec4b-11ea-8be1-bc0e90ddba91.png)

This script can handle multiple different connections and can be configured throught the settings.ini file by replacing the corresponding fields like-so

ip-0=0.0.0.0

mac-0=ad:dd:ad:dada

user-0:mugg

label-0:server

![](https://user-images.githubusercontent.com/64331791/91878083-d2693000-ec4c-11ea-8262-51d2465547da.png)

If you want to track multiple connections you can add another connection block inside the settings.ini by adding the fields and increasing the connection identifier by 1. 

![](https://user-images.githubusercontent.com/64331791/91878518-6c30dd00-ec4d-11ea-9202-14adc399274c.png)

There is no limit to the amount of connections as they are recursively added but can be a pain to cycle through if you have an obscene amount.





