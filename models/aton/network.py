class Network:
    def __init__(self,
                 code,
                 name,
                 element_id=None,
                 description=None,):
        self.element_id = element_id
        self.code = code
        self.name = name
        self.description = description

    def __repr__(self):
        return (f"<Network(code={self.code}, "
                f"element_id={self.element_id},"
                f"name={self.name},"
                f"description={self.description})>")