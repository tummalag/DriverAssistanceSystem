from picamera2 import Picamera2
import subprocess
import json
import os

def is_raspberry_pi() -> bool:
    try:
        with open('/sys/firmware/devicetree/base/model', 'r') as f:
            return 'raspberry pi' in f.read().lower()
    except:
        return False

def check_camera() -> bool:
    # First check if camera module is enabled
    try:
        if not os.path.exists('/dev/video0'):
            print("Camera module not detected. Check if enabled in raspi-config")
            return False
            
        camera = Picamera2()
        camera_info = camera.global_camera_info()
        
        # Print detected camera info for debugging
        print("Detected camera(s):")
        for info in camera_info:
            print(f"  - {info.get('model', 'Unknown model')}")
            
        if not any('imx708' in str(info).lower() for info in camera_info):
            print("Warning: AI Camera (IMX708) not detected, but found other camera")
            
        camera.start()
        camera.stop()
        return True
    except Exception as e:
        print(f"Camera check failed: {str(e)}")
        print("Try running: sudo modprobe bcm2835-v4l2")
        return False

def check_hailo() -> bool:
    # First check if Hailo device is present
    try:
        if not os.path.exists('/dev/hailo0'):
            print("Hailo device not found in /dev/hailo0")
            print("Check if Hailo HAT is properly connected")
            return False
            
        result = subprocess.run(['hailort-device-query', '-f', 'json'], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode != 0:
            print(f"Hailo query failed with: {result.stderr}")
            return False
            
        device_info = json.loads(result.stdout)
        if not device_info:
            print("No Hailo devices found by hailort-device-query")
            return False
            
        print(f"Detected Hailo device: {device_info[0].get('device_id', 'Unknown ID')}")
        return True
    except json.JSONDecodeError:
        print("Failed to parse Hailo device info")
        return False
    except Exception as e:
        print(f"Hailo check failed: {str(e)}")
        print("Try running: sudo hailort-device-reset")
        return False

def check_audio() -> bool:
    try:
        # First check if bluetooth service is running
        service_check = subprocess.run(['systemctl', 'is-active', 'bluetooth'],
                                     capture_output=True, text=True)
        if service_check.stdout.strip() != 'active':
            print("Bluetooth service not active")
            print("Try: sudo systemctl start bluetooth")
            return False
            
        result = subprocess.run(['bluetoothctl', 'info'], 
                              capture_output=True, 
                              text=True)
                              
        # Print connected devices for debugging
        devices = subprocess.run(['bluetoothctl', 'devices'], 
                               capture_output=True, text=True)
        print("Available Bluetooth devices:")
        for line in devices.stdout.splitlines():
            print(f"  - {line}")
            
        if "Connected: yes" not in result.stdout:
            print("No Bluetooth device connected")
            return False
        if "Audio" not in result.stdout:
            print("Connected device is not an audio device")
            return False
            
        return True
    except Exception as e:
        print(f"Bluetooth check failed: {str(e)}")
        print("Try: sudo systemctl restart bluetooth")
        return False
