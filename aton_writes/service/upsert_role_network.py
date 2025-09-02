import logging

from neo4j import Transaction
from neo4j.graph import Node, Graph

from models.aton.network import Network
from models.aton.role_network import RoleNetwork
from repository import role_location_repo, role_network_repo
from models.aton.role_location import RoleLocation

log = logging.getLogger(__name__)



def create_rn(transaction: Transaction, ri_node:Node,
              role_network:RoleNetwork):
    network: Network = role_network.network
    net_node = Node(Graph(), network.element_id, 0)
    rn_node = role_network_repo.create_role_network(transaction, ri_node, net_node)
    role_network.element_id = rn_node.element_id

    for associated_location in role_network.associated_locations:
        log.info(f"There are associated locations:{associated_location}")
        role_location: RoleLocation = associated_location.roleLocation
        rl_node: Node = Node(Graph(), role_location.element_id, 0, n_labels=['RoleLocation'], properties={})
        for role_location_serve in associated_location.role_location_serves:
            log.info(f"There are role location serves:{role_location_serve}")
            role_network_repo.create_rls(transaction, rl_node=rl_node, rn_node=rn_node, rls=role_location_serve)

    return rn_node