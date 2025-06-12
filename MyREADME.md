# DriverAssistanceSystem
System that helps drivers that doesn't have any advanced features with one camera.

### TODO
Great! Let's **calibrate and set up everything** needed for your **Driver Assistance System using Raspberry Pi 5 + AI Camera + AI HAT+ (26 TOPS)**. Here's a structured checklist so you can go step-by-step and know exactly what needs to be calibrated or configured.

---

## ✅ **🔧 SYSTEM SETUP & CALIBRATION ROADMAP**

---

### 1. **Raspberry Pi Setup**

* [ ] ✅ Flash Raspberry Pi OS (Bookworm 64-bit recommended)
* [ ] ✅ Enable SSH, set username/password via Raspberry Pi Imager (Advanced Settings)
* [ ] ✅ Connect to Wi-Fi / Ethernet and verify IP (`ssh pi@raspberrypi.local`)
* [ ] ✅ Update your Pi:

  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

---

### 2. **AI HAT+ Setup (26 TOPS Accelerator)**

* [ ] ✅ Mount the AI HAT+ on the Raspberry Pi GPIO
* [ ] ✅ Install drivers and libraries (depending on the chip — provide model for exact commands)
* [ ] ✅ Verify hardware recognition (`lsusb`, `dmesg`, or device-specific tools)

---

### 3. **Camera Calibration**

* [ ] ✅ Connect AI camera to CSI or USB port (depends on your module)
* [ ] ✅ Install camera libraries:

  ```bash
  sudo apt install libcamera-apps
  ```
* [ ] ✅ Test camera:

  ```bash
  libcamera-still -o test.jpg
  ```
* [ ] ✅ Perform lens calibration (for AI vision):

  * Use OpenCV's camera calibration scripts (checkerboard method)
  * Store `camera_matrix` and `distortion_coeffs` for future use

---

### 4. **Audio System Setup (Bluetooth Speaker / Audio Alerts)**

* [ ] ✅ Pair and connect Bluetooth audio device:

  ```bash
  bluetoothctl
  ```

  Inside prompt:

  ```bash
  power on
  agent on
  scan on
  pair XX:XX:XX:XX:XX:XX
  trust XX:XX:XX:XX:XX:XX
  connect XX:XX:XX:XX:XX:XX
  ```
* [ ] ✅ Set audio output:

  ```bash
  sudo apt install pulseaudio pulsemixer
  ```
* [ ] ✅ Test audio:

  ```bash
  aplay /usr/share/sounds/alsa/Front_Center.wav
  ```

---

### 5. **AI Model Deployment & Calibration**

* [ ] ✅ Choose model (e.g., YOLOv5/YOLOv8, MobileNet-SSD, etc.)
* [ ] ✅ Quantize/convert model (if needed) for your AI HAT+ (provide HAT chipset details for exact tools)
* [ ] ✅ Run test inference and verify FPS
* [ ] ✅ Fine-tune thresholds, non-max suppression, and class labels

---

### 6. **Driver Assistance Features to Calibrate**

Here’s what you can implement and calibrate:

| Feature                         | Calibration Required                          |
| ------------------------------- | --------------------------------------------- |
| ✅ Lane Detection                | Camera position, angle, perspective transform |
| ✅ Traffic Sign Detection        | Dataset + AI model + bounding box thresholds  |
| ✅ Pedestrian Detection          | AI model confidence tuning                    |
| ✅ Forward Collision Warning     | Object distance estimation, camera FOV        |
| ✅ Drowsiness Detection (future) | Face landmark model, camera angle             |
| ✅ Audio Alerts                  | Sound mapping to events, volume, speaker test |

---

### 7. **Code Structure & Automation**

* [ ] ✅ Create a folder structure (`/home/pi/driver-assist/`)
* [ ] ✅ Auto-start script via `systemd` or `rc.local`
* [ ] ✅ Logs for detections, camera status, and AI events
* [ ] ✅ Test full pipeline (camera → inference → action → audio)

---

### 8. **Optional Tuning**

* [ ] Night-time image enhancement (low-light filtering)
* [ ] Object distance estimation (with monocular depth inference)
* [ ] GPS integration or inertial sensors if desired later

---

