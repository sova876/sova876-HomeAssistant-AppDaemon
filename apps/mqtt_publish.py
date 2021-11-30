import appdaemon.plugins.hass.hassapi as hass
import mqttapi as mqtt


class MQTT_publish(hass.Hass, mqtt.Mqtt):
# Simple test class to listen to state chenge inside hass and publish message to mqtt
  def initialize(self):

     self.log("MQTT Publish App Run") 
     #listen to state of "binary_sensor.button_4" change from "on" to "off"
     self.listen_state(self.main, "binary_sensor.button_4", old="on", new="off")
    
  def main(self, entity, attribute, old, new, kwargs):
    # log to appdaemon
    self.log("Old:", old)
    self.log("New:", new)
    #publish message "on2off" to "hass/binary_sensor/button_4" topic
    self.mqtt_publish(topic = "hass/binary_sensor/button_4", payload = "on2off")