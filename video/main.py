from camera import Camera
from detector import Detector, ProcessorType
import cv2

def main():
    # Initialize camera and detectors
    camera = Camera(width=1280, height=720)  # Lower resolution for better performance
    hailo_detector = Detector(ProcessorType.HAILO)
    edge_detector = Detector(ProcessorType.IMX500_EDGE)

    # Create named windows
    cv2.namedWindow("Hailo Detection", cv2.WINDOW_NORMAL)
    cv2.namedWindow("IMX500 Edge Detection", cv2.WINDOW_NORMAL)

    try:
        camera.start()
        print("Starting video streams... Press 'q' to quit")

        while True:
            # Capture frame
            frame = camera.get_frame()
            if frame is None:
                print("Failed to capture frame")
                continue

            # Process with both detectors
            hailo_frame, hailo_detections = hailo_detector.process_frame(frame)
            edge_frame, edge_detections = edge_detector.process_frame(frame)

            # Show frames
            cv2.imshow("Hailo Detection", hailo_frame)
            cv2.imshow("IMX500 Edge Detection", edge_frame)

            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nStopping video streams...")
    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
