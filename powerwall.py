#!/usr/local/bin/python3

#POWERWALLIP="powerwall"                 # This is your Powerwall IP or DNS Name
#PASSWORD='3zCsW!jX*z84-U!xn6RXFV9'      # Login to the Powerwall UI and Set this password - follow the on-screen instructions
#serial TBANJ
#
import pypowerwall
import time

# Optional: Turn on Debug Mode
#pypowerwall.set_debug(True)


# get the date
date = time.localtime()
final_date = time.strftime("%m/%d/%Y", date)
#print(final_date)

# get the time
timestamp = time.localtime()
final_time = time.strftime("%H:%M")
#print (final_time)

# Credentials for your Powerwall - Customer Login Data
password='3zCsW!jX*z84-U!xn6RXFV9'
email='dominic@dmartinelli.net'
host = "powerwall"               # Address of your Powerwall Gateway
timezone = "America/Los_Angeles"  # Your local timezone
 
# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

# Some System Info
#print("Site Name: %s - Firmware: %s - DIN: %s" % (pw.site_name(), pw.version(), pw.din()))
#print("System Uptime: %s\n" % pw.uptime())

# Pull Sensor Power Data
grid = pw.grid()
solar = pw.solar()
battery = pw.battery()
home = pw.home()
power_level=pw.level()

# Display Data
#print("Battery power level: %0.0f%%" % pw.level())
#print("Combined power metrics: %r" % pw.power())
#print("")

# Display Power in kW
#print("Grid Power: %0.2fkW" % (float(grid)/1000.0))
#print("Solar Power: %0.2fkW" % (float(solar)/1000.0))
#print("Battery Power: %0.2fkW" % (float(battery)/1000.0))
#print("Home Power: %0.2fkW" % (float(home)/1000.0))
#print("")

file = open("/Users/dominic/powerwall/output.csv", "a")

#print (type(battery))
#print("Battery power level: %0.0f%%" % pw.level())
#print (power_level)
power_level_formated = '{0:.2f}'.format(power_level) # to 2 decimal places
#print (power_level_formated)

#print (battery_level)
print(final_date, final_time, power_level_formated, float(grid/1000.0), float(solar/1000.0), float(battery/1000.0), float(home/1000.0), sep=",", file=file)
#print(final_date, final_time, battery_level, float(grid/1000.0), float(solar/1000.0), float(battery/1000.0), float(home/1000.0), sep=",", file=file)
#print(final_date, final_time, float(grid/1000.0), float(solar/1000.0), float(battery/1000.0), float(home/1000.0), sep=",")
"""
if power_level_formatted > 98:
	print "(power wall above 98")
else:
	print ("powerwall less than 98")

"""
