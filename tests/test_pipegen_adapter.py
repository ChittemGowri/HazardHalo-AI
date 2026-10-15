import pytest
from edge_agent.pipegen_adapter import PipeGenAdapter
def test_fixture_and_malformed():
 assert len(PipeGenAdapter().parse({'detections':[{'label':'person','confidence':.9,'x':.1,'y':.1,'width':.2,'height':.3}]}))==1
 with pytest.raises(ValueError): PipeGenAdapter().parse('{}')
