import appdaemon.plugins.hass.hassapi as hass

class MQTT_test(hass.Hass):

  def initialize(self):
     self.log("MQTT Test App Run")
     
     self.listen_state(self.main, "sensor.mqtt_test")
         
  def main(self, entity, attribute, old, new, kwargs):

    self.log(old)
    self.log(new)  
    # self.toggle(entity_id="switch.diode_16")