# Drowsiness-monitoring-


This repository contains a Python-based real-time drowsiness detection system that uses OpenCV and Dlib libraries to monitor eye and mouth activity through webcam video feed. The system calculates Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) to identify signs of drowsiness, such as frequent blinking or yawning.

---

## Features

- **Eye Aspect Ratio (EAR):** Detects blinking patterns to assess drowsiness.
- **Mouth Aspect Ratio (MAR):** Monitors yawning frequency to determine potential fatigue.
- **Real-time Detection:** Uses live webcam feed to detect drowsiness.
- **Visual Feedback:** Highlights face landmarks and displays EAR and MAR values on the video feed.
- **Alerts:** Displays an alert on the screen if drowsiness is detected.

---

## Installation

### Prerequisites

- Python 3.x
- Dlib library
- OpenCV library
- Scipy library

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained shape predictor model:

   - [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract and place the `.dat` file in the project directory.

---

## Usage

1. Run the script:

   ```bash
   python drowsiness_detection.py
   ```

2. Ensure the webcam is accessible and functional.

3. Press **'q'** to quit the application.

---

## Configuration

- **EAR_THRESHOLD:** Minimum EAR value to detect a blink (default: `0.25`).
- **CONSECUTIVE_FRAMES:** Number of consecutive frames below EAR threshold to detect drowsiness (default: `15`).
- **MAR_THRESHOLD:** MAR value threshold to detect yawning (default: `0.75`).

You can modify these constants in the script to adjust the sensitivity of the detection system.

---

## File Structure

```
.
├── drowsiness_detection.py   # Main script
├── shape_predictor_68_face_landmarks.dat  # Pre-trained model (download separately)
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## Dependencies

- [OpenCV](https://opencv.org/)
- [Dlib](http://dlib.net/)
- [Scipy](https://www.scipy.org/)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Output

- Displays a live webcam feed with face landmarks highlighted.
- Displays real-time EAR and MAR values on the screen.
- Alerts if drowsiness is detected ("DROWSINESS DETECTED").

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to report bugs or suggest improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- Dlib for the pre-trained shape predictor model.
- OpenCV and Scipy for providing robust image processing and numerical computation tools.

---

## Disclaimer

This project is intended for educational purposes and should not be used as a replacement for certified safety systems.

