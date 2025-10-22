# dash2mqtt
Detect Amazon Dash button presses and publish to MQTT for Home Assistant automation


This all started with an idea for a button to turn on the garbage disposal for 5 or 10 seconds.
After finding they don't make many z-wave buttons really(there are some), it had me looking into alternatives without spending too much money.
I found a facebook marketplace post from 9 weeks ago. 24 Amazon Dash buttons for $10. The guy still had them, so here we are.

The Idea:
```
Amazon Dash button press >> ARP Announcement >> Publish to MQTT >> Home Assistant triggers a command.
```
I will be making this into a direct Home Assistant integration soon, but this is the working idea of it.


First things first, Make a firewall rule so the Amazon Dash button(s) can't reach the internet.
5 years later, and I believe they are still being bricked.

<h3>Pros and Cons to using an Amazon Dash button in 2025</h3>

| Pros | Cons | 
|------|-------|
| Cheap!|No Long presses or double presses available|
| Battery still works!|It takes about 35 seconds or so before the button can be pressed again| 


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
