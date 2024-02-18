from __future__ import annotations

import asyncio
import logging
from typing import Any, List
import serial
import struct

from pymodbus.client.asynchronous import schedulers
from pymodbus.client.asynchronous.tcp import AsyncModbusTCPClient
from pymodbus.client.asynchronous.serial import AsyncModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient, ModbusSerialClient
from pymodbus.framer import socket_framer, rtu_framer, tls_framer, ModbusFramer
from pymodbus.exceptions import ConnectionException, TimeOutException
from multipledispatch import dispatch

from iot_protocols import IBasicProtocol
from iot_protocols.modbus.exceptions import *
from iot_protocols.modbus import requests
from iot_protocols.modbus.decoder import ModbusPayloadDecoder


MODBUS_FUNCTION_TO_CODE={
    0x01: "ReadCoils",
    0x02: "ReadDiscreteInput",
    0x03: "ReadHoldingRegister",
    0x04: "ReadInputRegister",
    0x05: "WriteCoils",
    0x06: "WriteRegister",
}

def request_factory(request: dict) -> requests.ReadCoils | requests.WriteCoils | requests.ReadCoils | requests.ReadDiscreteInput | requests.ReadHoldingRegister | requests.WriteRegister | requests.ReadInputRegister:
    """ Generate and validate a request for modbus client."""
    if "function" not in request:
        raise ModbusRequestException(f"Request type field missing in config : 'function'")
    
    _function = request.pop("function")
    
    # If the function field is set as modbus function code
    if _function in MODBUS_FUNCTION_TO_CODE:
        _function = MODBUS_FUNCTION_TO_CODE[_function]

    try:
        factory = getattr(requests, _function)
        return factory(**request)
        
    except AttributeError:
        raise ModbusRequestException(f"Invalid Modbus request function.")
    
    except TypeError as err:
        raise ModbusRequestException(f"Too many arguments passed in ModbusRequest config : {err}")


def handle_modbus_error(function: callable):
    def wrapper(request):
        print(f"Calling: {function} with argument request: {request}")
        try:
            print(f"the request: {request}")
            return function(request)
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    return wrapper


