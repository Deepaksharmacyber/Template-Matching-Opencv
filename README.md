Template Matching with OpenCV

A Python project that performs template matching using OpenCV.
The system automatically detects the aspect ratio of an input image, loads the corresponding template, resizes the image to a predefined resolution, and performs template matching to locate the template inside the image.

This project demonstrates practical usage of computer vision techniques for pattern detection and screen element matching.

Features

Automatic image aspect ratio detection

Dynamic template selection based on ratio

Image resolution normalization

Template matching using OpenCV

Match confidence detection

Visual bounding box on detected template

Clean modular class-based implementation

Project Structure
template_matching_project/
│
├── main.py                 # Main script containing TemplateMatch class
├── images/                 # Input images for testing
│   └── 1720x720.png
│
├── template/               # Templates mapped by aspect ratio
│   ├── 8r5.png
│   └── 43r18.png
│
├── requirements.txt        # Python dependencies
└── README.md
How It Works

The system follows these steps:

Load the input image

Calculate the image aspect ratio

Generate a ratio code
Example:

1720x720 → ratio = 43:18 → ratio_code = 43r18

Load the corresponding template

template/43r18.png

Resize the input image according to predefined resolution mapping.

Example mapping:

43r18 → (3440, 1440)
8r5 → (800, 500)

Convert images to grayscale

Perform OpenCV template matching

cv2.matchTemplate()

If match confidence ≥ threshold (default 0.8)

Draw bounding box

Display result

Installation
1. Clone the repository
git clone https://github.com/Deepaksharmacyber/Template-Matching-Opencv.git

cd template-matching-opencv
2. Create virtual environment (recommended)
python3 -m venv venv

Activate it:

Linux / Mac

source venv/bin/activate

Windows

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

or manually

pip install opencv-python numpy
Requirements

Python 3.8+

Libraries:

opencv-python
numpy

System dependencies (Ubuntu only if GUI errors occur):

sudo apt install libgl1
sudo apt install libglib2.0-0
Usage

Run the script:

python main.py

Example:

tm = TemplateMatch()
tm.template_match("images/1720x720.png")
Output

If a template is detected:

Input Image ratio: 43:18
template ratio 43r18 found in the resolution map
Match found at: (x, y) with confidence 0.91

A window will open displaying the image with a green bounding box around the matched region.

If not detected:

No match found above the threshold.
Example

Input Image

images/1720x720.png

Template Used

template/43r18.png

Detected Result

Bounding box around matched template
Key Functions
get_ratio()

Calculates image aspect ratio.

Example:

1720x720 → 43:18
image_resolution_map()

Maps aspect ratio to a standard resolution.

get_resized_img()

Resizes the input image for consistent template matching.

match()

Performs template matching using:

cv2.matchTemplate()

Method used:

cv2.TM_CCOEFF_NORMED
Future Improvements

Multi-scale template matching

Support for multiple templates

GPU acceleration

Real-time screen detection

ORB / SIFT feature matching

CLI support

Logging system

Use Cases

Game UI detection

Screen automation

GUI testing

Visual element detection

Computer vision experiments

