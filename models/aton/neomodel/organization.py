from neomodel import StructuredNode, StringProperty


class Organization(StructuredNode):

    name: str = StringProperty(unique_index=True, required=True)
    description: str = StringProperty(required=False)
    type: str = StringProperty(required=True)