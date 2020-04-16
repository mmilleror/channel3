# channel3
All credit to original concept and program creator probnot. Their source can be found at: https://github.com/probnot/wpg-weatherchan 

Modifications made to work with weather.gov, RSS news feeds, added background music, addressed some timing issues, resized to work with Raspberry Pi 7" display

Simulates Channel 3 Teletext found on most US based cable systems in the 80s and 90s

Runs with Python3

If modules missing, install with pip3 install [module name]

Download VCR OSD MONO TTF and extract to /usr/local/share/fonts/

----------

Edit setup.py as follows:

-----

weatherObservationURL - Change your observation office code - ENTER THE CODE FOR YOUR FORECASTING OFFICE

VISIT https://forecast.weather.gov and search for your ZIP CODE. Look for "CURRENT CONDITIONS AT <Name of Location> (NNNN)" The code is in the parentheses. Change PHHI.xml to your CODE.xml. 

-----

ObsUrl - Change the lat= and lon= to your lat & long

Go to https://www.latlong.net/ and enter your address as 123 Main St, Anytown, KS and click find. Be sure to enter your Lat and Long correctly.

-----

WeatherAlertCode

Visit https://alerts.weather.gov/. Scroll down and select your state and click County List. Change the WeatherAlertCode to your six digit county code.

-----

News Feeds - Copy the URL of the RSS feed and include the comma after every entry. Some feeds may not work with the program.

-----

excludeList

This is a list of words that the program will check are in the RSS news feeds and exclude those results from appearing. Add a "word" followed by a comma on each line.

-----

SET loadMuisc = 1 to turn on background music. ADD LIST OF MP3 FILES TO playlist.lst

----------

Start by running 

$ bash start.sh
