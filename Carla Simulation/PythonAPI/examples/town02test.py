import glob
import os
import sys
import time

import carla

client = carla.Client("localhost", 2000)
client.set_timeout(2.0)
world = client.load_world('Town02')

blueprint_library = world.get_blueprint_library()
bp = blueprint_library.filter("model3")[0]
world = client.get_world()
spawnPoint=carla.Transform(carla.Location(x=38.6,y=5.8, z=0.598),carla.Rotation(pitch=0.0, yaw=0.0, roll=0.000000))
vehicle = world.spawn_actor(bp, spawnPoint)
time.sleep(1000)
vehicle.destroy()