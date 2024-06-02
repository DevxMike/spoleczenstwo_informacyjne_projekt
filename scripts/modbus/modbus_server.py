import asyncio
import logging
import sys

from pymodbus import __version__ as pymodbus_version
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSparseDataBlock,
)
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server import (
    StartAsyncSerialServer,
    StartAsyncTcpServer,
    StartAsyncTlsServer,
    StartAsyncUdpServer,
)

# Konfiguracja pamięci Modbus z przykładowymi danymi
block = ModbusSequentialDataBlock(0x00, [0] * 100)
store = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
context = ModbusServerContext(slaves=store, single=True)

# Uruchomienie serwera Modbus TCP/IP
async def run_server():
    server = await StartAsyncTcpServer(context, address=("0.0.0.0", 5020))
    await server.serve_forever()

asyncio.run(run_server())

