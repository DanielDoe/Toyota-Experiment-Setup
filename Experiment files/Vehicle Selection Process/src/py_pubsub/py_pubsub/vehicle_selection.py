class VehicleSelection():
    def __init__(self, idx, location, size, objects):
        self.idx = idx
        self.location = location
        self.size = size
        self.objects = objects
        
        
    def get_all_request(self):
        requests = []
        request = {
            "ID": self.idx,
            "location": self.location,
            "size": self.size,
            "objects": self.objects
            }
        return requests.push(request)
        
         