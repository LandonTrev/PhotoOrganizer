# Photo Organizing Script
This is a script I designed to automatically sort photos based on their creation date extracted from EXIF metadata. It scans a source folder containing photos and organizes them into seperate folders based on the date they were taken. It then moves the organized folders into a destination folder. As of now it is only capable of sorting .jpeg .jpg and .png file types. I plan on trying to implement compatibility with .heic .mov and .mp4 files soon along with a gui that allows you to browse for the directory or your source folder and your output folder.

# Getting Started
Follow these instructions to help you set up the script on you computer
for testing or further development.

# Prerequisites
- Python 3.x
- pip
- Pillow external library

# How to install and use
1. Start of by ensuring you have the package manager [pip] installed on your computer. (https://pip.pypa.io/en/stable/installation/)
2. Install Pillow if you havent already by running 'pip install pillow' in your preffered terminal
3. Clone the repository or download the script
  'photo-organizer.py'
4. Configure paths: Edit the 'local path' variable to specify the path to your source folder containing photos. Edit the 'destinationPath' variable to specify the path to the folder where sorted photos will be moved.

    ![carbon (3)](https://github.com/LandonTrev/PhotoOrganizer/assets/165218717/8077c013-909b-434c-bd41-b2172608e5a8)

6. Run the script by giving your terminal the command 'python photo-organizer.py' or simply double click the python file only after you've specified the paths. Make sure if using the terminal you specify the path the file is in. To do this you would run 'cd (specify the directory of .py file)' then proceed to type in the command to run it.

# Testing
I've done quite a bit of testing with this project so far. I had an issue with the paths when not using r before the path to indicate a raw string. The backslashes in the windows paths were creating errors. I fixed this up and it works like a charm. I've tested it with hundreds of photos and it finishes in a few secionds. I've also made sure to try and put mp4, mov, and heic files within to make sure it skips over the files it cannot process. This ensures the script continues running even when there are file types it doesnt recognize.

# Built With
- Python- 3.12.2
- Pillow- Python Imaging Library for image processing

# Contributing
Contributions are Welcdome! If you find any issues or have suggestions for improvments, I'm all ears. Feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the the LICENSE.md file for details

# Acknowledgements
- Props to the developers of the Pillow library for providing fast and powerful image processing capabilities.
- Inspiration from Aaron Yu in this article https://python.plainenglish.io/create-a-photo-organizer-in-1-hour-with-python-9d4b82552f21
- Along with inspiration from MadTc Tech in this video
https://www.youtube.com/watch?v=M0Pu68srZoI&t=26s

  



   

   
