# custclock
pwnagotchi clock plugin with added configurability 

## Features:
- orientation configurability like memtemp's (horizontal or vertical)
- Set x_coord and y_coord directly from config.toml 
- militarytime option for a 24 hr format  
- Set a timezone that only affects the clock displayed on the UI
- date_format configurability
  
## Installation:

```bash
sudo wget -O /usr/local/share/pwnagotchi/custom-plugins/custclock.py https://raw.githubusercontent.com/dozingreen/custclock/main/custclock.py
```
Or manually create the file in the custom-plugins directory and paste the contents of the .py file inside
```bash
sudo nano /usr/local/share/pwnagotchi/custom-plugins/custclock.py
```

Enable the plugin
```toml
main.plugins.custclock.enabled = true 
```

Restart to see changes
```bash
sudo systemctl restart pwnagotchi
```

## Example configuration:
```toml
main.plugins.custclock.enabled = true
main.plugins.custclock.orientation = "horizontal"
main.plugins.custclock.militarytime = false
main.plugins.custclock.timezone = "America/New_York"
main.plugins.custclock.date_format = "%d/%m/%y"
main.plugins.custclock.x_coord = 120
main.plugins.custclock.y_coord = 80
```

