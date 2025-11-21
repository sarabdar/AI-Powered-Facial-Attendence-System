# Face Recognition System

A Python-based face recognition system that captures images from a webcam and matches them against a database of known faces using DeepFace.

## Features

- Webcam image capture with Linux compatibility
- Face recognition against a database of known faces using DeepFace
- Simple command-line interface with visual feedback
- Support for multiple image formats (jpg, jpeg, png)
- Automatic cleanup of temporary files
- Detailed error messages and troubleshooting

## Prerequisites

- Python 3.7 or higher
- OpenCV (for webcam and image processing)
- DeepFace (for face recognition)
- A working webcam

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd face_recognition_attendence
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install opencv-python deepface
   ```

## Setting Up the Database

1. Create a `db` directory in the project folder and subdirectories for each person:
   ```bash
   mkdir -p db/person1 db/person2 db/person3
   ```
   
   **Note:** The `db` directory and its contents are excluded from version control (see `.gitignore`) to protect privacy.

2. Add reference images to the appropriate subdirectories in the `db` folder:
   - Create a subdirectory for each person (e.g., `db/john_doe/`, `db/jane_smith/`)
   - Place 1-5 clear, well-lit photos of each person in their respective subdirectory
   - Supported formats: .jpg, .jpeg, .png
   - Example structure:
     ```
     db/
     ├── john_doe/
     │   ├── john1.jpg
     │   ├── john2.jpg
     │   └── john3.jpg
     └── jane_smith/
         ├── jane1.jpg
         └── jane2.jpg
     ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The system will start your webcam. You'll see a window showing the camera feed.

3. To capture an image for recognition:
   - Position yourself in front of the camera
   - Press 'c' to capture the image
   - The system will process the image and search for a match in the database

4. The system will display:
   - The captured image briefly
   - Processing status in the console
   - Match results (if found) or a "no match" message
   - The matched image (if found)

5. To quit the application:
   - Press 'q' at any time
   - Or press Ctrl+C in the terminal

## Troubleshooting

### Common Issues

- **No webcam found**:
  - Ensure your webcam is properly connected
  - Check if another application is using the camera
  - On Linux, verify camera permissions with `ls -l /dev/video*`
  - Try a different USB port if using an external camera

- **No database found**:
  - Make sure you've created the `db` directory
  - Add reference images to the `db` directory
  - Ensure the application has read permissions for the directory

- **Recognition issues**:
  - Use clear, well-lit images in the database
  - Ensure faces are clearly visible and front-facing
  - Try with different lighting conditions

- **Performance**:
  - First run will be slower due to model loading
  - Subsequent runs should be faster
  - For better performance, consider using a GPU

## Project Structure

```
face_recognition_attendence/
├── db/                   # Directory for face database (excluded from git)
│   ├── person1/          # Subdirectory for each person (not pushed to git)
│   └── person2/          # Add your own directories as needed
├── main.py              # Main application script
├── README.md            # This file
└── .gitignore           # Excludes db/ and other large files
```

## Notes

- The system uses CPU for face recognition by default
- For better performance, you can enable GPU support by installing the appropriate CUDA drivers and TensorFlow-GPU
- The system shows TensorFlow initialization messages which are normal and can be ignored
- The `.gitignore` file excludes the `db/` directory and large model files from version control to protect privacy
- The system is compatible with Linux and other Unix-like systems

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of OpenCV and DeepFace
- Inspired by the need for simple and effective face recognition solutions
