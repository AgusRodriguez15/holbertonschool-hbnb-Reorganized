from IPersistenceManager import IPersistenceManager
import uuid

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_storage = {}

    def save(self, entity):
        entity_id = uuid.uuid4()
        self.data_storage[entity_id] = entity
        return entity_id
    
    def get(self, entity_id, entity_type):
        entity = self.data_storage.get(entity_id)
        if entity_type == type(entity):
            return entity
        return None

    def update(self, entity):
        if entity.id in self.data_storage:
            self.data_storage[entity.id] = entity
            return entity
        return None
    
    def delete(self, entity_id, entity_type):
        entity = self.data_storage.get(entity_id)
        if entity and isinstance(entity, entity_type):
            return self.data_storage.pop(entity_id, None)
        return None
