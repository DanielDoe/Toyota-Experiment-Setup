# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
import json
import uuid
import time
import random 

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('edge_server')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.i = 0
        self.requests = []
        self.subscription  # prevent unused variable warning

    def get_all_request(self, data):  
        self.requests.append({"idx": data[0], "distance": data[1], "file_size": data[2], "objects": data[3]}) 
        self.get_logger().info(f"Queue log: {len(self.requests)}")
        return self.requests  
        
    
    def select_vehicle(self):
        server_idx = str(uuid.uuid4())
        agent = "DDPG"
        if len(self.requests) > 50: 
            for x in range(5): 
                t0 = time.time()
                self.get_logger().info("Processing started!")
                if len(self.requests) % 50 == 0:
                    temp = sorted(self.requests[self.i:self.i+10], key = lambda i: (i['distance'], i['file_size']), reverse=True)
                    data = sorted(temp, key = lambda i: i['objects'])
                    idx, distance, file_size, objects = data[0].values()
                    time.sleep(random.randint(15,35))
                    print("\n")
                    print("******************************************************************")
                    self.get_logger().info(f"\n {agent} Selection :\n server: {x},\n vehicle:{idx},\n distance: {distance},\n file_size:{file_size},\n and objects:{objects},\n decision_time: {time.time() - t0} ")
                    print("******************************************************************\n")
                    self.i = self.i+10
                
        else:
            self.get_logger().info("Need more request to start processing")
    
    def listener_callback(self, msg):
        data = msg.data.split()
        self.get_all_request(data)
        self.select_vehicle()
        #self.get_logger().info(f'"idx": {data[0]}, "distance": {data[1]}, "file_size": {data[2]}, "objects": {data[3]}')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
