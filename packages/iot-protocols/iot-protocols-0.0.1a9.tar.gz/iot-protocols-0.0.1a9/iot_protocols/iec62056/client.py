from __future__ import annotations
"""
? Author : Delhaye Adrien
IEC 62056 (serial/tcp) module.
This module allows to exchange data using the IEC62056 protocol over a serial line.
* How to use : 
    1) create a client : client = IEC62056Client(baudrate=xxx, device_address="xxx", port="xxx")
    2) client.connect()
    3) read all or registers : client.read_all() | client.read_registers(registers = ["1.8.0", "2.8.0"])
"""
import logging
import time
import serial

from typing import List, Tuple

from iec62056 import client, messages, constants

from iot_protocols.iec62056 import requests
from iot_protocols.iec62056.exceptions import *
from iot_protocols._base import IBasicProtocol

logger = logging.getLogger(__name__)


def request_factory(request: dict) -> requests.ReadoutRequest:
    """ Generate and validate a request for modbus client."""
    
    try:
        factory = getattr(requests, request["function"])
        return factory(**request)

    except KeyError as err:
        raise IEC62056RequestException(f"Missing request function to use: {err}")
      
    except AttributeError as err:
        raise IEC62056RequestException(f"Invalid request passed in function: {err}")


class IEC62056Client(IBasicProtocol):
    
    """Class to communicate with meter using IEC62056-21 protocol.
    Usage:
    - Create a new client specifying it's baudrate, the port, if needed the meter address (serial number, ..) and the type of client (serial, tcp (encapsulated), ..).
    - To request all dataset available use client.read_all()
    - To request a particular register use client.read_registers(list_of_registers_by_obis_code).

    Returns:
        client : A new instance of a IEC62056 client's.
    """
    BAUDRATE_CHAR = {
        300: "0",
        600: "1",
        1200: "2",
        2400: "3",
        4800: "4",
        9600: "5",
        19200: "6"
    }

    def __init__(
            self,
            baudrate: int=9600,
            port: str="/dev/ttyO3",
            device_address: str = None,
            transport: str="serial",
            parity: str="E",
            bytesize: int=7,
            stopbits: int=1,
            **kwargs):
        
        self._baudrate = baudrate
        self._port = port
        self._device_address = device_address
        self._parity = parity
        self._bytesize = bytesize
        self._stopbits = stopbits

        if transport == "serial":
            self._client = client.Iec6205621Client.with_serial_transport(
                port=self._port,
                device_address=self._device_address
            )

            if self._device_address:
                self._client.transport.TRANSPORT_REQUIRES_ADDRESS = True

        elif transport == "tcp":
            #TODO: to be implemented.
            NotImplementedError("This feature is not implemented yet.")
            self.disconnect()
        else:
            self.disconnect()
            ValueError(f"Type : {type} is not valid.")

    @property
    def baudrate(self) -> int:
        try:
            return self._client.transport.port.baudrate
        except AttributeError:
            return "undefined"
    
    @property
    def identification(self) -> str:
        try:
            return self._identification
        except AttributeError:
            return "undefined"
    
    @property
    def manufacturer(self) -> str:
        try:
            return self._manufacturer
        except AttributeError:
            return "undefined"
    
    def connect(self):
        try:
            if not self._is_connected():
                self._client.connect()
            
            self._client.transport.port.baudrate = self._baudrate
        except serial.serialutil.SerialException as err:
            raise SerialPortBusyException(f"The serial port {self._port} is not available : {err}")
        
    def _is_connected(self) -> bool:
        if self._client.transport.port is not None:
            return self._client.transport.port.is_open
        return False
    
    def disconnect(self):
        self._client.disconnect()

    def set_identification(self, identification: messages.IdentificationMessage)-> None:
        self._identification = identification.identification
        self._manufacturer = identification.manufacturer
 
    def read_identifier(self, timeout: int = 5):
        self.connect()
        identification = self.read_client_identification()
        if isinstance(identification, messages.IdentificationMessage):
            self.set_identification(identification)
            return identification
        else:
            raise MeterIdentificationFailed(f"Cannot communicate with the meter using: baudrate: {self.baudrate} | parity: {self._parity} | bytesize: {self._bytesize} | stopbits: {self._stopbits}.")

    def request(self, registers: list=[], table: str= None, timeout: int = 15) -> List[messages.DataSet]:
        """read_registers specified in the list for the requested table of the iec62056-21 meter.

        Args:
            registers (list, optional): list of registers obis code to read. Defaults to [].
            table (str, optional): table to be read. Defaults to 0 which is equivalent to a standart readout.

        Returns:
            List[messages.DataSet]: A list of Dataset element that contains the requested registers if found.
        """
        try:
            self.connect()
        except SerialPortBusyException as err:
            raise err
        try:
            identification = self.read_identifier()
            logging.info(f"[Meter.Identification] Meter Identification has been read : {identification}")        
            message = self._get_ack_message(table)
            logging.info(f"[Meter.ACK] Sending ACK Message to the meter : {message.to_representation()}")

            data = message.to_bytes()
            time.sleep(1)
            self._write(data)
            datasets, bcc = self._read(timeout=timeout)
            self.disconnect()

            if len(registers) == 0:
                return datasets
            
            return [dataset for dataset in datasets if dataset.address in registers]

        except Exception as err:
            self.disconnect()
            raise IEC62056RequestException(f"Could not read registers : {err}")

    def read_client_identification(self):
        try:
            self._client.send_init_request()
            return self._client.read_identification()
        except Exception as err:
            raise IEC62056RequestException(f"Cannot read meter idenficiation message : {err}")
    
    def _get_ack_message(self, table: str = None) -> messages.AckOptionSelectMessage:
        if table is not None:
            message = messages.AckOptionSelectMessage(
                baud_char=self.BAUDRATE_CHAR[self._baudrate],
                mode_char=table
            )
        else:
            message = messages.AckOptionSelectMessage(
            baud_char=self.BAUDRATE_CHAR[self._baudrate],
            mode_char=client.Iec6205621Client.MODE_CONTROL_CHARACTER["readout"]
        )
        return message
            
    def _write(self, data: bytes):
        print(f"--> {data}")

        self._client.transport.port.write(data)

    def _read(self, timeout: int = 10) -> Tuple(List[messages.DataSet], bytes):
        result = []
        logging.info(f"Reading meter response.")
        port: serial.Serial = self._client.transport.port
        port.timeout = timeout
        encoded = port.read_until(constants.ETX.encode())
        bcc = port.read(1)
        logging.warning(f"DATA Fetched ({len(encoded)} bytes of length and bcc = {bcc})")
        lines = encoded.decode().split('\r\n')

        for line in lines:
            try:
                # The first line contains STX character that can be removed for decoding first register.
                if line.startswith(constants.STX):
                    line = line.replace(constants.STX, '')

                if line.startswith(constants.ETX):
                    line = line.replace(constants.ETX, '')
              
                dataset = messages.DataSet.from_representation(line)
                result.append(dataset)

            except Exception as err:
                logger.warning(f"Could not decode dataset for line : {err}")
        return result, bcc
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(address : {self._device_address}, baudrate : {self._baudrate}, port: {self._port})"
    