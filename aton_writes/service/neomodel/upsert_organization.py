from models.aton.neomodel.organization import Organization
import logging

log = logging.getLogger(__name__)

def save_organization(organization: Organization):
    try:
        organization.save()
        return True
    except Exception as e:
        log.error(e)
        return False

