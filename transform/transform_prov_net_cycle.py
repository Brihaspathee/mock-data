from neo4j.graph import Node

from models.aton import Organization, Contact, Telecom
from models.aton.location import Location
from models.aton.network import Network
from models.aton.role_instance import RoleInstance
from models.aton.role_location import RoleLocation
from models.aton.role_network import RoleLocationServes, AssociatedLocation, RoleNetwork
from models.portico import PPProv, PPProvTinLoc, PPProvLoc, PPPhones, PPAddrPhones
import logging

from repository.location_repo import get_location_by_smarty_key
from repository.network_repo import match_network
from utils.hash_util import hash_utility

log = logging.getLogger(__name__)


def transform_prov_net_cycle(provider: PPProv, organization:Organization):
    role_instance: RoleInstance = RoleInstance()

    if provider.prov_locs:
        _process_prov_locs(provider.prov_locs, role_instance, organization)
    if provider.networks:
        role_networks: list[RoleNetwork] = []
        # there are one or more prv net cycles
        # combine pnc's of providers with the same network
        # ignore networks that are not in PAR status
        for network_cycle in provider.networks:
            status = network_cycle.status
            log.info(f"Network Status:{status}")
            # role_network: RoleNetwork | None = None
            if status == "PAR":
                network_id = network_cycle.network.id
                network_name = network_cycle.network.name
                log.info(f"Network ID:{network_id}")
                log.info(f"Network Name:{network_name}")
                # check if network is already present in role networks
                role_network = _is_net_present(network_id, role_networks)
                if not role_network:
                    log.info(f"Network {network_id} not present in role networks")
                    new_rn: RoleNetwork = _transform_net_cycle(network_cycle, network_id, network_name, role_instance)
                    role_networks.append(new_rn)
                else:
                    log.info(f"Network {network_id} present in role networks")
                    # _transform_net_cycle(network_cycle, network_id, network_name, role_instance, role_network,
                    #                      role_networks)
                    for loc_cycle in network_cycle.loc_cycles:
                        pp_prov_tin_loc: PPProvTinLoc = loc_cycle.location
                        assoc_locs: list[AssociatedLocation] = role_network.associated_locations
                        associated_loc: AssociatedLocation | None = _fetch_associated_location(assoc_locs,
                                                                                               pp_prov_tin_loc)
                        if associated_loc:
                            rls: RoleLocationServes = RoleLocationServes()
                            rls.start_date = loc_cycle.start_date
                            rls.end_date = loc_cycle.end_date
                            associated_loc.role_location_serves.append(rls)
                        else:
                            associated_location = _create_assoc_loc(loc_cycle, pp_prov_tin_loc, role_instance)
                            role_network.associated_locations.append(associated_location)

                # log.info(f"Role Network before appending:{role_network}")
                # role_networks.append(role_network)
        for rn in role_networks:
            log.info(f"Role Network after appending to role networks list:{rn}")
        role_instance.roleNetworks = role_networks
    organization.roleInstances.append(role_instance)

def _process_prov_locs(prov_locs: list[PPProvLoc], role_instance: RoleInstance, organization: Organization) :
    role_locations: list[RoleLocation] = []
    for prov_loc in prov_locs:
        role_location: RoleLocation = RoleLocation()
        role_location.contacts = []
        prov_tin_loc: PPProvTinLoc = prov_loc.location
        # log.info(f"Location:{location}")
        log.info(f"Location Address:{prov_tin_loc.address}")
        hash_code = hash_utility(prov_tin_loc.address.addr1,
                                 prov_tin_loc.address.addr2,
                                 prov_tin_loc.address.city,
                                 prov_tin_loc.address.state,
                                 prov_tin_loc.address.zip,
                                 prov_tin_loc.address.county,
                                 prov_tin_loc.address.fips)
        log.info(f"Hash Code:{hash_code}")
        location_node = get_location_by_smarty_key(hash_code)
        if location_node:
            log.info(f"Location node:{location_node}")
            location: Location = Location()
            location.element_id = location_node.element_id
            location.smarty_key = hash_code
            role_location.location = location
            role_locations.append(role_location)
        else:
            log.info(f"Location node not found for smarty key: {hash_code}")
            location: Location = Location()
            log.info(f"Location name:{prov_tin_loc.name}")
            location.location_name = prov_tin_loc.name
            location.street_address = prov_tin_loc.address.addr1
            location.secondary_address = prov_tin_loc.address.addr2
            location.city = prov_tin_loc.address.city
            location.state = prov_tin_loc.address.state
            location.zip_code = prov_tin_loc.address.zip
            location.county = prov_tin_loc.address.county
            location.fips = prov_tin_loc.address.fips
            location.latitude = prov_tin_loc.address.latitude
            location.longitude = prov_tin_loc.address.longitude
            location.smarty_key = hash_code
            log.info(f"Location data:{location}")
            # TODO: Add phone and fax to Role Location
            if prov_tin_loc.address.phones:
                if prov_tin_loc.address.type == "MAIN":
                    contact: Contact = Contact(use="Directory")
                    telecom: Telecom = Telecom()
                    log.info("Location has address")
                    log.info(f"Location phone:{prov_tin_loc.address.phones}")
                    addr_phones: list[PPAddrPhones] = prov_tin_loc.address.phones
                    for addr_phone in addr_phones:
                        log.info(f"Phone:{addr_phone.phone}")
                        log.info(f"Phone Type:{addr_phone.phone.type}")
                        log.info(f"Phone area:{addr_phone.phone.area_code}")
                        log.info(f"Phone exchange:{addr_phone.phone.exchange}")
                        log.info(f"Phone number:{addr_phone.phone.number}")
                        phone_number: str = addr_phone.phone.area_code + addr_phone.phone.exchange +  addr_phone.phone.number
                        if addr_phone.phone.type == "PHONE":
                            telecom.phone = phone_number
                        contact.telecom = telecom
            role_location.contacts.append(contact)
            role_location.location = location
            role_locations.append(role_location)
        role_instance.roleLocations = role_locations

