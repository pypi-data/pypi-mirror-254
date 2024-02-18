
        
class MetaData:
    def __init__(self, data) -> None:
        self.metadata = data.get('metadata', {})
        self.markets = data.get('markets', {})
        self.indopc = data.get('indopc', {})
        self.bdi_id = data.get('bdi_id', {})
        self.corrections = data.get('corrections', {})

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def add_market(self, key, value):
        self.markets[key] = value

    def add_indopc(self, key, value):
        self.indopc[key] = value

    def add_bdi_id(self, key, value):
        self.codbdi[key] = value
    
    def add_corrections(self, key, value):
        self.corrections[key] = value
