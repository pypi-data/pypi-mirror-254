from KMLPipePy.CVNodeProcess import CVNodeProcess, DataType
from KMLPipePy.types import Keypoint2D, KPFrame
from .utils import importModule

import os
import math

class FaceMeshDetection(CVNodeProcess):
    def initialize(self):
        self.mp = importModule('mediapipe') # import mediapipe as mp
        
        BaseOptions = self.mp.tasks.BaseOptions
        FaceLandmarker = self.mp.tasks.vision.FaceLandmarker
        FaceLandmarkerOptions = self.mp.tasks.vision.FaceLandmarkerOptions
        VisionRunningMode = self.mp.tasks.vision.RunningMode

        model_path = os.path.join(os.path.dirname(__file__), "assets/face_landmarker.task")

        options = FaceLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.IMAGE,
            output_facial_transformation_matrixes = True)
    
        self.landmarker = FaceLandmarker.create_from_options(options)
    
    def execute(self):
        image = self.vars[self.cvnode.inputs[0].connection.id]

        if self.catchNoDetections(image):
            return

        mp_image = self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=image)
        predictions = self.landmarker.detect(mp_image)

        if len(predictions.face_landmarks) == 0:
            return DataType.NoDetections

        x_conv = image.shape[1]
        y_conv = image.shape[0]

        # todo: 3d keypoints, also figure out why confidence doesn't exist
        kps = [Keypoint2D(int(x_conv * p.x), int(y_conv * p.y), 1, i) for i, p in enumerate(predictions.face_landmarks[0])]

        mat = predictions.facial_transformation_matrixes[0]
        #https://stackoverflow.com/a/37558238
        yaw = math.atan2(-mat[2][0], math.sqrt(mat[2][1]**2 + mat[2][2]**2))
        pitch = math.atan2(mat[2][1], mat[2][2])
        roll = math.atan2(mat[1][0], mat[0][0])
        angle_vec = [yaw, pitch, roll]
        
        self.vars[self.cvnode.outputs[0].id] = KPFrame(kps)