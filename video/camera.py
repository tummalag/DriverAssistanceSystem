from picamera2 import Picamera2
import numpy as np
import cv2
import time

class Camera:
    def __init__(self, width=1920, height=1080):
        self.picam = Picamera2()
        self.config = self.picam.create_video_configuration(
            main={"size": (width, height), "format": "RGB888"}
        )
        self.picam.configure(self.config)
        
    def start(self):
        self.picam.start()
        time.sleep(2)  # Warm-up time
        
    def get_frame(self):
        return self.picam.capture_array()
        
    def stop(self):
        self.picam.stop()
        
    def __enter__(self):
        self.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        
    def stream(self):
        """Stream video from camera to window"""
        try:
            print("Starting video stream. Press 'q' to exit.")
            cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
            
            while True:
                frame = self.get_frame()
                
                # Convert from RGB to BGR for OpenCV display
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                # Display the frame
                cv2.imshow("Camera Feed", frame_bgr)
                
                # Break loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            cv2.destroyAllWindows()
