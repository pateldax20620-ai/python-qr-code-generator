
# Python QR Code Generator

A Python project that generates QR codes using both Command-Line Interface (CLI) and Graphical User Interface (GUI).

## Features

- Generate QR codes from text, URLs, and other data.
- CLI mode for generating QR codes through the terminal.
- GUI mode using Tkinter.
- Save QR codes as PNG images.
- Generate black and blue QR codes with a white background.

## Technologies Used

- Python
- qrcode
- Tkinter
- Pillow

## Requirements

- Python 3
- Required Python packages listed in requirements.txt

## Installation

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal and install the required package:

   ```bash
   python -m pip install -r requirements.txt
   ```

## How to Run

Run the following command in the terminal:

```bash
python qr_generator.py
```

Choose an option from the menu:

1. Enter `1` to generate a QR code using CLI.
2. Enter `2` to generate a QR code using GUI.

## Output

- CLI mode generates `cli_qr.png`.
- GUI mode generates `gui_qr.png`.

The generated QR code images are saved in the current working directory.

## Author

Created as a Python project for learning and practicing Python programming.
