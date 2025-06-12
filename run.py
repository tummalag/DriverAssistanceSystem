from status.hardware_checks import check_camera, check_hailo, check_audio
from video.camera import Camera
from video.detector import Detector, ProcessorType
import cv2

def print_status():
    print("\nHardware Status Report:")
    print("----------------------")
    camera_ok = check_camera()
    hailo_ok = check_hailo()
    audio_ok = check_audio()
    print("----------------------")
    return all([camera_ok, hailo_ok])

def main():
    if not print_status():
        print("Hardware check failed. Please fix issues and retry.")
        return

    print("All systems ready. Starting video streams...")
    
    # Initialize camera and detectors
    camera = Camera(width=1280, height=720)
    hailo_detector = Detector(ProcessorType.HAILO)
    edge_detector = Detector(ProcessorType.IMX500_EDGE)

    # Create windows
    cv2.namedWindow("Hailo Detection", cv2.WINDOW_NORMAL)
    cv2.namedWindow("IMX500 Edge Detection", cv2.WINDOW_NORMAL)

    try:
        camera.start()
        print("Press 'q' to quit")

        while True:
            frame = camera.get_frame()
            if frame is None:
                continue

            # Process with both detectors
            hailo_frame, _ = hailo_detector.process_frame(frame.copy())
            edge_frame, _ = edge_detector.process_frame(frame.copy())

            # Display frames
            cv2.imshow("Hailo Detection", hailo_frame)
            cv2.imshow("IMX500 Edge Detection", edge_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nStopping video streams...")
    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
