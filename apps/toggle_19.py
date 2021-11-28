import appdaemon.plugins.hass.hassapi as hass

class Toggle(hass.Hass):

  def initialize(self):
     self.log("Toggle App Run")
     
     self.listen_state(self.main, "binary_sensor.button_4", old="on", new="off")
     self.listen_state(self.esp_button, "binary_sensor.esp32_gpio_34", old="off", new="on")
     self.listen_state(self.master, "binary_sensor.button_3", old="on", new="off",duration=3)

     self.listen_state(self.brightness, "sensor.brightness")

     self.bright = True
    
  def main(self, entity, attribute, old, new, kwargs):
    self.toggle(entity_id="switch.diode_16")

  def esp_button(self, entity, attribute, old, new, kwargs):
    self.toggle(entity_id="switch.esp32_gpio_27")

  def master(self, entity, attribute, old, new, kwargs):
    self.turn_off(entity_id="switch.diode_13")
    self.turn_off(entity_id="switch.diode_16")
    # self.turn_off(entity_id="switch.esp32_led")

  def brightness(self, entity, attribute, old, new, kwargs):

    brightness_v = float(self.get_state("sensor.brightness"))
    self.log("Old:", old)
    self.log("New:", new)

    if brightness_v > 0.9:
      self.log(brightness_v)
      self.turn_on(entity_id = "switch.esp32_gpio_27")
      # self.bright = False

    elif brightness_v < 0.5:  
      self.turn_off(entity_id = "switch.esp32_gpio_27")
      # self.bright = True