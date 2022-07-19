# Python Module vehicle_data

import random 
import uuid

server_idx = []
for x in range(5): 
    idx = str(uuid.uuid4())
    server_idx.append(idx)

for x in range(len(server_idx)):
    print(server_idx[x])
     
# def fetch_data():
#     idx = str(uuid.uuid4())
#     size = random.uniform(100, 300)
#     distance = random.uniform(0,100)
#     objects = random.randint(0, 10)
    
#     return [
#         idx,
#         size,
#         distance,
#         objects
#     ] 
    
# def fetch_data():
#     server_idx = str(uuid.uuid4())
#     vehicle_idx = str(uuid.uuid4())
#     image_size = random.uniform(100, 300)
#     distance = random.uniform(0,100)
#     objects = random.randint(0, 10)
    
#     return [
#         server_idx,
#         vehicle_idx,
#         image_size,
#         distance,
#         objects
#     ]    