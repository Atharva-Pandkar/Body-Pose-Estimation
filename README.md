# Body Pose Estimation

A desktop application for **body pose estimation** (keypoint detection) with a simple graphical interface. It supports running pose estimation on images, pre-recorded videos, and live camera streams.

## What This Project Does

- **Image Pose Estimation** — Run keypoint/pose detection on a single image. You provide the path to an image file; the app runs the detection pipeline (using CPU by default) and shows or saves the result.
- **Ready Video Pose Estimation** — Run pose estimation on an existing video file. You provide the path to a video; processing runs (using GPU when available) and can take longer than single images.
- **Live Stream Pose Estimation** — Run pose estimation on a live camera feed. You enter a name for the output; the app uses the camera and processes the stream in real time.

The main interface is built with **Tkinter** and offers a welcome screen with a single “Click to Enter” button, then a menu to choose among the three modes. Each mode asks for the required input (image path, video path, or output name) and then launches the corresponding backend script.

## Project Structure

- **`root_File.py`** — Main entry point. Tkinter GUI and logic to switch between Image, Video, and Live Stream modes and to launch the right scripts.
- **`ats.py`** — Small utility script that prints and checks paths (e.g. `Files/Image`, `Files/Video`, `Files/Live-Stream`) used by the app.
- **`root_File.spec`** — PyInstaller spec file used to build a standalone executable from `root_File.py`.

The app expects a **`Files/`** directory with backend modules:

- `Files/Image/` — Image pose estimation (e.g. `pose.py` or compiled equivalent).
- `Files/Video/` — Pre-recorded video pose estimation (e.g. `pose_video.py`).
- `Files/Live-Stream/` — Live stream pose estimation (e.g. `pose_video.py`).

## How to Run

1. Ensure Python 3 is installed (the code references `python3`).
2. Set up the `Files/` directory and the Image, Video, and Live-Stream modules as expected by `root_File.py`.
3. From the project root, run:
   ```bash
   python root_File.py
   ```
4. Optional command-line arguments (see `root_File.py`):
   - `--device` — Device for inference (default: `cpu`).
   - `--image_file` — Default input image (default: `single.jpeg`).
   - `--call` — Which function/screen to show (e.g. `options` to open the menu directly).

To build a standalone executable (e.g. for distribution):

```bash
pyinstaller root_File.spec
```

## Requirements

- Python 3 (e.g. 3.8+).
- Tkinter (usually included with Python).
- The pose estimation backends in `Files/Image`, `Files/Video`, and `Files/Live-Stream` (and their dependencies, e.g. OpenCV, PyTorch or TensorFlow, depending on the model used).

For a full list of next steps and known gaps, see **TODO.md**.
