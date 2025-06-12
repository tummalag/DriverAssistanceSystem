from hailo_platform import Device
from enum import Enum
import numpy as np
import cv2

class ProcessorType(Enum):
    IMX500_EDGE = "imx500_edge"
    HAILO = "hailo"

class Detector:
    def __init__(self, processor_type: ProcessorType, model_path="yolov5"):
        self.processor_type = processor_type
        self.model_path = model_path
        if processor_type == ProcessorType.HAILO:
            self.device = Device()
            # Initialize Hailo specific settings
            self.net = self._init_hailo_network()
        else:
            # Initialize IMX500 edge AI specific settings
            self.edge_processor = self._init_edge_processor()
            
    def _init_hailo_network(self):
        # Initialize Hailo network here
        pass
        
    def _init_edge_processor(self):
        # Initialize IMX500 edge AI processor
        # This will use the camera's built-in AI capabilities
        pass

    def process_frame(self, frame):
        try:
            # Preprocessing
            processed_frame = self._preprocess(frame)
            
            # Run detection based on processor type
            if self.processor_type == ProcessorType.HAILO:
                detections = self._hailo_detect(processed_frame)
            else:
                detections = self._edge_detect(processed_frame)
                
            # Draw detections on frame copy
            output_frame = frame.copy()
            self._draw_detections(output_frame, detections)
            
            return output_frame, detections
            
        except Exception as e:
            print(f"Detection error ({self.processor_type.value}): {str(e)}")
            return frame, []
            
    def _hailo_detect(self, frame):
        # Hailo specific detection
        pass
        
    def _edge_detect(self, frame):
        # IMX500 edge AI specific detection
        pass
        
    def _draw_detections(self, frame, detections):
        # Draw bounding boxes and labels
        for det in detections:
            # Format: (x1, y1, x2, y2, conf, class_id)
            x1, y1, x2, y2 = map(int, det[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{det[5]}: {det[4]:.2f}", 
                       (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5, (0, 255, 0), 2)
