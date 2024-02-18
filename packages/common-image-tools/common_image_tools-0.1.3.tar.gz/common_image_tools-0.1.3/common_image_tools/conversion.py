import cv2
import numpy as np
from PIL import Image
import dlib

# === PILLOW - OPENCV ==================================================================================================
def pil_to_cv2(pil_image: Image) -> np.ndarray:
    """
    Convert PIL image to cv2 image.

    Args:
        pil_image: PIL image

    Returns:
        cv2 image
    """

    # Convert PIL image to numpy array
    np_array = np.array(pil_image)

    # if the image is RGBA, then we need to convert it to BGRA
    if len(np_array.shape) == 3 and np_array.shape[2] == 4:
        return cv2.cvtColor(np_array, cv2.COLOR_RGBA2BGRA)

    return cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)


def cv2_to_pil(cv2_image: np.ndarray) -> Image:
    """
    Convert cv2 image to PIL image.

    Args:
        cv2_image: cv2 image

    Returns:
        PIL image
    """

    # if the image is RGBA, then we need to convert it to BGRA
    if len(cv2_image.shape) == 3 and cv2_image.shape[2] == 4:
        cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGRA2RGBA)
        return Image.fromarray(cv2_image)

    # Convert cv2 image to PIL image
    return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

# === DLIB =============================================================================================================

def rect_to_tuple(rect):
    return rect.left(), rect.top(), rect.right() - rect.left(), rect.bottom() - rect.top()

def tuple_to_rect(bbox):
    return dlib.rectangle(int(bbox[0]), int(bbox[1]),
                          int(bbox[2] + bbox[0]),
                          int(bbox[3] + bbox[1]))

# ======================================================================================================================