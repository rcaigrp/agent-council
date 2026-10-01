class SyncEngine:
    def __init__(self):
        # In-memory storage for now - will be replaced with database
        self.synced_data = []
        
    def sync_data(self, data):
        # Simulate data synchronization
        self.synced_data.append(data)
        
    def get_synced_data(self):
        return self.synced_data
