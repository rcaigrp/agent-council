# Synchronization Engine

class SyncEngine:
    def __init__(self):
        self.devices = {}
        
    def register_device(self, device_id):
        self.devices[device_id] = []
        
    def sync_data(self, device_id, data):
        if device_id in self.devices:
            self.devices[device_id].append(data)
            return True
        return False