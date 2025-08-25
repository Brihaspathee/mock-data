from models.aton.network import Network
from models.aton.product import Product
from models.portico.pp_net import PPNet, PPNetDict
from transform.transformers import transform_to_aton
import logging

log = logging.getLogger(__name__)

@transform_to_aton.register(PPNet)
def _(network:PPNet) -> Product | None:
    """
    Transforms an instance of `PPNet` to a corresponding `Product` object, including its
    child PPNet objects as networks of the product. The transformation involves converting
    relevant attributes of the `PPNet` instance into attributes of the `Product` object
    and its associated networks.

    :param network: An instance of `PPNet` to be transformed.
    :type network: PPNet
    :return: A `Product` instance created from the given `PPNet` instance, or `None` if
             the transformation is unsuccessful.
    :rtype: Product | None
    """
    net_dict: PPNetDict = network.to_dict()
    log.info(f"Transforming network {net_dict}")
    product: Product = Product(
        code=net_dict["id"],
        name=net_dict["name"],
        description=net_dict["description"])
    networks: list[PPNetDict] = net_dict["children"]
    for network in networks:
        net: Network = Network(
            code=network["id"],
            name=network["name"],
            description=network["description"]
        )
        product.networks.append(net)
    return product