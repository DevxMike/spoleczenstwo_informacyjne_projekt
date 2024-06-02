import asyncio
import logging
import sys
import pymodbus.client as modbus_async_client
from pymodbus.exceptions import ModbusException

async def run_modbus_client():
    client = modbus_async_client.ModbusTcpClient('127.0.0.1', port=5020)

    try:
        client.connect()

        rr_coils = client.read_coils(0, 10)  
        rr_registers = client.read_holding_registers(0, 10) 
        
        print("Odczytane I/O: ", rr_coils.bits)
        print("Odczytane rejestry przed ustawieniem: ", rr_registers.registers)

        write_registers = [i for i in range(10)]
        client.write_registers(0, write_registers)
        rr_registers_after = client.read_holding_registers(0, 10)
        print("Odczytane rejestry po ustawieniu: ", rr_registers_after.registers)

    except ModbusException as e:
        print("Błąd Modbus:", e)

    finally:
        client.close()

async def main():
    await run_modbus_client()

if __name__ == "__main__":
    asyncio.run(main())
