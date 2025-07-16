# OMR Sheet Scanner and Auto Grader

A Python-based real-time **OMR (Optical Mark Recognition) sheet scanner** that detects answers from a scanned sheet image or webcam feed, compares them to an answer key, and calculates the score. Built using OpenCV and NumPy with custom utilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-ImageProcessing-green)

---

- Detects marked answers from OMR-style sheets.
- Compares detected answers with an answer key.
- Displays result overlay with correct/incorrect markings.
- Shows live webcam feed or static image processing.
- Automatically grades and displays percentage score.

---

## Features

- Real-time webcam or static image input.
- Perspective correction and contour detection.
- Bubble detection via thresholding and pixel counting.
- Custom answer key and multi-question configuration.
- Score visualization directly on the sheet.
- Image stacking for debugging view.

---

## Project Structure

OMRScannerProject/  
├── `main.py` — Main scanner logic  
├── `utlis.py` — Helper functions (contour, reorder, answer display, etc.)  
├── `1.jpg` — Sample test sheet  
├── `FinalResult.jpg` — Optional saved result image  
├── `requirements.txt` — Project dependencies  
└── `README.md` — This documentation

---

## Tech Stack

| Library     | Purpose                            |
|-------------|------------------------------------|
| OpenCV      | Image processing, video I/O        |
| NumPy       | Array operations, matrix handling  |

---

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/OMRScannerProject.git
   cd OMRScannerProject
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scanner**  
   - Using webcam:
     ```bash
     python main.py
     ```
   - Using a static image:
     - Set `webCamFeed = False` in `main.py`
     - Place your image as `1.jpg`

---

## Configuration

| Parameter         | Purpose                                        |
|-------------------|------------------------------------------------|
| `widthImg`        | Final width of processed image (e.g., 700)     |
| `heightImg`       | Final height of processed image (e.g., 700)    |
| `questions`       | Number of questions on the sheet               |
| `choices`         | Number of choices per question                 |
| `answers`         | Python list storing the correct options        |

Example:
```python
questions = 5
choices = 5
answers = [1, 2, 0, 1, 4]  # Zero-based index of correct options
```

---

## Controls

| Key | Action                 |
|-----|------------------------|
| `s` | Save result as image   |
| `q` | Quit (if webcam shown) |

---

## requirements.txt

```txt
opencv-python
numpy
```

---

## How It Works

1. Capture input from webcam or static image.
2. Preprocess (grayscale, blur, Canny edge).
3. Detect the two largest rectangles:
   - One for questions.
   - One for score box.
4. Warp the perspective to get a top-down view.
5. Apply thresholding and split into answer boxes.
6. Count non-zero pixels to determine filled choices.
7. Compare with answer key and calculate the score.
8. Overlay results (marks, score) onto the original image.

---

## Notes

- Ensure the sheet is well-lit and flat for best accuracy.
- Bubble spacing should be uniform for pixel analysis to work.
- Score display appears in the top-right grading rectangle.

---

## Credits

- Inspired by various OpenCV contour and grading tutorials
- [OpenCV](https://opencv.org/)

---

## Feedback

Feel free to open issues, fork the repo, or suggest improvements!
