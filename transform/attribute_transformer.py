from models.aton import Identifier, Qualification
from typing import Union, Literal, Any
from models.aton.identifier import IdentifierResult
from models.aton.qualification import QualificationResult
from config import settings
from models.portico import PPProvAttrib
import logging

log = logging.getLogger(__name__)


class AttributeStructure:
    """
    Represents the structure of an attribute with its associated metadata.

    This class encapsulates all attributes and details related to a specific entity, allowing for
    the representation, categorization, and relationship mapping of attributes in a structured
    manner. It also supports detailed customization via labels, field mappings, and conditions.

    :ivar entity_type: The type of the entity associated with this attribute.
    :type entity_type: str
    :ivar category: The category to which this attribute belongs.
    :type category: str
    :ivar labels: A list of labels or tags associated with this attribute.
    :type labels: list[str]
    :ivar relationship: The type of relationship this attribute has with other entities.
    :type relationship: str
    :ivar attr_type: The type of the attribute, specifying its function or category.
    :type attr_type: str
    :ivar issuer: The entity or source responsible for issuing this attribute.
    :type issuer: str
    :ivar name: The name or identifier for this attribute.
    :type name: str
    :ivar field_mappings: A mapping of field names to their corresponding values or identifiers.
    :type field_mappings: dict[str, str]
    :ivar conditions: A list of conditions or rules associated with this attribute.
    :type conditions: list[dict] | None
    """
    def __init__(self, entity_type:str,
                 category:str,
                 labels:list[str]=None,
                 relationship:str=None,
                 attr_type: str=None,
                 issuer: str=None,
                 name:str=None,
                 field_mappings:dict[str,str]=None,
                 conditions: list[dict] | None = None):
        self.entity_type = entity_type
        self.category = category
        self.issuer = issuer
        self.labels = labels or []
        self.relationship = relationship
        self.attr_type = attr_type
        self.name = name
        self.field_mappings = field_mappings or {}
        self.conditions = conditions or []

    def __repr__(self):
        """
        Provides a string representation of the instance for debugging and logging purposes.

        This method returns a string detailing the internal attributes of the class. It is
        helpful for inspecting the state of an object during development or logging. The
        representation includes all core attributes of the class instance in a readable format.

        :return: A string representation of the class instance, detailing its attributes.
        :rtype: str
        """
        return f"<AttributeStructure(entity_type={self.entity_type}, category={self.category}, " \
               f"labels={self.labels}, relationship={self.relationship}, attr_type={self.attr_type}, issuer= {self.issuer}, name={self.name}, " \
               f"field_mappings={self.field_mappings}, conditions={self.conditions})>"


Result = Union[IdentifierResult, QualificationResult]

def get_attribute(attribute:PPProvAttrib) -> Result :
    """
    Processes an attribute object by mapping its values to a structure based on its
    configuration and returns the processed result.

    This function takes an attribute object and processes its values by referring
    to the configuration provided in the application settings. It maps field IDs
    from the attribute to corresponding data in a dictionary, depending on whether
    the value is a date, number, or a generic value. Then it converts the collected
    field values into a structured node data.

    :param attribute: The attribute object to process.
    :type attribute: PPProvAttrib
    :return: The result object containing processed node data.
    :rtype: Result
    """
    # log.info(f"Flat config:{settings.FLAT_CONFIG}")
    # log.info(f"Attribute:{attribute}")
    # log.info(f"Attribute ID:{attribute.attribute_id}")
    attribute_structure: AttributeStructure = settings.ATTRIBUTE_STRUCTURES[str(attribute.attribute_id)]
    # log.info(f"Attribute Config:{attribute_structure}")
    # log.info(f"Attribute Category:{attribute_structure.category}")
    field_values: dict[str, Any] = {}
    for value in attribute.values:

        # log.info(f"Value:{value}")
        # log.info(f"Field ID:{value.field_id}")
        # log.info(f"Value:{value.value}")
        # log.info(f"Value Date:{value.value_date}")
        # log.info(f"Value Number:{value.value_number}")
        if value.value_date:
            field_values[value.field_id] = value.value_date
        elif value.value_number:
            field_values[value.field_id] = value.value_number
        else:
            field_values[value.field_id] = value.value
    field_values = {str(k): v for k, v in field_values.items()}
    result: Result = build_node_data(attribute_structure, field_values)
    # log.info(f"Result: {result}")
    # log.info(f"Result: {result.value}")
    return result