class ModbusClient(IBasicProtocol):

    def __init__(self, client):
        self._client: ModbusSerialClient = client

    def connect(self) -> bool:
        return self._client.connect()
    
    def disconnect(self) -> None:
        self._client.close()
    
    @dispatch(requests.ReadCoils)
    def request(self, request: requests.ReadCoils) -> List[bool]:
        try:
            self.connect()
            _response = self._client.read_coils(**request.__dict__)
            if _response.isError():
                raise ModbusRequestException(self._get_error_message(_response, request))
            
            result =  _response.bits[:request.count]
            if request.count==1:
                return result[0]
            self.disconnect()
            return result
        
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
    
    @dispatch(requests.WriteCoils)
    def request(self, request: requests.WriteCoils) -> List[bool]:
        try:
            self.connect()
            _request = self._client.write_coils(**request.__dict__)
            print(f"MODBUS RESPONSE ---> {_request}")
            if _request.isError():
                raise ModbusRequestException(self._get_error_message(_request, request))
            
            return self.request(requests.ReadCoils(address=request.address, count=len(request.values), unit=request.unit))
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    @dispatch(requests.ReadDiscreteInput)
    def request(self, request: requests.ReadDiscreteInput) -> List[bool]:
        try:
            self.connect()
            _response = self._client.read_discrete_inputs(**request.__dict__)
            if _response.isError():
                return ModbusRequestException(self._get_error_message(_response, request))

            result =  _response.bits[:request.count]
            if request.count==1:
                return result[0]
            self.disconnect()
            return result
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    @dispatch(requests.ReadInputRegister)
    def request(self, request: requests.ReadInputRegister) -> List[float | int | str] | float | int | str:
        try:
            self.connect()
            _response = self._client.read_input_registers(**request.__dict__)
            if _response.isError():
                return ModbusRequestException(self._get_error_message(_response, request))
            
            decoded = ModbusPayloadDecoder.decode(_response.registers, request.encoding)
            self.disconnect()
            if request.count == 1:
                return decoded[0]
            return decoded
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    @dispatch(requests.ReadHoldingRegister)
    def request(self, request: requests.ReadHoldingRegister) -> List[float | int | str] | float | int | str:
        try:
            self.connect()
            _response = self._client.read_holding_registers(**request.__dict__)
            if _response.isError():
                return ModbusRequestException(self._get_error_message(_response, request))
        
            decoded = ModbusPayloadDecoder.decode(_response.registers, request.encoding)
            self.disconnect()
            if request.count == 1:
                return decoded[0]
            return decoded
    
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    @dispatch(requests.WriteRegister)
    def request(self, request: requests.WriteRegister) -> List[float | int | str] | float | int | str:
        try:
            self.connect()
            _response = self._client.write_registers(**request.__dict__)
            if _response.isError():
                raise ModbusRequestException(self._get_error_message(_response, request))
            
            return self.request(requests.ReadHoldingRegister(address=request.address, count=len(request.values), unit=request.unit, encoding=str(type(request.values))))
        except ConnectionException as err:
            raise ModbusClientException(f"Could not connect to modbus client : {err}")
        except TimeoutError as err:
            raise ModbusRequestException(f"Request to the modbus device timeout : {err}")
        except Exception as err:
            raise ModbusRequestException(f"Request to the modbus device failed: {err}")
        
    def _get_error_message(self, exception, request, **kwargs) -> str:
        try:
            error_message = f"Error when executing Modbus Request from {self.__class__.__name__} with request {request} : {exception}"
            return error_message
        except Exception as err:
            logging.error(f"Could not generate error msg : {err}")
            return f"Modbus Request failed - Cannot get Error Message : {err}"

    @classmethod
    def with_serial_client(cls, port: str="/dev/ttyO3", method: str="rtu", baudrate: int=9600, parity: str=serial.PARITY_EVEN, stopbits: str=serial.STOPBITS_ONE, bytesize: str=serial.SEVENBITS, timeout: int = 10):
        """ Createa a ModbusClient isntance with serial transport communication."""
        client = ModbusSerialClient(
            port=port,
            method=method,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity,
            timeout=timeout,
            baudrate=baudrate
        )
        if isinstance(client, ModbusSerialClient):
            return cls(client)
        else:
            return ModbusClientException("Could not initiate modbus serial client")
        
    @classmethod
    def with_tcp_client(cls, host: str, port: int=502, timeout: int=10, framer: ModbusFramer = "socket", **kwargs):
        """ Create a ModbusClient instance with TCP transport communication."""

        if framer == "rtu":
            framer = rtu_framer.ModbusRtuFramer
        else:
            framer = socket_framer.ModbusSocketFramer

        client = ModbusTcpClient(
            host=host,
            port=port,
            timeout=timeout,
            framer=framer
        )
        if isinstance(client, ModbusTcpClient):
            return cls(client)
        else:
            raise ModbusClientException("Could not initiate modbus tcp client")


class ModbusTCP(ModbusClient):

    def __new__(cls, host: str, port: int=502, timeout: int=10, framer: ModbusFramer = "socket", **kwargs):
        return ModbusClient.with_tcp_client(
            host=host,
            port=port,
            timeout=timeout, framer=framer,
            **kwargs)    

class ModbusSerial(ModbusClient):

    def __new__(cls, port: str="/dev/ttyO3", method: str="rtu", baudrate: int=9600, parity: str=serial.PARITY_EVEN, stopbits: str=serial.STOPBITS_ONE, bytesize: str=serial.SEVENBITS, timeout: int = 5, **kwargs):
        return ModbusClient.with_serial_client(
            port=port,
            method=method,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity,
            timeout=timeout,
            baudrate=baudrate,
            **kwargs)