def _is_net_present(net_id: int, rns: list[RoleNetwork]) -> RoleNetwork | None:
    for rn in rns:
        if str(net_id) == rn.network.code:
            return rn
    return None

def _fetch_role_location(rls: list[RoleLocation], prov_tin_loc: PPProvTinLoc) -> RoleLocation | None:
    hash_code = hash_utility(prov_tin_loc.address.addr1,
                             prov_tin_loc.address.addr2,
                             prov_tin_loc.address.city,
                             prov_tin_loc.address.state,
                             prov_tin_loc.address.zip,
                             prov_tin_loc.address.county,
                             prov_tin_loc.address.fips)
    for rl in rls:
        if rl.location.smarty_key == hash_code:
            return rl
    return None

def _fetch_associated_location(assoc_locs: list[AssociatedLocation],
                                                  prov_tin_loc: PPProvTinLoc) -> AssociatedLocation | None :
    for assoc_loc in assoc_locs:
        rl: RoleLocation = assoc_loc.roleLocation
        hash_code = hash_utility(prov_tin_loc.address.addr1,
                                 prov_tin_loc.address.addr2,
                                 prov_tin_loc.address.city,
                                 prov_tin_loc.address.state,
                                 prov_tin_loc.address.zip,
                                 prov_tin_loc.address.county,
                                 prov_tin_loc.address.fips)
        if rl.location.smarty_key == hash_code:
            return assoc_loc
    return None

def _transform_net_cycle(network_cycle, network_id, network_name, role_instance) -> RoleNetwork:
    network_node: Node = match_network(network_id)
    net_node_dict = dict(network_node)
    log.info(f"Match network properties:{net_node_dict}")
    log.info(f"Network ID:{net_node_dict["code"]}")
    log.info(f"Network element is:{network_node.element_id}")
    log.info(f"Network ID:{net_node_dict["name"]}")
    if network_node:
        net_element_id = network_node.element_id
        net_node_dict = dict(network_node)
        network = Network(element_id=net_element_id,
                          code=net_node_dict["code"],
                          name=net_node_dict["name"])
    else:
        network: Network = Network(code=network_id, name=network_name)
    # network: Network = Network(element_id=network_node.element_id, code=network_id, name=network_name)
    new_rn: RoleNetwork = RoleNetwork()
    new_rn.network = network
    log.info(f"Location cycles for network :{network_name}")
    assoc_locations: list[AssociatedLocation] = []
    for loc_cycle in network_cycle.loc_cycles:
        log.info(f"Network Location Cycle {loc_cycle}")
        log.info(f"Location in the cycle - {loc_cycle.location}")
        log.info(f"Location element id - {loc_cycle.location.id}")
        pp_prov_tin_loc: PPProvTinLoc = loc_cycle.location
        # check if an associated location already exists for this location
        assoc_loc: AssociatedLocation = _fetch_associated_location(assoc_locations, pp_prov_tin_loc)
        # if yes, append the role location serves to the existing associated location
        if assoc_loc:
            rls_new: RoleLocationServes = RoleLocationServes()
            rls_new.start_date = loc_cycle.start_date
            rls_new.end_date = loc_cycle.end_date
            assoc_loc.role_location_serves.append(rls_new)
        else:
            # if no, create a new associated location and append it to the list of associated locations
            associated_location = _create_assoc_loc(loc_cycle, pp_prov_tin_loc, role_instance)
            assoc_locations.append(associated_location)
    new_rn.associated_locations = assoc_locations
    return new_rn


def _create_assoc_loc(loc_cycle, pp_prov_tin_loc, role_instance):
    associated_location: AssociatedLocation = AssociatedLocation()
    associated_location.role_location_serves = []
    role_location: RoleLocation = _fetch_role_location(role_instance.roleLocations, pp_prov_tin_loc)
    associated_location.roleLocation = role_location
    log.info(f"Associated Location:{associated_location}")
    log.info(f"Associated Location - RLS:{associated_location.role_location_serves}")
    rls: RoleLocationServes = RoleLocationServes()
    rls.start_date = loc_cycle.start_date
    rls.end_date = loc_cycle.end_date
    associated_location.role_location_serves.append(rls)
    log.info(f"Associated Location:{associated_location}")
    log.info(f"Associated Location - rls:{associated_location.role_location_serves}")
    return associated_location
