# Sync Engine for Travel Itinerary Planner

class SyncEngine:
    def __init__(self):
        self.devices = {}
        self.data_store = {}
        
    def register_device(self, device_id):
        if device_id not in self.devices:
            self.devices[device_id] = {
                'last_sync': 0,
                'data_version': 0
            }
            
    def sync_itinerary(self, device_id, itinerary_data, timestamp):
        # Validate device registration
        if device_id not in self.devices:
            raise ValueError(f'Device {device_id} not registered')
            
        # Check for conflicts with existing data
        conflicts = self._detect_conflicts(device_id, itinerary_data)
        
        # Resolve conflicts (simple timestamp-based resolution for now)
        resolved_data = self._resolve_conflicts(conflicts, itinerary_data)
        
        # Update device state and store data
        self.devices[device_id]['last_sync'] = timestamp
        self.data_store[itinerary_data['id']] = {
            'data': resolved_data,
            'version': self.devices[device_id]['data_version'] + 1,
            'timestamp': timestamp
        }
        
        return {
            'status': 'synced',
            'conflicts_resolved': len(conflicts),
            'data_version': self.data_store[itinerary_data['id']]['version']
        }
        
    def _detect_conflicts(self, device_id, new_data):
        # Simple conflict detection based on data modification times
        conflicts = []
        if new_data['id'] in self.data_store:
            existing = self.data_store[new_data['id']]
            if existing['timestamp'] > new_data.get('last_modified', 0):
                conflicts.append({
                    'type': 'timestamp_conflict',
                    'existing_timestamp': existing['timestamp'],
                    'new_timestamp': new_data.get('last_modified', 0)
                })
        return conflicts
        
    def _resolve_conflicts(self, conflicts, new_data):
        # For now just accept the newer data
        if conflicts:
            print(f"Conflicts detected: {len(conflicts)} - resolving with newer data")
        return new_data