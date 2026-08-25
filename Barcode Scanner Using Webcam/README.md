# Barcode Scanner Using Webcam

A Python project that uses a webcam to scan product barcodes and fetch product details from the Open Food Facts API.

## Features

* Scan barcodes using a webcam
* Decode barcodes with `pyzbar`
* Fetch product information from Open Food Facts
* Display the barcode on the camera feed

## Requirements

```bash
pip install opencv-python pyzbar requests
```

For Ubuntu/Debian, install ZBar if required:

```bash
sudo apt-get install libzbar0
```

## Run

```bash
python barcode.py
```

Point the webcam at a barcode. Product details will be displayed in the terminal.

Press **`q`** to exit.

## Technologies

* Python
* OpenCV
* PyZbar
* Requests
* Open Food Facts API
