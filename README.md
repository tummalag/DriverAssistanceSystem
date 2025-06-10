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
