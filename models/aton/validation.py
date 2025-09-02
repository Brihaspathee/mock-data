class Validation:
    def __init__(self,
                 type,
                 source,
                 key,
                 element_id=None,
                 ):
        self.element_id = element_id
        self.type = type
        self.source = source
        self.key = key

    def __repr__(self):
        return (f"<Validation(element_id={self.element_id}, "
                f"type={self.type}, "
                f"source={self.source}, "
                f"key={self.key})>")