import os  #Imports os module for file and directory operations
from PIL import Image #Imports image module from the Pillow Library for image processing
from PIL.Exiftags import TAGS #Imports TAGS from the Exiftags module in the Pillow Library for Exif data extraction
import shutil # Imports shutil module for high-level file operations
import time #Imports the time module. For measuring execution time of the program.

#Source folder 
localPath = u' FOLDER PATH OF THE SOURCE FOLDER HERE'

#Destination Folder 
destinationPath = u'FOLDER PATH OF DESTINATION FOLDER HERE'

# Mapping Exif tag names to their respective codes for retrieval

# Global Variables to keep track of processing progress

# Function to process to process a single photo
def processphoto(photoPath):
  global
  try: 
    with Image.open(photoPath) as im: 

# Function to recursively process all files in a folder

# Main function to initiate the processing


      
# Entry point of the script


