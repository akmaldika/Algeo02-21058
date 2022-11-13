# Face Recognition with Eigenface
> Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri Aplikasi Nilai Eigen dan EigenFace pada Pengenalan Wajah (Face Recognition) Semester I Tahun 2022/2023

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
- The goal of this project is to implement a web or GUI that can recognize someone's face by comparing it with similar images inside the program database/dataset. 
- The SVD were calculated without any help from libraries that could calculate eigenvalues/ eigenvectors/ svd directly. 
- Students were asked to implement what they got in class by making their own code to calculate eigenvaluses, eigenvectors, and svd.


## Technologies Used
- Python 3.11.0
- numpy 1.23.4
- OpenCV 4.6.0


## Features
List the ready features here:
- Awesome feature 1
- Awesome feature 2
- Awesome feature 3


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
Prerequirement:
1. Python:https://www.python.org/downloads/
2. Pip:https://pip.pypa.io/en/stable/installation/

Requirement:
In terminal:
  ``` powerShell
  pip install numpy
  pip install opencv-python
  ```

## Usage
Method 1:
  1. Make sure the directory on the terminal is in '.\Algeo02-21058\'
  2. Run main.py inside src folder using vscode extension

Method 2:
  1. Make sure the directory on the terminal is in '.\Algeo02-21058\'
  2. py src/main.py


## Project Status
Project is: <span style = "color : yellow" >_in progres_ </span>


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- [x] function scanning image to matrix
- [x] function calculate mean of all matrix
- [x] function calculate differenc between training image and mean
- [] function calculate value of covarian matrix
- [] function calculate eigen value and eigen vector
- [] function calculate value of Eigenface
- [] function calculate new face image

