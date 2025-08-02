
 🎯 FitCheck.AI

Basic Details

Team Name: AJ
Team Members

Team Lead: Annliya Viju - Adi Shankara Institute of Engineering and Technology,Kalady

Member 2: Joseph xavier- Adi Shankara Institute of Engineering and Technology,Kalady


Project Description

FitCheck.AI is your personal, brutally honest, AI-powered fashion consultant. It analyzes your outfit in real-time, providing style ratings, suggestions, and even a little bit of sass. Upload a photo, and get instant feedback on whether your "fit" is a "hit" or a "miss."

The Problem (that doesn't exist)

In an increasingly casual world, people have forgotten the art of dressing to impress. Our society is on the brink of a fashion crisis, with mismatched socks and questionable color combinations running rampant. The world needs a solution to prevent global embarrassment, one outfit at a time.

The Solution (that nobody asked for)

FitCheck.AI provides a highly sophisticated, AI-driven platform to judge your sartorial choices. Using advanced computer vision and a database of fashion no-nos, it will give you a style rating from 1 to 10 (with 10 being "you're a style icon" and 1 being "did you get dressed in the dark?"). It also offers constructive, albeit sometimes snarky, suggestions for improvement.

Technical Details

Technologies/Components Used

For Software:

Languages used: Python, JavaScript

Frameworks used: Flask (for backend API), React.js (for frontend)

Libraries used: OpenCV, TensorFlow (or PyTorch), PIL (Pillow), Tailwind CSS

Tools used: VS Code, Git, Docker

For Hardware:

List main components: Raspberry Pi 4, Pi Camera Module v2

List specifications: Raspberry Pi 4 (4GB RAM model), Camera Module (8MP sensor)

List tools required: Micro-SD card, power supply, basic soldering kit (for optional custom casing)

Implementation

For Software:

Installation

Bash

# Clone the repository
git clone https://github.com/[your_github_username]/FitCheck.AI.git
cd FitCheck.AI

# Set up the backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up the frontend
cd frontend
npm install
Run

Bash

# Run the backend server
cd ../
python app.py

# In a new terminal, run the frontend server
cd frontend
npm start
Project Documentation

For Software:

Screenshots

Caption: The main dashboard where users can upload an image or activate the webcam.

Caption: A demonstration of the AI's feedback, showing a "miss" outfit with suggestions.

Caption: A "hit" outfit receives praise from our virtual fashion consultant.

Diagrams

Caption: This diagram illustrates the project's workflow, from image input to AI analysis and feedback output.

For Hardware:

Schematic & Circuit

Caption: A simple circuit diagram showing the connection of the Raspberry Pi Camera Module to the Pi's CSI port.

Caption: The schematic shows the pinout and connections for the camera and power supply.

Build Photos

List of components: Raspberry Pi 4, Pi Camera Module, Micro-SD Card, Power Adapter.

Explanation: Photos of the build process, including attaching the camera ribbon cable and flashing the OS on the Micro-SD card.

Explanation: The final product—a Raspberry Pi with the camera module, ready to be mounted in a custom-built enclosure (a shoebox, for dramatic effect).

Project Demo

Video


Team Contributions

Annliya Viju: Developed the backend API with Flask, implemented the machine learning models for image analysis, and handled database integration.

Joseph Xavier: Designed and built the frontend user interface using React.js and Tailwind CSS, and created the project documentation.
