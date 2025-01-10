from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import logging
import datetime
import pytz
import os
import toml

class CustomClockPlugin(plugins.Plugin):
    __author__ = 'dozingreen'
    __version__ = '1.0'
    __license__ = 'MIT'
    __description__ = 'clock plugin with added configurability'
     
    def on_loaded(self):
        self.date_format = self.options.get('date_format', "%m/%d/%y")
        self.orientation = self.options.get('orientation', 'vertical') 
        self.x_coord = self.options.get("x_coord", 120)
        self.y_coord = self.options.get("y_coord", 80)
        self.militarytime = self.options.get('militarytime', False) #12 hr default 
        self.timezone = self.options.get('timezone', 'UTC')  # Changes UI timezone 
        logging.info(f"Clock Plugin loaded with configurations {self.options}")

#timezone validation
        try:
            self.timezone = pytz.timezone(self.timezone)
            logging.info(f"Timezone set to {self.timezone}")
        except pytz.UnknownTimeZoneError:
            logging.error(f"Unknown timezone '{self.timezone}', using UTC.")
            self.timezone = pytz.UTC  
            
    def on_ui_setup(self, ui):
        config_path = '/etc/pwnagotchi/config.toml'
        try: 
            if os.path.exists(config_path):
                with open(config_path) as f:
                    data = toml.load(f)
                logging.info("toml configuration loaded successfully")
            else:
                logging.warning(f"Config file not found at {config_path}")
        except Exception as e:
            logging.error(f"Error loading TOML configuration: {e}")  
             
    #UI setup 
        pos = (self.x_coord, self.y_coord)
        ui.add_element('clock', LabeledValue(color=BLACK, label='', value='-/-/- -:--',
                                                 position=pos,
                                                 label_font=fonts.Small, text_font=fonts.Small))
        logging.info("Clock UI setup loaded")

    def on_ui_update(self, ui):
        now = datetime.datetime.now(self.timezone)
        time_format = "%H:%M" if self.militarytime else "%I:%M %p"
        time_rn = now.strftime(
            self.date_format + (" ✦ " if self.orientation == 'horizontal' else "\n") + time_format)
        ui.set('clock', time_rn)

