from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "olive_harvester olive_timelord_launcher olive_timelord olive_farmer olive_full_node olive_wallet".split(),
    "node": "olive_full_node".split(),
    "harvester": "olive_harvester".split(),
    "farmer": "olive_harvester olive_farmer olive_full_node olive_wallet".split(),
    "farmer-no-wallet": "olive_harvester olive_farmer olive_full_node".split(),
    "farmer-only": "olive_farmer".split(),
    "timelord": "olive_timelord_launcher olive_timelord olive_full_node".split(),
    "timelord-only": "olive_timelord".split(),
    "timelord-launcher-only": "olive_timelord_launcher".split(),
    "wallet": "olive_wallet olive_full_node".split(),
    "wallet-only": "olive_wallet".split(),
    "introducer": "olive_introducer".split(),
    "simulator": "olive_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
