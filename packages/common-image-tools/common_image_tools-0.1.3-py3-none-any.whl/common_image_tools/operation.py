import cv2
import numpy as np
from math import ceil


def resize_image_with_aspect_ratio(image: np.ndarray, size: tuple[int, int]) -> np.ndarray:
    """
    Resize an image while maintaining its aspect ratio using OpenCV.

    """
    width, height = size

    # Calculate the aspect ratio
    aspect_ratio = width / float(height)

    # Calculate new dimensions while preserving the aspect ratio
    if image.shape[1] / image.shape[0] > aspect_ratio:
        new_width = width
        new_height = int(width / image.shape[1] * image.shape[0])

    else:
        new_height = height
        new_width = int(height / image.shape[0] * image.shape[1])

    # Resize the image using the calculated dimensions
    resized_image = cv2.resize(image, (new_width, new_height))

    # Save the resized image
    return resized_image


def is_point_in_bbox(point: tuple[int, int], bbox: tuple[int, int, int, int]) -> bool:
    x1, y1, w, h = bbox
    x2, y2 = x1 + w, y1 + h
    x, y = point
    if x1 < x < x2 and y1 < y < y2:
        return True
    return False


def is_point_in_shape(point, shape_contour) -> bool:
    ctn = np.array(shape_contour)
    ctn = ctn.reshape((-1, 1, 2))

    # When measureDist=false , the return value is +1, -1, and 0, respectively. Otherwise, the return value is a
    # signed distance between the point and the nearest contour edge.
    result = cv2.pointPolygonTest(ctn, point, measureDist=False)

    return result >= 0


def scale_bboxes(bboxes: list[tuple], scale_factor: float) -> list[tuple]:
    """Ridimensiona i rettangoli per il fattore passato come parametro

    :param bboxes: Lista di rettangoli da ridimensionare
    :param scale_factor: Valore moltiplicativo
    :return: Lista di rettangoli ridimensionati
    """
    f_bboxes = []
    for box in bboxes:
        x, y, w, h = box
        f_bboxes.append(
            (ceil(x * scale_factor), ceil(y * scale_factor), ceil(w * scale_factor), ceil(h * scale_factor)))

    return f_bboxes


def bbox_centroid(bbox):
    x, y, w, h = bbox
    center_x = x + (w / 2)
    center_y = y + (h / 2)
    return int(center_x), int(center_y)
