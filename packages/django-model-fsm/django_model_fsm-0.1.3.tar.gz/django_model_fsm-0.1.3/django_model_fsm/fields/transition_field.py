from django.db import models


class TransitionField(models.CharField):
    description = "Transition state"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = kwargs["max_length"] if "max_length" in kwargs else 255
        kwargs["blank"] = True
        kwargs["null"] = False

        super().__init__(*args, **kwargs)
