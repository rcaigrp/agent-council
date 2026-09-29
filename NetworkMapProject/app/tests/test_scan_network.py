import sys, os
# Add project root to PYTHONPATH so that 'app' package can be imported
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from app.utils.scan_network import scan_network

def test_scan_returns_list():
    result = scan_network()
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, dict)
        assert 'ip' in item