Would you like me to generate a GitHub-ready starter project or sample code for one of the features (e.g., lane detection or object detection with audio alerts)? Just say the word!



### Requirements:
- Raspberry pi 5
- Rasperry pi AI HAT+ - 26 TOPS
- Raspberry Pi AI camera
- SD Card - 64GB

### Features

🚧 1. **Lane Detection & Departure Warning**

* Detect lane markings using edge detection, perspective transforms, or deep learning.
* Alert when vehicle drifts out of lane (without using turn signals).

**Tools:** OpenCV, NumPy, CNN-based lane detection (e.g., SCNN, UltraFast)

---

🚗 2. **Forward Collision Warning (FCW)**

* Detect vehicles ahead and estimate Time-to-Collision (TTC).
* Alert if you're approaching another vehicle too fast.

**Tools:** YOLOv5 or YOLO-NAS, depth estimation (monocular)

🚦 3. **Traffic Sign Recognition**

* Detect and classify traffic signs (stop, speed limit, yield, etc.).
* Works well with pre-trained models and datasets like GTSRB.

**Tools:** CNN, MobileNet, Tiny YOLO, OpenCV classifiers

---

🚶 4. **Pedestrian Detection**

* Identify pedestrians crossing or standing on the road.
* Useful for low-speed environments (urban, parking lots).

**Tools:** YOLOv5, SSD MobileNet, Haar Cascades (simpler)

---

🚓 5. **Vehicle Detection & Tracking**

* Detect cars, trucks, bikes, buses on the road.
* Track multiple objects over time using DeepSORT, Kalman Filters.

**Tools:** YOLOv5 + DeepSORT

---

📏 6. **Distance Estimation**

* Approximate distance to detected objects using:

  * Bounding box size heuristics
  * Monocular depth estimation networks (MiDaS)

---

 🧠 7. **Driver Alerts & Logging**

* Log events (e.g., "Pedestrian ahead at 12m").
* Use sound alerts or display overlays (if you have a screen).

---

1. Define Clear Goals & Use Cases

    What core features do you want initially? (e.g., object detection, collision warning, speed sign detection)

    What hardware will be involved? (IMX500 AI Camera, Hailo AI HAT+, Raspberry Pi 5)

    How should the system notify the driver? (Bluetooth audio, CLI print, future display)

    Requirements for redundancy and fail-safe operation

2. Design a Modular Software Architecture

    Detection Layer:
    Independent modules for each AI pipeline (IMX500 AI camera pipeline & Hailo TAPPAS pipeline). Each module handles its own hardware, runs inference, and produces detection outputs.

    Fusion Layer:
    Combine detections from both pipelines — e.g., match object bounding boxes by location/time, merge confidence scores, filter duplicates.

    Notification Layer:
    Abstract interface to send alerts via Bluetooth speaker, CLI output, and potential future UI.

    Hardware Status & Health Monitor:
    Monitor each hardware unit’s connectivity and readiness; raise status flags if any module fails.

3. Plan Data Structures & Communication

    Define a common Detection Object structure with fields like:

        Object Type (e.g., pedestrian, stop sign)

        Bounding Box Coordinates

        Confidence Score

        Timestamp

        Source (AI Camera / Hailo TAPPAS)

    Communication between modules via queues or callbacks, so they remain loosely coupled.

4. Develop & Test Core Modules Independently

    Start by getting each pipeline running separately with simple output (e.g., print detected objects).

    Implement health checks for hardware readiness.

    Validate output formats and timings.

5. Implement Fusion & Notification Logic

    Fuse detection outputs from both sources, decide priority (e.g., trust Hailo if confidence > 0.7, else fallback to AI camera).

    Trigger notifications accordingly.

    Keep notification logic extensible (e.g., add display output in future).

6. Iterate & Optimize

    Profile performance (CPU, memory, latency).

    Optimize pipeline parameters or scheduling.

    Add new features step-by-step, e.g., traffic sign detection, lane detection.

7. Maintain Clear Code Structure & Version Control

    Use meaningful naming conventions (snake_case for variables/functions, PascalCase for classes, ALL_CAPS for constants).

    Document each module with README or docstrings.

    Use git branches for features and merge carefully.