def build_node_data(attribute_structure: AttributeStructure, field_data: dict[str, Any]) -> Result :
    """
    Builds and processes node data based on the given attribute structure and field data.

    The function evaluates conditions and maps provided field data to build objects of different types,
    depending on the category of the attribute structure. If the category is 'identifier', it constructs
    an identifier object, and if the category is 'qualification', it constructs a qualification object.
    The resulting object is then wrapped into a result object specific to the respective category.

    :param attribute_structure: Contains the attribute details like category, conditions, type, labels,
        and field mappings used for processing the field data.
    :type attribute_structure: AttributeStructure
    :param field_data: A dictionary containing the field values to be processed and mapped based on
        the attribute structure's field mappings.
    :type field_data: dict[str, Any]
    :return: A result object containing the kind of object constructed and its respective value.
    :rtype: Result
    :raises ValueError: If the attribute category is invalid or not supported.
    """
    if attribute_structure.category == "qualification" and attribute_structure.conditions:
        if not evaluate_conditions(attribute_structure, field_data):
            return QualificationResult(kind="qualification", value=None)

    kwargs = {}
    for field_id, value in field_data.items():
        mapped_field = attribute_structure.field_mappings.get(str(field_id))
        # log.info(f"Mapping field {field_id} to {mapped_field}")
        if mapped_field and mapped_field != "NOT-MAPPED":
            kwargs[mapped_field] = value

    if attribute_structure.category == "identifier":
        kwargs["identifier_type"] = attribute_structure.attr_type
        kwargs["identifier_label"] = attribute_structure.labels[0] if attribute_structure.labels else None
        # log.info(f"Attribute relationship:{attribute_structure.relationship}")
        kwargs["identifier_rel"] = attribute_structure.relationship
        # log.info(f"Built kwargs:{kwargs}")
        identifier_obj = Identifier(**kwargs)
        # log.info(f"Identifier Object:{identifier_obj}")
        return IdentifierResult(kind="identifier", value=identifier_obj)
    elif attribute_structure.category == "qualification":
        kwargs["qualification_type"] = attribute_structure.attr_type
        kwargs["issuer"] = attribute_structure.issuer
        kwargs["secondary_labels"] = attribute_structure.labels
        qual_obj = Qualification(**kwargs)
        return QualificationResult(kind="qualification", value=qual_obj)
    else:
        raise ValueError(f"Invalid attribute category: {attribute_structure.category}")

def evaluate_conditions(attribute_structure: AttributeStructure, field_data: dict[str, Any]) -> bool:
    """
    Evaluate a set of conditions against the provided field data and determine if all conditions are satisfied.

    This function iterates over a list of conditions defined in the `attribute_structure`.
    Each condition specifies an operation to be performed on a field value retrieved
    from the `field_data` dictionary. The function evaluates each condition using the
    corresponding operator and expected value, and returns a boolean indicating whether
    all conditions evaluate to `True`. If any condition fails, the function returns `False`.
    It also logs the actual value of the field being evaluated.

    Parameters
    ----------
    :param attribute_structure: The structure containing conditions to evaluate. It is expected
        to have a `conditions` attribute, which is a list of dictionaries. Each dictionary
        should specify the field ID, operator, and value for the condition.
    :type attribute_structure: AttributeStructure
    :param field_data: A dictionary containing field values to be evaluated against the conditions.
    :type field_data: dict[str, Any]

    Returns
    -------
    :return: A boolean indicating whether all conditions were satisfied.
    :rtype: bool

    Raises
    ------
    :raises ValueError: If an invalid or unsupported operator is provided in any condition.
    """
    for condition in attribute_structure.conditions:
        field_id = condition["field_id"]
        operator = condition["operator"]
        expected_value = condition["value"]
        # Check of the field_id exists as a key in the field_data dictionary,
        # If it does, check if the value is not None (i.e. it's not empty)')
        if field_id in field_data and field_data[field_id] is not None:
            actual_value = field_data[field_id]
            # log.info(f"Actual value: {actual_value}")
            if operator == "equals":
                if actual_value != expected_value:
                    return False
            elif operator == "not-equals":
                if actual_value == expected_value:
                    return False
            elif operator == "contains" or operator == "in":
                if expected_value not in actual_value:
                    return False
            elif operator == "not-contains" or operator == "not-in":
                if expected_value in actual_value:
                    return False
            elif operator == "less-than":
                if actual_value is None or actual_value >= expected_value:
                    return False
            elif operator == "greater-than":
                if actual_value is None or actual_value <= expected_value:
                    return False
            else:
                raise ValueError(f"Invalid operator: {operator} is not implemented")
    return True