class AsyncModbusClient(IBasicProtocol):

    def __init__(self, client: AsyncModbusTCPClient | AsyncModbusSerialClient):
        self._client = client

    @dispatch(requests.ReadCoils)
    async def request(self, request: requests.ReadCoils) -> List[bool]:
        _response = await self._client.read_coils(**request.__dict__)
        if _response.isError():
            raise ModbusRequestException(self._get_error_message(_response, request))

        result =  _response.bits[:request.count]
        if request.count==1:
            return result[0]
        return result
    
    @dispatch(requests.WriteCoils)
    async def request(self, request: requests.WriteCoils) -> None:
        _response = await self._client.write_coils(**request.__dict__)
        if _response.isError():
            raise ModbusRequestException(self._get_error_message(_response, request))

    @dispatch(requests.ReadDiscreteInput)
    async def request(self, request: requests.ReadDiscreteInput) -> List[bool]:
        _response = await self._client.read_discrete_inputs(**request.__dict__)
        if _response.isError():
            return ModbusRequestException(self._get_error_message(_response, request))

        result =  _response.bits[:request.count]
        if request.count==1:
            return result[0]
        return result
    
    @dispatch(requests.ReadInputRegister)
    async def request(self, request: requests.ReadInputRegister) -> int | float:
        _response = await self._client.read_input_registers(**request.__dict__)
        if _response.isError():
            return ModbusRequestException(self._get_error_message(_response, request))
        
        return ModbusPayloadDecoder.decode(_response.registers, request.encoding)
    
    @dispatch(requests.ReadHoldingRegister)
    async def request(self, request: requests.ReadHoldingRegister) -> Any:
        try:
            _response = await self._client.read_holding_registers(**request.__dict__)
            if _response.isError():
                return ModbusRequestException(self._get_error_message(_response, request))
        
            return True, ModbusPayloadDecoder.decode(_response.registers, request.encoding)
        except Exception as err:
            logging.error(f"Read Holding Register Failed for (unit: {request.unit}, address: {request.address}, count: {request.count}) : {err}")
            raise ModbusRequestException(f"Read Holding register faile : {err}")
        
    @dispatch(requests.WriteRegister)
    async def request(self, request: requests.WriteRegister) -> None:
        _response = await self._client.write_coils(**request.__dict__)
        if _response.isError():
            raise ModbusRequestException(self._get_error_message(_response, request))
        
    def _get_error_message(self, exception, request, **kwargs) -> str:
        try:
            error_message = f"Error when executing Modbus Request from {self.__clas__.__name__} with request {request} : {exception}"
            return error_message
        except Exception as err:
            logging.error(f"Could not generate error msg : {err}")
            return f"Modbus Request failed - Cannot get Error Message : {err}"

    @classmethod
    def with_serial_client(cls, port: str="/dev/ttyO3", method: str="rtu", baudrate: int=9600, parity: str=serial.PARITY_EVEN, stopbits: str=serial.STOPBITS_ONE, bytesize: str=serial.SEVENBITS, timeout: int = 10):
        """ Createa a ModbusClient isntance with serial transport communication."""
        loop = asyncio.get_event_loop()
        client = AsyncModbusSerialClient(
            port=port,
            method=method,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity,
            timeout=timeout,
            baudrate=baudrate,
            scheduler=schedulers.ASYNC_IO,
            loop=loop
        )
        if isinstance(client, AsyncModbusSerialClient):
            return cls(client.protocol)
        else:
            return ModbusClientException("Could not initiate modbus serial client")
        
    @classmethod
    def with_tcp_client(cls, host: str, port: int=502, timeout: int=5, framer: ModbusFramer = "socket", **kwargs):
        """ Create a ModbusClient instance with TCP transport communication."""
        loop = asyncio.get_event_loop()

        if framer == "rtu":
            framer = rtu_framer.ModbusRtuFramer
        else:
            framer = socket_framer.ModbusSocketFramer

        loop, client = AsyncModbusTCPClient(
            host=host,
            port=port,
            timeout=timeout,
            framer=framer,
            scheduler=schedulers.ASYNC_IO,
            loop=loop
        )
        return cls(client.protocol)