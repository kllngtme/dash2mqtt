# Important
Make a firewall rule so the Amazon Dash button(s) can't reach the internet.
5 years later, and I believe they are still being bricked by Bezos

# Requirements
- Home Assistant
- mqtt broker
- Amazon dash button

# Getting started
This [link](https://blog.christophermullins.com/2019/12/20/rescue-your-amazon-dash-buttons/) helped figuring out how to atleast get the buttons to join a wifi network.

That being said, the first one I tried connecting was easy. I got a screen that showed the mac address and to configure my wifi and it was connected. Maybe it's a caching issue for the page but every other button just received a blank screen, so I was having issues connecting them or understanding what to do next. 

01. Put Dash Button in setup mode by holding down the button until the LED flashes blue.
  - Connect to the Amazon ConfigureMe WiFi network and visit http://192.168.0.1

02. Enter the following address in to configure your wifi. As soon as you hit enter into the address bar, the blue light on the button will go away: http://192.168.0.1/?amzn_ssid=yourwifiname&amzn_pw=yourwifipassword
When you press the button again, it should join your wifi network. 

After, you need to run the docker compose image(I have it running in the same docker compose stack with home assistant and the mqtt broker) and configure it to your liking using the mqtt info of your server and what buttons you have. From there, you can build a automation in home assistant for when the mqtt topic is triggered from pressing the button.

----------------------------------

<h2>Docker-Compose.yml:</h2>

```
services:
  dash2mqtt:
    image: kllngtme/dash2mqtt:latest
    container_name: dash2mqtt
    restart: unless-stopped
    network_mode: host
    cap_add:
      - NET_ADMIN
      - NET_RAW
    environment:
      - MQTT_BROKER=192.168.1.120   # the broker IP
      - MQTT_PORT=1883
      - MQTT_USER=myuser            # optional, left blank if no login/password
      - MQTT_PASS=mypass            # optional
      - MQTT_TOPIC=dash             # the root MQTT topic for button presses
      - BUTTON_1_NAME=greenworks
      - BUTTON_1_MAC=xx:xx:xx:xx:xx
      - BUTTON_2_NAME=snuggle
      - BUTTON_2_MAC=xx:xx:xx:xx:xx
    depends_on:
      - mqtt
      - homeassistant
```


