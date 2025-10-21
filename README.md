# dash2mqtt
Detect Amazon Dash button presses and publish to MQTT for Home Assistant automation

The Idea:
```
Amazon Dash button press >> ARP Announcement >> Publish to MQTT >> Home Assistant triggers a command.
```

First things first, make a firewall rule for the Amazon Dash button(s) to not be able to reach the internet. 
5 years later, and I believe they are still being bricked.

Cons of using this button:
-No long presses or double presses available.
-It takes about 35seconds or so before that button can be pressed again.

Pros:
 -Cheap!
 -Battery still works!


