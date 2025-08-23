from sqlalchemy import select, Sequence
from sqlalchemy.orm import joinedload, Session

from models.portico import PPProv, PPAddr, PPProvAddr, PPAddrPhones, PPProvAttribValues, PPProvTIN

from models.portico.pp_prov_attrib import PPProvAttrib
import logging

log = logging.getLogger(__name__)


def read_provider(session:Session) -> list[PPProv] | None:
    stmt = (
        select(PPProv)
        .options(
            joinedload(PPProv.addresses)
            .joinedload(PPProvAddr.address)
            .joinedload(PPAddr.phones)
            .joinedload(PPAddrPhones.phone),
            joinedload(PPProv.prov_type),
            joinedload(PPProv.tin),
            joinedload(PPProv.attributes).joinedload(PPProvAttrib.attribute_type),
            joinedload(PPProv.attributes).joinedload(PPProvAttrib.values).joinedload(PPProvAttribValues.field),
        )
    )
    providers: list[PPProv] = list(session.execute(stmt).unique().scalars().all())
    log.info(f"Read providers successfully:{providers}")
    return providers

