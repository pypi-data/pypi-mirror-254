import logging

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

from iot_protocols.modbus.exceptions import ModbusDecoderException
class ModbusPayloadDecoder:
    _elements_size = {
        "bool": 1,
        "8bit_int": 1,
        "16bit_int": 1,
        "32bit_int":2,
        "64bit_int": 4,
        "8bit_uint": 1,
        "16bit_uint": 1,
        "32bit_uint": 2,
        "64bit_uint": 4,
        "16bit_float": 1,
        "32bit_float": 2,
        "64bit_float": 4
    }
    _functions_map = {
        "8bit_int": BinaryPayloadDecoder.decode_8bit_int,
        "16bit_int": BinaryPayloadDecoder.decode_16bit_int,
        "32bit_int":BinaryPayloadDecoder.decode_32bit_int,
        "64bit_int": BinaryPayloadDecoder.decode_64bit_int,
        "8bit_uint": BinaryPayloadDecoder.decode_8bit_uint,
        "16bit_uint": BinaryPayloadDecoder.decode_16bit_uint,
        "32bit_uint": BinaryPayloadDecoder.decode_32bit_uint,
        "64bit_uint": BinaryPayloadDecoder.decode_64bit_uint,
        "16bit_float": BinaryPayloadDecoder.decode_16bit_float,
        "32bit_float": BinaryPayloadDecoder.decode_32bit_float,
        "64bit_float": BinaryPayloadDecoder.decode_64bit_float,
        "str": BinaryPayloadDecoder.decode_string,
        "string": BinaryPayloadDecoder.decode_string
    }
    @classmethod
    def decode(cls, registers, encoding):
        if encoding not in cls._functions_map:
            return registers
        
        try:
            decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big)
            f = cls._functions_map[encoding]
            if encoding == "str" or encoding=="string":
                size = len(registers)*2 # one register (word) store 2 char
                return f(decoder, size).decode().strip("\x00")
            return f(decoder)
        except KeyError as err:
            logging.error(f"Encoding specified for decoding isn't valid : {err}.")
        except Exception as err:
            logging.error(f"Cannot decode modbus registers : {err}")
    
    @staticmethod
    def get_element_size(type: str):
        try:
            return ModbusPayloadDecoder._elements_size[type]
        except Exception as err:
            logging.error(f"Invalid Type : {type}")
            raise ModbusDecoderException(f"Invalid Type : {type}")