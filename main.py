from status import HardwareStatus, StatusType, Component
from status.hardware_checks import is_raspberry_pi, check_camera, check_hailo, check_audio
import sys

def main():
    if not is_raspberry_pi():
        print("Error: This software can only run on Raspberry Pi hardware")
        sys.exit(1)

    hw_status = HardwareStatus()
    checks = {
        Component.CAMERA: check_camera,
        Component.HAILO: check_hailo,
        Component.AUDIO: check_audio
    }
    
    for component, check_func in checks.items():
        hw_status.update_status(
            component,
            StatusType.OK if check_func() else StatusType.ERROR
        )
    
    hw_status.print_status()
    print("\nAll systems ready!" if hw_status.all_ok() else 
          "\nSystem not ready - check hardware status report")

if __name__ == "__main__":
    main()
