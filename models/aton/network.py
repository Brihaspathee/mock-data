class Network:
    def __init__(self, code, name,
                 description=None,):
        self.code = code
        self.name = name
        self.description = description

    def __repr__(self):
        return (f"<Network(code={self.code}, "
                f"name={self.name},"
                f"description={self.description})>")