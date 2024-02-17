import unittest
from KMLPipePy.operations.rtmPose2DBody import RTMPose2DBody
from KMLPipePy.operations.drawKeyPoints import DrawKeyPoints
from KMLPipePy.base_structs import CVNode, CVVariable, CVVariableConnection, CVParameter
from KMLPipePy.types import Canvas
import cv2
import logging

# python -m unittest

class TestRTMPose(unittest.TestCase):
    DO_TEST = True

    def __construct_node__(self, node, inputs : list, num_outputs : int, parameters : list):
        cv_node = CVNode(
            parameters = [
                CVParameter(name=None, label=None, dataType=None, value=x) for x in parameters
            ],
            inputs = [
                CVVariableConnection(connection=CVVariable(id = "input-" + str(x),
                                    name=None, dataType=None, value=None),
                                    id=None, dataType=None) for x in range(len(inputs))],
            outputs = [CVVariable(id = "output-" + str(x), name=None, value=None, dataType=None)
                       for x in range(num_outputs)],
            id=None, label=None, operation=None, platforms=None)
            
        vars = {}
        for i, input in enumerate(inputs):
            vars["input-" + str(i)] = input
        for i in range(num_outputs):
            vars["output-" + str(i)] = None

        res = node(cv_node, vars)
        res.initialize()

        return res

    def test_rtmpose(self):
        if not self.DO_TEST:
            return
        image = cv2.imread("./tests/test_media/testimage.jpeg")
        #image = cv2.resize(image, (400, 600))

        node = self.__construct_node__(RTMPose2DBody, [image], 1, [])
        node.execute()

        print(node.vars["output-0"])
        self.assertTrue(len(node.vars["output-0"].keypoints) > 0, node.vars["output-0"])

        canvas = Canvas(image)
        drawing_node = self.__construct_node__(DrawKeyPoints, [node.vars["output-0"], image, canvas], 0, [0.1])
        drawing_node.execute()
        canvas.show(10000)

        # for point in node.vars["output-0"].keypoints:
        #     print(point)
        #     image = cv2.circle(image, (int(point.x), int(point.y)), radius=0, color=(255, 0, 0), thickness=10)
        # cv2.imshow("Image", canvas.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    