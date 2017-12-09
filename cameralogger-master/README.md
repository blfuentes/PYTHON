# Camera Logger

This is a project for testing the raspberry pi using the picamera and a pir sensor.

The pir_sensor.py file logs the data captured by the pir sensor.

Every time the pir sensor status changes the time is saved with the status
"HIGH" or "LOW" into a *.csv file,

In case the status is "HIGH" a picture is taken by the camera and saved
into the {web} directory.

# display
A 7-segment display to keep counting of number of high values has been added

http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python

http://www.produktinfo.conrad.com/datenblaetter/175000-199999/186570-da-01-en-4Digit_LED_Anzeige_7Segment_Common_K.pdf
# web part
There is also a test.php file.
It opens the loc.csv file and creates a table to show the logged data with
the pictures


# to be taken in consideration
modify filepaths in the pir_sensor.py and test.php files to adjust it to 
the specific server directory structure

