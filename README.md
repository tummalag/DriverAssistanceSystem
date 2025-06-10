# Driver Assistance System

A Raspberry Pi-based driver assistance system using Hailo-8 AI accelerator for real-time detection and warnings.

## Hardware Requirements

- Raspberry Pi (4 or 5)
- Hailo-8 AI Accelerator
- Camera module
- Bluetooth audio speaker

## Software Requirements

- Ubuntu 22.04 (or Hailo's Docker image on Bookworm)
- Python 3.x
- Hailo Runtime

## Project Structure

```
DriverAssistanceSystem/
├── main.py              # Main application entry point
├── status/             # Hardware status management
│   ├── __init__.py
│   └── hardware_status.py
├── README.md
└── .gitignore
```

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/DriverAssistanceSystem.git
    cd DriverAssistanceSystem
    ```

2. Set up Python environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Linux/Mac
    # or
    .\env\Scripts\activate  # On Windows
    ```

3. Install dependencies (coming soon)

## Usage

Run the hardware check:
```bash
python main.py
```

The system will verify:
- Camera connectivity
- Hailo-8 availability
- Audio device status

## Features (Planned)

- Forward Collision Warning
- Lane Departure Warning
- Speed Sign Recognition
- Pedestrian/Cyclist Detection
- Traffic Light Recognition
- Object Distance Estimation

## Development Status

Currently implementing hardware initialization and status checks. See ToDo.md for development roadmap.

driverAssist/
├── assist_app/
│   ├── __init__.py
│   ├── camera_input.py         # Handles camera capture
│   ├── object_detector.py      # Hailo inference logic
│   ├── visualizer.py           # Bounding box drawing
│   ├── utils.py                # Helper functions
│   ├── constants.py            # CONFIDENCE_THRESHOLD, etc.
│   ├── main.py                 # Entry script
│   └── README.md               # ReadMe

# Assist App – Driver Assistance Core

This directory contains modular components of a driver assistance system using Raspberry Pi 5, Hailo-8 AI HAT+, and an AI camera.

### Modules:
- `camera_input.py`: Captures video input from AI camera.
- `object_detector.py`: Runs inference on frames using Hailo-8.
- `visualizer.py`: Draws bounding boxes on detected objects.
- `utils.py`: Common helper functions.
- `constants.py`: Global constants like thresholds.
- `main.py`: Entry point to launch the basic detection loop.

### Naming Convention:
- Variables & functions: `snake_case`
- Classes: `PascalCase`
- Constants: `ALL_CAPS`

### Status:
✅ Base structure created. Object detection module WIP.
