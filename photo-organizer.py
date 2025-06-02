import os  
from PIL import Image #image module from Pillow Library(Image Processing)
from PIL.Exiftags import TAGS #Imports TAGS from the Exiftags module in the Pillow Library for Exif data extraction https://pillow.readthedocs.io/en/stable/reference/ExifTags.html
import shutil # Imports shutil module for high-level file operations
import time #Imports the time module. For measuring execution time of the program.

#Source folder 
localPath = r'FOLDER PATH OF THE SOURCE FOLDER HERE'
#Destination Folder 
destinationPath = r'FOLDER PATH OF DESTINATION FOLDER HERE'

# Mapping EXIF tag names to their respective codes for easier retrieval
_TAGS_r = dict(((v, k) for k, v in TAGS.items()))

# Global variables to keep track of the processing progress
totalFiles = 0
processedPhotos = 0
notPhotos = 0

# Function to process a single photo
def processPhoto(photoPath):
    global processedPhotos, notPhotos
    try:
        with Image.open(photoPath) as im:
            # Extract EXIF data from the image
            exif_data_PIL = im._getexif()
            if exif_data_PIL is not None:
                # Check if the image has the DateTimeOriginal tag
                if _TAGS_r["DateTimeOriginal"] in exif_data_PIL:
                    # Extract the creation date of the image
                    fileDate = exif_data_PIL[_TAGS_r["DateTimeOriginal"]]
                    # Check if the date is valid and in the correct format
                    if fileDate != '' and len(fileDate) > 10:
                        # Remove colons from the date to make it suitable for folder names
                        fileDate = fileDate.replace(":", "")
                        # Extract the year and month from the date for folder naming
                        destinationFolder = fileDate[:6]
                        # Create the destination folder if it doesn't exist
                        if not os.path.isdir(os.path.join(destinationPath, destinationFolder)):
                            os.makedirs(os.path.join(destinationPath, destinationFolder))
                        # Generate the new path for the photo in the sorted folder
                        newPhotoName = os.path.join(destinationPath, destinationFolder, os.path.basename(photoPath))
                        # Move the photo to the sorted folder
                        shutil.move(photoPath, newPhotoName)
                        # Update the processed photo count
                        processedPhotos += 1
                        # Print progress message
                        print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
                else:
                    # Increment the count of photos without creation date
                    notPhotos += 1
                    # Print progress message
                    print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
            else:
                # Increment the count of photos without EXIF data
                notPhotos += 1
                # Print progress message
                print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
    except IOError:
        # Increment the count of photos that couldn't be opened
        notPhotos += 1
        # Print progress message
        print("\r%d photos processed, %d not processed" % (processedPhotos, notPhotos), end='')
    except KeyError:
        # Increment the count of photos with missing EXIF tags
        notPhotos += 1
        pass

# Function to recursively process all files in a folder
def processFolder(folderPath, countOnly):
    global totalFiles
    for file in os.listdir(folderPath):
        # Construct the full path of the file
        fileNameIn = os.path.join(folderPath, file)
        # Check if the file is a directory
        if os.path.isdir(fileNameIn):
            # Recursively process the subdirectory
            processFolder(fileNameIn, countOnly)
        else:
            # Increment the total file count
            if countOnly:
                totalFiles += 1
            else:
                # Process the file if it's an image
                if fileNameIn.lower().endswith(('.jpg', '.jpeg', '.png')):
                    processPhoto(fileNameIn)

# Main function to initiate the processing
def main():
    global processedPhotos, notPhotos, totalFiles
    # Record the start time of the processing
    tic = time.perf_counter()
    # Count the total number of files in the source folder
    processFolder(localPath, True)
    print("There are total %d files" % totalFiles)
    # Process the files in the source folder and move them to the destination folder
    processFolder(localPath, False)
    print("\nThere are %d photos processed, %d not processed" % (processedPhotos, notPhotos))
    # Record the end time of the processing
    toc = time.perf_counter()
    # Print the total time taken for processing
    print(f"Time used: {toc - tic:0.4f} seconds")

# Entry point of the script
if __name__ == "__main__":
    main()

