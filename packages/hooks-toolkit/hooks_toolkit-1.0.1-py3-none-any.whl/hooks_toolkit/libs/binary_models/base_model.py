#!/usr/bin/env python
# coding: utf-8

from typing import List, Type

from hooks_toolkit.libs.binary_models.utils import (
    encode_field,
    decode_field,
    length_to_hex,
)


class BaseModel:
    @staticmethod
    def get_metadata() -> List[dict]:
        raise NotImplementedError("Subclasses must implement get_metadata() method.")

    def encode(self) -> str:
        return encode_model(self)

    @staticmethod
    def decode(hex: str, model_class: Type["BaseModel"]) -> "BaseModel":
        return decode_model(hex, model_class)

    @classmethod
    def get_hex_length(cls, model_class: Type["BaseModel"]) -> int:
        metadata = model_class.get_metadata()
        length = 0

        for field_metadata in metadata:
            field_type = field_metadata["type"]
            if field_type == "uint8":
                length += 2
            elif field_type == "uint32":
                length += 8
            elif field_type == "uint64":
                length += 16
            elif field_type == "uint224":
                length += 56
            elif field_type == "hash256":
                length += 64
            elif field_type == "publicKey":
                length += 66
            elif field_type == "varString":
                max_string_length = field_metadata.get("maxStringLength")
                if max_string_length is None:
                    raise ValueError("maxStringLength is required for type varString")
                length += max_string_length * 2 + (
                    2 if max_string_length <= 2**8 else 4
                )
            elif field_type == "xfl":
                length += 16
            elif field_type == "currency":
                length += 40
            elif field_type == "xrpAddress":
                length += 40
            elif field_type == "model":
                field_model_class = field_metadata.get("modelClass")
                if field_model_class is None:
                    raise ValueError("modelClass is required for type model")
                length += cls.get_hex_length(field_model_class)
            elif field_type == "varModelArray":
                raise ValueError(
                    "varModelArray hex length doesn't need to be computed for this"
                    "application; only its model elements only do. However, this will"
                    "fail if getHexLength is called on a model that contains a "
                    "varModelArray. Will need to be updated if this is ever needed."
                )
            else:
                raise ValueError(f"Unknown type: {field_type}")

        return length

    @classmethod
    def create_empty(cls, model_class: Type["BaseModel"]) -> "BaseModel":
        model_args = []
        metadata = model_class.get_metadata()

        for field_metadata in metadata:
            field_type = field_metadata["type"]
            if field_type == "uint8":
                model_args.append(0)
            elif field_type == "uint32":
                model_args.append(0)
            elif field_type == "uint64":
                model_args.append(0)
            elif field_type == "uint224":
                model_args.append(0)
            elif field_type == "hash256":
                model_args.append("")
            elif field_type == "publicKey":
                model_args.append("")
            elif field_type == "varString":
                model_args.append("")
            elif field_type == "xfl":
                model_args.append(0)
            elif field_type == "currency":
                model_args.append("")
            elif field_type == "xrpAddress":
                model_args.append("")
            elif field_type == "model":
                field_model_class = field_metadata.get("modelClass")
                if field_model_class is None:
                    raise ValueError("modelClass is required for type model")
                model_args.append(cls.create_empty(field_model_class))
            else:
                raise ValueError(f"Unknown type: {field_type}")

        return model_class(*model_args)


def decode_model(hex_str: str, model_class: Type[BaseModel]) -> BaseModel:
    metadata = model_class.get_metadata()
    model = model_class()

    hex_index = 0
    decoded_field = None
    for field_metadata in metadata:
        field_name = field_metadata["field"]
        field_type = field_metadata["type"]
        max_string_length = field_metadata.get("maxStringLength")
        field_model_class = field_metadata.get("modelClass")

        field_hex = ""
        if field_type == "uint8":
            field_hex = hex_str[hex_index : hex_index + 2]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 2

        elif field_type == "uint32":
            field_hex = hex_str[hex_index : hex_index + 8]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 8

        elif field_type == "uint64":
            field_hex = hex_str[hex_index : hex_index + 16]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 16

        elif field_type == "uint224":
            field_hex = hex_str[hex_index : hex_index + 56]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 56

        elif field_type == "hash256":
            field_hex = hex_str[hex_index : hex_index + 64]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 64

        elif field_type == "publicKey":
            field_hex = hex_str[hex_index : hex_index + 66]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 66

        elif field_type == "varString":
            if max_string_length is None:
                raise ValueError("maxStringLength is required for type varString")
            prefix_length_hex = 2 if max_string_length <= 2**8 else 4
            length = prefix_length_hex + max_string_length * 2
            field_hex = hex_str[hex_index : hex_index + length]
            decoded_field = decode_field(field_hex, field_type, max_string_length)
            hex_index += length

        elif field_type == "xfl":
            field_hex = hex_str[hex_index : hex_index + 16]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 16

        elif field_type == "currency":
            field_hex = hex_str[hex_index : hex_index + 40]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 40
        elif field_type == "xrpAddress":
            field_hex = hex_str[hex_index : hex_index + 40]
            decoded_field = decode_field(field_hex, field_type)
            hex_index += 40
        elif field_type == "model":
            if field_model_class is None:
                raise ValueError("modelClass is required for type model")
            model_hex_length = BaseModel.get_hex_length(field_model_class)
            field_hex = hex_str[hex_index : hex_index + model_hex_length]
            decoded_field = decode_model(field_hex, field_model_class)
            hex_index += model_hex_length
        elif field_type == "varModel":
            raise ValueError(f"Unknown type: {field_type}")
        else:
            raise ValueError(f"Unknown type: {field_type}")

        setattr(model, field_name, decoded_field)

    return model


def encode_model(model: BaseModel) -> str:
    metadata = model.get_metadata()

    result = ""
    for field_info in metadata:
        field = field_info["field"]
        field_type = field_info["type"]
        max_string_length = field_info.get("maxStringLength")
        max_array_length = field_info.get("maxArrayLength")

        field_value = getattr(model, field)
        if field_value is None:
            raise ValueError(f"Field {field} is undefined in model")

        encoded_field = ""
        if field_type == "model":
            encoded_field = encode_model(field_value)
        elif field_type == "varModelArray":
            if max_array_length is None:
                raise ValueError("maxArrayLength is required for type varModelArray")
            if len(field_value) > max_array_length:
                raise ValueError(
                    f"{field} varModelArray length {len(field_value)} exceeds"
                    f"maxArrayLength {max_array_length} for model"
                    f"{type(field_value[0]).__name__}"
                )
            length_hex = length_to_hex(len(field_value), 256)  # 1-byte max length
            encoded_field = length_hex
            for model_item in field_value:
                encoded_field += encode_model(model_item)
        else:
            encoded_field = encode_field(field_value, field_type, max_string_length)

        result += encoded_field

    return result
