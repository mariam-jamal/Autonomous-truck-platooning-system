

# ==============================================================================
# -- find carla module ---------------------------------------------------------
# ==============================================================================


import glob
import os
import sys
import numpy as np

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla

import random
import time
import numpy as np
import cv2

im_width = 640
im_height = 480


def process_img(image):
    i = np.array(image.raw_data)
    i2 = i.reshape((im_height, im_width, 4))
    i3 = i2[:, :, :3]
    cv2.imshow("", i3)
    cv2.waitKey(1)
    return i3/255.0


actor_list = []
try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(10)

    world = client.load_world('Town02_opt')
    
    world.unload_map_layer(carla.MapLayer.All   )
    blueprint_library = world.get_blueprint_library()

    
    time.sleep(5)

finally:

    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')