import cv2
import math
from KMLPipePy.types import Keypoint2D
from KMLPipePy.base_structs import DataType
from typing import List
import base64
import importlib

def calc3PtAngle(p1 : Keypoint2D, p2: Keypoint2D, p3: Keypoint2D):
    # https://stackoverflow.com/a/31334882
    part1 = math.atan2(p3.y - p2.y, p3.x - p2.x)
    part2 = math.atan2(p1.y - p2.y, p1.x - p2.x)

    return abs(part1 - part2) * (180 / math.pi)

def calcKPDist(p1 : Keypoint2D, p2: Keypoint2D):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def calcCosineSimilarity(v1: List[float], v2: List[float]):
    # algorithm from https://stackoverflow.com/a/18424953
    if len(v1) != len(v2):
        raise ValueError("Vectors must be same length")
    
    sumxy, sumxx, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxy += x * y
        sumxx += x * x
        sumyy += y * y

    if sumxx == 0 or sumyy == 0:
        return 0

    return sumxy / math.sqrt(sumxx * sumyy)

# converts cv2 image to base64 string
def imageToBase64(image):
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text.decode('utf-8')

imported_dict = {}

# prevent unnecessary imports of intensive modules
def importModule(module_name):
    if module_name in imported_dict:
        return imported_dict[module_name]
    else:
        try:
            imported_dict[module_name] = importlib.import_module(module_name)
        except ImportError as e: # custom error handling if neccesary
            parent = module_name.split(".")[0]
            if parent == "rtmlib":
                raise ImportError("rtmlib is not installed. Please see installation instructions at https://github.com/Tau-J/rtmlib") from e
            raise e
            
    return imported_dict[module_name]