import appdaemon.plugins.hass.hassapi as hass

class MQTT_test(hass.Hass):
# Simple class to listen to mqtt_topic from homeassistant and log
  def initialize(self):

     self.log("MQTT Test App Run")
    #Listening to "sensor.mqtt_test" topic and call self.main method when sensor state is changed. 
    #This sensor inside HA configuration.yaml
    # sensor:
    #   - platform: mqtt
    #     name: "mqtt_test"
    #     state_topic: "test"     
     self.listen_state(self.main, "sensor.mqtt_test")
         
  def main(self, entity, attribute, old, new, kwargs):
# Log old and new state
    self.log(old)
    self.log(new)