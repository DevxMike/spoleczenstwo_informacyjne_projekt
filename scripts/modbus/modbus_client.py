from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('host_IP', port=5020)  
client.connect()

result = client.read_holding_registers(0, 10)
print(result.registers)

client.close()

