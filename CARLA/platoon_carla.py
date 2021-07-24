
import glob
import os
import sys
import numpy as np

import random
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla



actor_list = []
try:

    

    client = carla.Client('localhost', 2000)
    traffic_manager = client.get_trafficmanager(8000)
    traffic_manager.set_global_distance_to_leading_vehicle(1.0)
    traffic_manager.set_hybrid_physics_mode(True)
    traffic_manager.set_synchronous_mode(True)
    client.set_timeout(5.0)
    
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    bp = blueprint_library.filter('cybertruck')[0]# leading vehicle
    bp1 = blueprint_library.filter('cybertruck')[0] # following vehilce
    bp2 = blueprint_library.filter('cybertruck')[0] # another following vehicle

    transform1 = carla.Transform(carla.Location(x = -7.530004, y = 135, z = 0.5), carla.Rotation(pitch = 0.0,yaw = 89.99954,roll = 0.0))
    transform2 = carla.Transform(carla.Location(x = -7.530004, y = 125, z = 0.5), carla.Rotation(pitch = 0.0,yaw = 89.99954,roll = 0.0))
    transform3 = carla.Transform(carla.Location(x = -7.530004, y = 115, z = 0.5), carla.Rotation(pitch = 0.0,yaw = 89.99954,roll = 0.0))
    
    throt1 = 1.0;
    brake1 = 0.0;
    vehicle = world.spawn_actor(bp, transform1)
    vehicle1 = world.spawn_actor(bp1, transform2)
    vehicle2 = world.spawn_actor(bp2, transform3)
    vehicle.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    vehicle1.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    vehicle2.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    vehicle.set_autopilot(True, traffic_manager.get_port())
    
    actor_list.append(vehicle)
    actor_list.append(vehicle1)
    actor_list.append(vehicle2)
    # sleep for 9 seconds, then finish:
    time.sleep(9)
    #throt1 = 0.0;
    #brake1 = 1.0;
    vehicle.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    vehicle1.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    vehicle2.apply_control(carla.VehicleControl(throttle = throt1, steer = 0,brake = brake1))
    #print(vehicle.get_location);
    time.sleep(5)   
    
finally:

    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')