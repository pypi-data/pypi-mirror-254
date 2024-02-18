from pydantic import BaseModel

from conjure.models.annotation.bounding_box import BoundingBox


class ObjectDetection(BaseModel):
    """
    Stores object detection annotations and predictions.

    Attributes
    ----------
    `boxes : list[BoundingBox]`
        Bounding boxes of the objects in the image.
    """

    boxes: list[BoundingBox]
