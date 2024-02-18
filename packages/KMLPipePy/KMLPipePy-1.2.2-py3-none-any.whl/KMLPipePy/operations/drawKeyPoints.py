from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.types import Keypoint2D, KPFrame, Canvas, Annotation
from KMLPipePy.base_structs import DataType
from numpy import ndarray

class DrawKeyPoints(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """
        self.radius = self.cvnode.parameters[0].value

    def execute(self):
        keypoints : KPFrame = self.vars[self.cvnode.inputs[0].connection.id]
        image : ndarray = self.vars[self.cvnode.inputs[1].connection.id]
        canvas : Canvas = self.vars[self.cvnode.inputs[2].connection.id]

        if self.catchNoDetections(keypoints, image, canvas):
            return

        # BGR
        COLOR = (255, 255, 255)
        LEFT = (0, 0, 255)
        RIGHT = (0, 255, 0)

        annotations = [Annotation(kp.x, kp.y, self.radius, COLOR if i == 0 else LEFT if i % 2 == 1 else RIGHT) for i, kp in enumerate(keypoints.keypoints)]
        canvas.add_annotations(annotations)