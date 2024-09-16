import paho.mqtt.client as mqtt
import time

# MQTT broker details
broker_address = "192.168.43.7"  # Replace with your MQTT broker's address
port = 1883  # Default MQTT port

# Create an MQTT client
client = mqtt.Client()
# Callback function for when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Set the callback function for when the client connects to the broker
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port)

# Run the MQTT client loop in the background
client.loop_start()



# Function to publish a message to a topic
def publish_to_topic(topic, value):
    client.publish(topic, value,qos=2)
    print(f"Published: {value} to topic: {topic}")

# Example usage:
i = 0
while True:
    
    # topic = "greenCount"  # Replace with the desired MQTT topic
    # message = str(i)
    # publish_to_topic(topic, message)
    # topic = "redCount"  # Replace with the desired MQTT topic
    # message = str(i+2)
    # publish_to_topic(topic, message)
    client.subscribe("red_color")#subscribe
    # time.sleep(1)  # Publish a message every 5 seconds
    # i+=1
