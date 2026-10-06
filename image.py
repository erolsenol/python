"""Validated OpenCV template matching without desktop or window side effects."""
from pathlib import Path
import cv2


def _read_images(image_path, template_path):
    if not image_path or not template_path:
        raise ValueError('Both image paths are required')
    image = cv2.imread(str(Path(image_path)))
    template = cv2.imread(str(Path(template_path)))
    if image is None or template is None:
        raise ValueError('Image or template could not be decoded')
    if template.shape[0] > image.shape[0] or template.shape[1] > image.shape[1]:
        raise ValueError('Template must fit inside the image')
    return image, template


def imageSearch(img1=None, img2=None):
    image, template = _read_images(img1, img2)
    result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)
    _, _, location, _ = cv2.minMaxLoc(result)
    return {'x': location[0] + 15, 'y': location[1] + 40}


def hasImageReturnCoor(img1=None, img2=None, threshold=0.95):
    if not 0 <= threshold <= 1:
        raise ValueError('Threshold must be between zero and one')
    image, template = _read_images(img1, img2)
    # Normalized correlation uses the maximum score and its matching position.
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, score, _, location = cv2.minMaxLoc(result)
    if score < threshold:
        return False
    return {'x': location[0] + 15, 'y': location[1] + 40}
