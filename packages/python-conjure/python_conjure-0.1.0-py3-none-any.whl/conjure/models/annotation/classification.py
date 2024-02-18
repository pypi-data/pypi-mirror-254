from pydantic import BaseModel


class Classification(BaseModel):
    """
    Stores classification annotations and predictions.

    Attributes
    ----------
    `class_name : str`
        The name associated with the classification of the image.
    """

    class_name: str
