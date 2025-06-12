from camera import Camera
from detector import Detector
import cv2
import signal
import sys

class VideoProcessor:
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGINT, self._signal_handler)
        
    def _signal_handler(self, sig, frame):
        print("\nStopping video processing...")
        self.running = False
        
    def run(self):
        try:
            with Camera() as cam:
                detector = Detector()
                print("Starting video processing. Press Ctrl+C to stop.")
                
                while self.running:
                    # Capture frame
                    frame = cam.get_frame()
                    if frame is None:
                        print("Error: Failed to capture frame")
                        continue
                    
                    # Process frame
                    detections = detector.process_frame(frame)
                    
                    # Print detections
                    if detections:
                        print("\nDetected objects:")
                        for det in detections:
                            print(f"- {det}")  # Format based on your model output
                            
        except Exception as e:
            print(f"Error in video processing: {str(e)}")
            
if __name__ == "__main__":
    processor = VideoProcessor()
    processor.run()
