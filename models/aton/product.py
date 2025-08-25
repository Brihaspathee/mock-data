from models.aton.network import Network


class Product:
    def __init__(self,
                 code,
                 name,
                 description=None,
                 networks: list[Network]=None):
        self.code = code
        self.name = name
        self.description = description
        if networks is None:
            self.networks = []
        else:
            self.networks = networks

    def __repr__(self):
        return (f"<Product(code={self.code}, "
                f"name={self.name},"
                f"description={self.description},"
                f"networks={self.networks})>")