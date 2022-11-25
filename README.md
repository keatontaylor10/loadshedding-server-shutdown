# Python Script to Shutdown Linux Servers before loadshedding

This script uses Eskom Se Push's API. (Eskom's API sucks)

To get an ESP token go here https://eskomsepush.gumroad.com/l/api
A free API key allows 50 requests per day which should be enough.

Edit the config.py file with your settings.

To find your area code according to ESP, run find_area.py (after adding your token to config.py)
and select the id.

