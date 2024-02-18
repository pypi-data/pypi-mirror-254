"""
Ensure you have a modbus slave available with specified parameters for this test.
( I used pyModSlave )
"""
import asyncio
import time

from iot_protocols.modbus import ModbusClient, AsyncModbusClient, request_factory, requests, ModbusSerial, ModbusTCP

RCS={
        "function": "ReadCoils",
        "unit": 1,
        "address": 5,
        "count": 4
    }
WCS={
        "function": "WriteCoils",
        "unit": 1,
        "address": 5,
        "values": [True]*5
    }
RDI={
        "function": "ReadDiscreteInput",
        "unit": 1,
        "address": 0,
        "count": 5
    }
RIR={
        "function": "ReadInputRegister",
        "unit": 1,
        "address": 10,
        "count": 3,
        "encoding": "int64"
    }
RHR={
        "function": "ReadHoldingRegister",
        "unit": 1,
        "address": 1,
        "count": 3,
        "encoding": "int64"
    }

SERIAL_CLIENT = ModbusClient.with_serial_client(
        port="COM11",
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=5
    )
TCP_CLIENT = ModbusClient.with_tcp_client(
        host="127.0.0.1",
        port=502
    )

COILS = [True, False, True, False, True]
DI = [not c for c in COILS]
IR = [28,11,1996]
HR = [28,11,1996]



def test_moxa_r12r14():
    from colorama import Fore, Back, Style, init
    init()
    client = ModbusSerial(
        port="COM3",
        parity="N",
        bytesize=8
    )

    def set_light(g, y, r):
        client.request(requests.WriteCoils(address=320, values = [g, y, r], unit=1))
    
    def read_light() -> tuple:
        def display_light(bits: tuple):
            GREEN = f"{Fore.GREEN}ON" if bits[0] else f"{Fore.LIGHTBLACK_EX}OFF"
            YELLOW = f"{Fore.YELLOW}ON" if bits[1] else f"{Fore.LIGHTBLACK_EX}OFF"
            RED = f"{Fore.RED}ON" if bits[2] else f"{Fore.LIGHTBLACK_EX}OFF"
            return f"( {GREEN} {YELLOW} {RED} {Style.RESET_ALL})"
        
        bits = client.request(requests.ReadCoils(address=320, count=6, unit=1))
        print(display_light(tuple(bits[0:3])))
        return tuple(map(lambda b: "ON" if b==True else "OFF", bits[0:3]))
    # Write to coils RLY:
    print("Set all OFF")
    set_light(0,0,0)
    time.sleep(2)
    print("Set GREEN ON")
    set_light(1,0,0)
    read_light()
    time.sleep(2)

    print("Set YELLOW ON")
    set_light(1,1,0)
    read_light()
    time.sleep(2)

    print("Set RED ON")
    set_light(1,1,1)
    read_light()
    time.sleep(2)

    print("Set GREEN OF")
    set_light(0,1,1)
    read_light()
    time.sleep(2)

    print("Set YELLOW OFF")
    set_light(0,0,1)
    read_light()
    time.sleep(2)

    print("Set RED OFF")
    set_light(0,0,0)
    read_light()
    time.sleep(2)


test_moxa_r12r14()