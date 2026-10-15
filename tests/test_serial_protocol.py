import pytest
from edge_agent.serial_bridge import SerialProtocol
def test_protocol():
 assert SerialProtocol.alert('abc')==b'ALERT|abc\n'; assert SerialProtocol.parse('ACK|CLEAR\n')=='ACK|CLEAR'
 with pytest.raises(ValueError): SerialProtocol.parse('DANGER')
