from collections.abc import Sequence

from pymodbus.bit_read_message import ReadCoilsResponse, ReadDiscreteInputsResponse
from pymodbus.register_read_message import ReadHoldingRegistersResponse, ReadInputRegistersResponse

from iot_protocols.modbus.exceptions import ModbusResponseException

class ReadCoilsResponse(Sequence):

    def __init__(self, response: ReadCoilsResponse, size: int):
        self._response = response
        self._is_error = response.isError()
        self._size = size

        super().__init__()

    def __getitem__(self, i: int):
        if not self._is_error:
            return self._response.bits[0:self._size]
        else:
            raise ModbusResponseException(f"The response is in Error: {self._response}")
    
    def __len__(self) -> int:
        if self._is_error:
            return 0
        
        return len(self._response.bits)

    def isError(self) -> bool:
        return self._is_error