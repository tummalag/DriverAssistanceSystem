from camera import Camera
from detector import Detector, ProcessorType
import cv2
import threading
import queue
import signal

class DualProcessingSystem:
    def __init__(self):
        self.running = True
        self.frame_queue = queue.Queue(maxsize=2)
        self.result_queues = {
            ProcessorType.IMX500_EDGE: queue.Queue(),
            ProcessorType.HAILO: queue.Queue()
        }
        signal.signal(signal.SIGINT, self._signal_handler)
        
    def _signal_handler(self, sig, frame):
        print("\nStopping processing...")
        self.running = False

    def camera_thread(self):
        with Camera() as cam:
            while self.running:
                frame = cam.get_frame()
                if frame is not None:
                    # Clear queue and put new frame
                    while not self.frame_queue.empty():
                        try:
                            self.frame_queue.get_nowait()
                        except queue.Empty:
                            break
                    self.frame_queue.put(frame)

    def processor_thread(self, processor_type):
        detector = Detector(processor_type)
        window_name = f"Detection - {processor_type.value}"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        
        while self.running:
            try:
                frame = self.frame_queue.get(timeout=1.0)
                output_frame, detections = detector.process_frame(frame)
                
                # Show results
                cv2.imshow(window_name, output_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    break
                    
            except queue.Empty:
                continue

    def run(self):
        try:
            # Start camera thread
            cam_thread = threading.Thread(target=self.camera_thread)
            cam_thread.start()

            # Start processor threads
            edge_thread = threading.Thread(
                target=self.processor_thread,
                args=(ProcessorType.IMX500_EDGE,)
            )
            hailo_thread = threading.Thread(
                target=self.processor_thread,
                args=(ProcessorType.HAILO,)
            )
            
            edge_thread.start()
            hailo_thread.start()

            # Wait for threads to complete
            cam_thread.join()
            edge_thread.join()
            hailo_thread.join()

        finally:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    processor = DualProcessingSystem()
    processor.run()
