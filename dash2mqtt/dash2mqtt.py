#!/usr/bin/env python3
import os
import time
from scapy.all import sniff, ARP
import paho.mqtt.client as mqtt

# ---------- MQTT CONFIG ----------
MQTT_BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER", "")
MQTT_PASS = os.getenv("MQTT_PASS", "")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "dash")

# ---------- BUTTON CONFIG ----------
buttons = {}
for i in range(1, 25):  # support up to 24 buttons
    name = os.getenv(f"BUTTON_{i}_NAME")
    mac = os.getenv(f"BUTTON_{i}_MAC")
    if name and mac:
        buttons[mac.lower()] = name

print(f"[dash2mqtt] Starting up...", flush=True)
print(f"[dash2mqtt] Keep on Rocking in the Free World.", flush=True)
print(f"[dash2mqtt] MQTT -> Broker: {MQTT_BROKER}, port: {MQTT_PORT}, Topic: {MQTT_TOPIC}", flush=True)
print(f"[dash2mqtt] Loaded Buttons: {buttons}", flush=True)

# ---------- MQTT CONNECTION ----------
client = mqtt.Client(protocol=mqtt.MQTTv311, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
if MQTT_USER and MQTT_PASS:
    client.username_pw_set(MQTT_USER, MQTT_PASS)

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"[dash2mqtt] ERROR connecting to MQTT Broker: {e}", flush=True)
    exit(1)

client.loop_start()

# ---------- ARP PACKET HANDLER ----------
def arp_display(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 1:  # who-has request
        mac = pkt[ARP].hwsrc.lower()
        if mac in buttons:
            topic = f"{MQTT_TOPIC}/{buttons[mac]}"
            print(f"[dash2mqtt] Button press detected: {buttons[mac]} ({mac})", flush=True)
            client.publish(topic, "pressed", qos=0, retain=False)
            print(f"[dash2mqtt] Published MQTT message to {topic}", flush=True)

print("[dash2mqtt] Listening for ARP requests...", flush=True)
sniff(prn=arp_display, filter="arp", store=0)
