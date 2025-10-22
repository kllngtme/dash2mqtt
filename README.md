# dash2mqtt
Detect Amazon Dash button presses and publish to MQTT for Home Assistant automation

The Idea:
```
Amazon Dash button press >> ARP Announcement >> Publish to MQTT >> Home Assistant triggers a command.
```
I will be making this into a direct Home Assistant integration, but this is the working idea of it.


First things first, make a firewall rule for the Amazon Dash button(s) to not be able to reach the internet. 
5 years later, and I believe they are still being bricked.

<h2>Pros and Cons to using an Amazon Dash button in 2025</h2>

<b>Pros:</b><br>
 - Cheap!<br>
 - Battery still works!<br>

 <b>Cons:</b><br>
 - No long presses or double presses available.<br>
 - It takes about 35seconds or so before that button can be pressed again.<br>


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

# Requirements
- Home Assistant
- mqtt broker
- Amazon dash button
