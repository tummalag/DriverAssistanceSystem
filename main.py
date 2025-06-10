from status import HardwareStatus, StatusType, Component
import sys

def is_raspberry_pi() -> bool:
    """Check if the code is running on a Raspberry Pi."""
    try:
        with open('/sys/firmware/devicetree/base/model', 'r') as f:
            return 'raspberry pi' in f.read().lower()
    except:
        return False

def check_camera() -> bool:
    # TODO: Implement actual camera check
    return True

def check_hailo() -> bool:
    # TODO: Implement actual Hailo check
    return True

def check_audio() -> bool:
    # TODO: Implement actual audio check
    return True

def main():
    if not is_raspberry_pi():
        print("Error: This software can only run on Raspberry Pi hardware")
        sys.exit(1)

    hw_status = HardwareStatus()
    
    # Perform hardware checks
    checks = {
        Component.CAMERA: check_camera(),
        Component.HAILO: check_hailo(),
        Component.AUDIO: check_audio()
    }
    
    # Update status based on checks
    for component, check_passed in checks.items():
        hw_status.update_status(
            component,
            StatusType.OK if check_passed else StatusType.ERROR
        )
    
    # Print status report
    hw_status.print_status()
    
    # Print overall system status
    if hw_status.all_ok():
        print("\nAll systems ready!")
    else:
        print("\nSystem not ready - check hardware status report")

if __name__ == "__main__":
    main()
