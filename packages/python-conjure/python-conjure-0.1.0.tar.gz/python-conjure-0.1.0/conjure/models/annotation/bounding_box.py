from pydantic import BaseModel


class BoundingBox(BaseModel):
    """
    Describes an object's bounding box.

    Attributes
    ----------
    `class_name: str`
        A string depicting the type of object.

    `center_x: float`
        The center location of the bounding box along the x-axis in pixels.

    `center_y: float`
        The center location of the bounding box along the y-axis in pixels.

    `width: float`
        The width of the bounding box in pixels.

    `height: float`
        The height of the bounding box in pixels.
    """

    class_name: str
    center_x: float
    center_y: float
    width: float
    height: float
