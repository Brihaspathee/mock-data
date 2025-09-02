import logging

from neo4j import Transaction
from neo4j.graph import Node
from repository import location_repo

from models.aton.location import Location

log = logging.getLogger(__name__)

def create_location(transaction: Transaction, location:Location):
    return location_repo.create_location(transaction, location)