# DriverAssistanceSystem
System that helps drivers that doesn't have any advanced features with one camera.

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
