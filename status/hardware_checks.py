from picamera2 import Picamera2
import subprocess
import json

def is_raspberry_pi() -> bool:
    try:
        with open('/sys/firmware/devicetree/base/model', 'r') as f:
            return 'raspberry pi' in f.read().lower()
    except:
        return False

def check_camera() -> bool:
    try:
        camera = Picamera2()
        camera_info = camera.global_camera_info()
        if not any('imx708' in str(info).lower() for info in camera_info):
            print("Warning: AI Camera (IMX708) not detected")
            return False
        camera.start()
        camera.stop()
        return True
    except Exception as e:
        print(f"Camera check failed: {e}")
        return False

def check_hailo() -> bool:
    try:
        result = subprocess.run(['hailort-device-query', '-f', 'json'], 
                              capture_output=True, 
                              text=True)
        if result.returncode != 0:
            return False
            
        device_info = json.loads(result.stdout)
        return bool(device_info and device_info[0].get('device_id'))
    except Exception as e:
        print(f"Hailo check failed: {e}")
        return False

def check_audio() -> bool:
    try:
        result = subprocess.run(['bluetoothctl', 'info'], 
                              capture_output=True, 
                              text=True)
        return "Connected: yes" in result.stdout and "Audio" in result.stdout
    except Exception as e:
        print(f"Bluetooth audio check failed: {e}")
        return False
