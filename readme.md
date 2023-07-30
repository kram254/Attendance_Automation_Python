# Automated Attendance System with Face Recognition 📋👤

```
Python Version
OpenCV Version
face_recognition Version
```

## Overview 📝

The Attendance System with Face Recognition is a Python project that automates the process of tracking attendance using facial recognition technology. This system is designed to provide organizations, schools, and universities with an efficient and accurate method of recording attendance, eliminating the need for manual processes.

## Features ✨

Facial Recognition: The project utilizes the power of the OpenCV and face_recognition libraries to recognize faces in real-time.

Real-time Updates: The system provides real-time updates on attendance records, ensuring accurate data.

CSV Export: Attendance data can be easily exported to CSV files for seamless data management and integration with other systems.

User-Friendly Interface: The simple Graphical User Interface (GUI) makes it easy for users to interact with the system.

## Requirements 🛠️

Python 3.8 or higher
OpenCV 4.5.3 or higher
face_recognition 1.3.0 or higher
Numpy

## Installation 🚀

### Clone the repository:

```
git clone https://github.com/your-username/attendance-system.git
```

Install the required libraries:

```
pip install opencv-python face_recognition numpy
```

### Usage 📌

Place images of individuals in the 'images' directory. Make sure each image contains only one face and is labelled with the person's name.

Run the 'attendance_system.py' script:

```
Atterndance_Automation_Python.py
```

The system will launch the webcam to capture the faces and compare them with the images in the 'images' directory.

When a recognized face is detected, the person's name will be displayed on the screen, and their attendance will be recorded in the 'Attendance.csv' file.

To stop the system, press 'Enter' or 'Return' key.

Example Directory Structure 📁

```
attendance-system/
├── images/
│   ├── person1.jpg
│   ├── person2.jpg
│   └── ...
├── attendance_system.py
├── Attendance.csv
└── README.md
```

### Contributing 🤝

Contributions are welcome! If you have any improvements, suggestions, or bug fixes, feel free to create a pull request.

### License 📜

This project is licensed under the MIT License.

### Acknowledgments 👏

Special thanks to the creators of OpenCV and face_recognition libraries for providing powerful tools to work with computer vision and facial recognition.

### Contact 📧

For any questions or inquiries, please feel free to reach out to me at markorlando45@gmail.com.

Let's automate attendance management with the power of facial recognition! 🚀👤
