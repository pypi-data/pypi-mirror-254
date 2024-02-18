from typing import Any, Sequence

from palworld_save_tools.archive import *

NO_OP_TYPES = [
    "EPalBaseCampModuleType::Energy",
    "EPalBaseCampModuleType::Medical",
    "EPalBaseCampModuleType::ResourceCollector",
    "EPalBaseCampModuleType::ItemStorages",
    "EPalBaseCampModuleType::FacilityReservation",
    "EPalBaseCampModuleType::ObjectMaintenance",
]


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]:
    if type_name != "MapProperty":
        raise Exception(f"Expected MapProperty, got {type_name}")
    value = reader.property(type_name, size, path, nested_caller_path=path)
    # module map
    module_map = value["value"]
    for module in module_map:
        module_type = module["key"]
        module_bytes = module["value"]["RawData"]["value"]["values"]
        print(module_type)
        print("".join(f"{b:02x}" for b in module_bytes))
        # module["value"]["RawData"]["value"] = decode_bytes(module_bytes, module_type)
    return value


def pal_item_and_slot_read(reader: FArchiveReader) -> dict[str, Any]:
    return {
        "item_id": {
            # "static_id": reader.fstring(),
            # "dynamic_id": {
            "created_world_id": reader.guid(),
            "local_id_in_created_world": reader.guid(),
            # }
        },
        "slot_id": reader.guid(),
    }


def transport_item_character_info_reader(reader: FArchiveReader) -> dict[str, Any]:
    return {
        "item_infos": reader.tarray,
        "character_location": reader.vector_dict,
    }


PASSIVE_EFFECT_ENUM = {
    0: "EPalBaseCampPassiveEffectType::None",
    1: "EPalBaseCampPassiveEffectType::WorkSuitability",
    2: "EPalBaseCampPassiveEffectType::WorkHard",
}


def module_passive_effect_reader(reader: FArchiveReader) -> dict[str, Any]:
    data = {}
    data["type"] = reader.byte()
    if data["type"] not in PASSIVE_EFFECT_ENUM:
        raise Exception(f"Unknown passive effect type {data['type']}")
    elif data["type"] == 1:
        data["work_hard_type"] = reader.byte()
    return data


def decode_bytes(
    parent_reader: FArchiveReader, b_bytes: Sequence[int], module_type: str
) -> dict[str, Any]:
    reader = parent_reader.internal_copy(bytes(b_bytes), debug=False)
    data: dict[str, Any] = {}
    if module_type in NO_OP_TYPES:
        pass
    elif module_type == "EPalBaseCampModuleType::TransportItemDirector":
        try:
            data["transport_item_character_infos"] = reader.tarray(
                transport_item_character_info_reader
            )
        except Exception as e:
            print(
                f"Warning: Failed to decode transport item director, please report this: {e} ({bytes(b_bytes)!r})"
            )
            return {"values": b_bytes}
    elif module_type == "EPalBaseCampModuleType::PassiveEffect":
        try:
            data["passive_effects"] = reader.tarray(module_passive_effect_reader)
        except Exception as e:
            reader.data.seek(0)
            print(
                f"Warning: Failed to decode passive effect, please report this: {e} ({bytes(b_bytes)!r})"
            )
            return {"values": b_bytes}
    else:
        print(f"Warning: Unknown base camp module type {module_type}, skipping")
        return {"values": b_bytes}

    if not reader.eof():
        raise Exception(f"Warning: EOF not reached for {module_type}")

    return data


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int:
    if property_type != "MapProperty":
        raise Exception(f"Expected MapProperty, got {property_type}")
    del properties["custom_type"]
    # encoded_bytes = encode_bytes(properties["value"])
    # properties["value"] = {"values": [b for b in encoded_bytes]}
    return writer.property_inner(property_type, properties)


def encode_bytes(p: dict[str, Any]) -> bytes:
    writer = FArchiveWriter()
    writer.byte(p["state"])
    writer.guid(p["id"])
    encoded_bytes = writer.bytes()
    return encoded_bytes
