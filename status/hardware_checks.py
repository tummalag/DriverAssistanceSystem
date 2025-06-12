from picamera2 import Picamera2
import subprocess
import json
import os
from hailo_platform import Device

def is_raspberry_pi() -> bool:
    try:
        with open('/sys/firmware/devicetree/base/model', 'r') as f:
            return 'raspberry pi' in f.read().lower()
    except:
        return False

def check_camera() -> bool:
    try:
        if not os.path.exists('/dev/video0'):
            print("Camera module not detected. Check if enabled in raspi-config")
            return False
            
        camera = Picamera2()
        camera_info = camera.global_camera_info()
        
        print("Detected camera(s):")
        for info in camera_info:
            print(f"  - {info.get('model', 'Unknown model')}")
            
        # Update to check for either IMX708 or IMX500
        if not any(model in str(info).lower() for info in camera_info 
                  for model in ['imx708', 'imx500']):
            print("Warning: Neither AI Camera (IMX708) nor IMX500 detected")
            return False
            
        camera.start()
        camera.stop()
        return True
    except Exception as e:
        print(f"Camera check failed: {str(e)}")
        print("Try running: sudo modprobe bcm2835-v4l2")
        return False

def check_hailo() -> bool:
    try:
        device = Device()
        print("✅ Hailo device connected")
        return True
    except Exception as e:
        print(f"❌ Hailo device not connected: {str(e)}")
        print("Ensure Hailo device is properly connected to the board")
        return False

def check_audio() -> bool:
    try:
        # First check if bluetooth service is running
        service_check = subprocess.run(['systemctl', 'is-active', 'bluetooth'],
                                     capture_output=True, text=True)
        if service_check.stdout.strip() != 'active':
            print("Warning: Bluetooth service not active")
            print("To enable, run: sudo systemctl start bluetooth")
            return True  # Not a showstopper
            
        # Print connected devices for debugging
        devices = subprocess.run(['bluetoothctl', 'devices'], 
                               capture_output=True, text=True)
        print("Available Bluetooth devices:")
        for line in devices.stdout.splitlines():
            print(f"  - {line}")
            
        result = subprocess.run(['bluetoothctl', 'info'], 
                              capture_output=True, 
                              text=True)
        
        if "Connected: yes" not in result.stdout:
            print("Warning: No Bluetooth device connected")
            return True  # Not a showstopper
        if "Audio" not in result.stdout:
            print("Warning: Connected device is not an audio device")
            return True  # Not a showstopper
            
        return True
    except Exception as e:
        print(f"Warning: Bluetooth check issue: {str(e)}")
        return True  # Not a showstopper
