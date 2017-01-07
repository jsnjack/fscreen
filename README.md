fscreen
===========

Makes the screen look friendly in GNOME when in need to change font size caused by different DPI of the screens

Script controls the following parameters:
 - GNOME:
   - `org.gnome.desktop.interface text-scaling-factor`
 - Firefox
   - `layout.css.devPixelsPerPx`

# Installation
 - Clone the repository
 - To simplify the script call, create a link to it:
   ```bash
   sudo ln -s /home/jsn/workspace/fscreen/fscreen.py /usr/bin/fscreen
   ```
   where `/home/jsn/workspace/fscreen` location of the cloned repository

# Usage
Specify scale factor as an integer or float value:
```bash
fscreen.py 1.4
```
