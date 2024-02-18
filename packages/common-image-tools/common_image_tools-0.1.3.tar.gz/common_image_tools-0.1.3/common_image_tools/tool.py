import cv2
import numpy as np
from PIL import Image


def merge_color(image: np.ndarray, mask: np.ndarray, target_color_rgb: tuple) -> np.ndarray:
    """Merge the target color with the image using the mask using hsv color space.ù

    Args:
        image (np.ndarray): Image in opencv format (BGR)
        mask (np.ndarray): Mask in opencv format one channel
        target_color_rgb (tuple): Target color in RGB format

    Returns:
        np.ndarray: Image with merged color in opencv format (BGR)

    """
    hsv_image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv_image)

    color_to_merge = np.uint8([[target_color_rgb[:: -1]]])
    hsv_color = cv2.cvtColor(color_to_merge, cv2.COLOR_BGR2HSV)

    h.fill(hsv_color[0][0][0])
    s.fill(hsv_color[0][0][1])

    new_hsv_image = cv2.merge([h, s, v])

    new_hsv_image = cv2.cvtColor(new_hsv_image, cv2.COLOR_HSV2BGR)

    colored_image = cv2.bitwise_and(new_hsv_image, new_hsv_image, mask=mask)
    original_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    final_img = cv2.bitwise_xor(colored_image, original_image)

    return final_img


def merge_texture(image, mask, texture, alpha=0.3):
    """Merge the texture with the image using the mask using hsv color space."""

    # if texture is smaller than image, resize it
    # if texture.shape[0] < image.shape[0] or texture.shape[1] < image.shape[1]:
    pattern = cv2.resize(texture, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_AREA)
    # pattern = pil_image_to_cv2(resize_image(cv2_image_to_pil(texture), image.shape[1]))
    # pattern = texture[0:image.shape[0], 0:image.shape[1]]

    # crop texture to image size

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    hsv_pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2HSV)
    hp, sp, vp = cv2.split(hsv_pattern)

    # new_h = cv2.add(hp, h)
    # new_s = cv2.add(sp, s)
    # new_v = cv2.add(vp, vp)

    beta = (1.0 - alpha)
    new_v = cv2.addWeighted(v, alpha, vp, beta, 0)

    new_hsv_image = cv2.merge([hp, sp, new_v])
    # new_hsv_image = cv2.merge([new_h, new_s, v])

    new_hsv_image = cv2.cvtColor(new_hsv_image, cv2.COLOR_HSV2BGR)

    colored_image = cv2.bitwise_and(new_hsv_image, new_hsv_image, mask=mask)
    original_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    final_img = cv2.bitwise_xor(colored_image, original_image)

    return final_img


def create_pil_image(size: tuple, color: tuple) -> Image:
    """Create a PIL image with the specified color and size.

    Args:
        size (tuple): Size of the image
        color (tuple): Color of the image in RGB format

    Returns:
        PIL.Image: Image in PIL format (RGB)
    """
    from PIL import Image

    return Image.new("RGB", size, color)


def create_cv2_image(size: tuple, color: tuple) -> np.ndarray:
    """Create a cv2 image with the specified color and size.

    Args:
        size (tuple): Size of the image
        color (tuple): Color of the image in BGR format

    Returns:
        np.ndarray: Image in opencv format (BGR)
    """
    img = np.zeros((size[0], size[1], 3), np.uint8)
    img[:] = color
    return img

