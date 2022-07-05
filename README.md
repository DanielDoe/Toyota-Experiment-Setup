Getting started and documentation
===============

## Carla Environment Setup

CARLA is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and
validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings,
vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites and
environmental conditions.

![CARLA Video](Docs/img/video_thumbnail_0910.jpg)
### Recommended system

* Intel i7 gen 9th - 11th / Intel i9 gen 9th - 11th / AMD ryzen 7 / AMD ryzen 9
* +16 GB RAM memory 
* NVIDIA RTX 2070 / NVIDIA RTX 2080 / NVIDIA RTX 3070, NVIDIA RTX 3080
* Ubuntu 18.04

## CARLA Ecosystem
Repositories associated to the CARLA simulation platform:

* [**CARLA Autonomous Driving leaderboard**](https://leaderboard.carla.org/): Automatic platform to validate Autonomous Driving stacks
* [**Scenario_Runner**](https://github.com/carla-simulator/scenario_runner): Engine to execute traffic scenarios in CARLA 0.9.X
* [**ROS-bridge**](https://github.com/carla-simulator/ros-bridge): Interface to connect CARLA 0.9.X to ROS
* [**Driving-benchmarks**](https://github.com/carla-simulator/driving-benchmarks): Benchmark tools for Autonomous Driving tasks
* [**Conditional Imitation-Learning**](https://github.com/felipecode/coiltraine): Training and testing Conditional Imitation Learning models in CARLA
* [**AutoWare AV stack**](https://github.com/carla-simulator/carla-autoware): Bridge to connect AutoWare AV stack to CARLA
* [**Reinforcement-Learning**](https://github.com/carla-simulator/reinforcement-learning): Code for running Conditional Reinforcement Learning models in CARLA
* [**Map Editor**](https://github.com/carla-simulator/carla-map-editor): Standalone GUI application to enhance RoadRunner maps with traffic lights and traffic signs information



Building CARLA
--------------

Use `git clone` or download the project from this page. Note that the master branch contains the most recent release of CARLA with the latest fixes and features.

Then follow the instruction at [How to build on Linux][buildlinuxlink] or [How to build on Windows][buildwindowslink].  
The Linux build needs for an UE patch to solve some visualization issues regarding Vulkan. Those already working with a Linux build should install the patch and make the UE build again using the following commands.  
```sh
# Download and install the UE patch  
cd ~/UnrealEngine_4.24
wget https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/UE_Patch/430667-13636743-patch.txt ~/430667-13636743-patch.txt
patch --strip=4 < ~/430667-13636743-patch.txt
# Build UE
./Setup.sh && ./GenerateProjectFiles.sh && make
```

Unfortunately we don't have official instructions to build on Mac yet, please check the progress at [issue #150][issue150].

[buildlinuxlink]: https://carla.readthedocs.io/en/latest/build_linux/
[buildwindowslink]: https://carla.readthedocs.io/en/latest/build_windows/
[issue150]: https://github.com/carla-simulator/carla/issues/150

Debian CARLA installation
--------------
The Debain package is available for both Ubuntu 18.04 and Ubuntu 20.04, however the officially supported platform is Ubuntu 18.04.

1. Set up the Debian repository in the system:

```sh
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9
sudo add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla $(lsb_release -sc) main"
```

2. Install CARLA and check for the installation in the /opt/ folder:

```sh
sudo apt-get update # Update the Debian package index
sudo apt-get install carla-simulator # Install the latest CARLA version, or update the current installation
cd /opt/carla-simulator # Open the folder where CARLA is installed
```
This repository contains CARLA 0.9.10 and later versions. To install a specific version add the version tag to the installation command:

```sh
apt-cache madison carla-simulator # List the available versions of Carla
sudo apt-get install carla-simulator=0.9.10-1 # In this case, "0.9.10" refers to a CARLA version, and "1" to the Debian revision
```
Now, let's get started to run carla simulator

```sh
# Start carla environment
cd ~/[carla env directory] # e.g., cd /opt/carla-simulator/
./CarlaUE4.sh
```
This command should display the carlar world simulation as shown below

![CARLA Video](Docs/img/carla_env.png)

To interact with carla environment, spawn some objects that can be found in the `[carla env directory]/PythonAPI/examples`, you can also generate a random traffic on the system by running `python3 generate_traffic.py`.

```sh
# Start carla environment
cd ~/[carla env directory] # e.g., cd /opt/carla-simulator/
./CarlaUE4.sh

# Open a different terminal, then run
cd ~/[carla env directory]/PythonAPI/examples
python3 generate_traffic.py # you should see moving vehicles

# Open another terminal and run
python manual_control.py # for a manual control vehicle
# OR
python automatic_control.py # for an automatic control vehicle
```

ROS/ROS2 bridge for CARLA simulator
--------------
This ROS package is a bridge that enables two-way communication between ROS and CARLA. The information from the CARLA server is translated to ROS topics. In the same way, the messages sent between nodes in ROS get translated to commands to be applied in CARLA.

![rviz setup](Docs/img/ad_demo.png "AD Demo")

**This version requires CARLA 0.9.12**

## Features

- Provide Sensor Data (Lidar, Semantic lidar, Cameras (depth, segmentation, rgb, dvs), GNSS, Radar, IMU)
- Provide Object Data (Transforms (via [tf](http://wiki.ros.org/tf)), Traffic light status, Visualization markers, Collision, Lane invasion)
- Control AD Agents (Steer/Throttle/Brake)
- Control CARLA (Play/pause simulation, Set simulation parameters)

## ROS Bridge Installation

Installation instructions and further documentation of the ROS bridge and additional packages are found [__here__](https://carla.readthedocs.io/projects/ros-bridge/en/latest/).

After installing ros-bridge, run the following code to start our carla ros-bridge implementation.
```sh
# Start carla environment
cd ~/[carla env directory] # e.g., cd /opt/carla-simulator/
./CarlaUE4.sh

# Open another terminal to start ros bridge
cd ~/[ros-bridge directory] # e.g., cd ~/carla-ros-bridge/
source install/setup.bash
ros2 launch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch.py spawn_point_ego_vehicle:="spawn_point_hero0"
```

This should spawn a vehicle that would interact with your carla environment that looks like this.

![ros_bridge setup](Docs/img/ros_bridge.png "Ros_Bridge")

The spawn object actively records sensor data to be transmitted to a server address of your choice. 

## Getting started with data collection

You can either collect carla data locally or over specified connection. To record data locally, run the following commands
```sh
# Start carla environment
cd ~/[carla env directory] # e.g., cd /opt/carla-simulator/
./CarlaUE4.sh

# Open a different terminal, then run
cd ~/[carla env directory]/PythonAPI/examples
python3 generate_traffic.py # you should see moving vehicles

# Open another terminal and run
python record_datas.py # for a manual control vehicle with data recording
```
To record data using carla ros bridge, kindly see the documentation [__here__](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html) to help you setup a  ROS2 subscribe and publish protocol for your ros vehicle and your preferred destination address. 

_CARLA: An Open Urban Driving Simulator_<br>Alexey Dosovitskiy, German Ros,
Felipe Codevilla, Antonio Lopez, Vladlen Koltun; PMLR 78:1-16
[[PDF](http://proceedings.mlr.press/v78/dosovitskiy17a/dosovitskiy17a.pdf)]


```
@inproceedings{Dosovitskiy17,
  title = {{CARLA}: {An} Open Urban Driving Simulator},
  author = {Alexey Dosovitskiy and German Ros and Felipe Codevilla and Antonio Lopez and Vladlen Koltun},
  booktitle = {Proceedings of the 1st Annual Conference on Robot Learning},
  pages = {1--16},
  year = {2017}
}
```

## Yolo HD image optimization setup
Internship stuff based on yolox from [YOLOX github](https://github.com/Megvii-BaseDetection/YOLOX)

#### Standard Models.

|Model |size |mAP<sup>val<br>0.5:0.95 |mAP<sup>test<br>0.5:0.95 | Speed V100<br>(ms) | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:    | :---:       |:---:     |:---:  | :---: | :----: |
|[YOLOX-s](./exps/default/yolox_s.py)    |640  |40.5 |40.5      |9.8      |9.0 | 26.8 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth) |
|[YOLOX-m](./exps/default/yolox_m.py)    |640  |46.9 |47.2      |12.3     |25.3 |73.8| [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_m.pth) |
|[YOLOX-l](./exps/default/yolox_l.py)    |640  |49.7 |50.1      |14.5     |54.2| 155.6 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_l.pth) |
|[YOLOX-x](./exps/default/yolox_x.py)   |640   |51.1 |**51.5**  | 17.3    |99.1 |281.9 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_x.pth) |
|[YOLOX-Darknet53](./exps/default/yolov3.py)   |640  | 47.7 | 48.0 | 11.1 |63.7 | 185.3 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_darknet.pth) |


### Legacy models

|Model |size |mAP<sup>test<br>0.5:0.95 | Speed V100<br>(ms) | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:       |:---:     |:---:  | :---: | :----: |
|[YOLOX-s](./exps/default/yolox_s.py)    |640  |39.6      |9.8     |9.0 | 26.8 | [onedrive](https://megvii-my.sharepoint.cn/:u:/g/personal/gezheng_megvii_com/EW62gmO2vnNNs5npxjzunVwB9p307qqygaCkXdTO88BLUg?e=NMTQYw)/[github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_s.pth) |
|[YOLOX-m](./exps/default/yolox_m.py)    |640  |46.4      |12.3     |25.3 |73.8| [onedrive](https://megvii-my.sharepoint.cn/:u:/g/personal/gezheng_megvii_com/ERMTP7VFqrVBrXKMU7Vl4TcBQs0SUeCT7kvc-JdIbej4tQ?e=1MDo9y)/[github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_m.pth) |
|[YOLOX-l](./exps/default/yolox_l.py)    |640  |50.0  |14.5 |54.2| 155.6 | [onedrive](https://megvii-my.sharepoint.cn/:u:/g/personal/gezheng_megvii_com/EWA8w_IEOzBKvuueBqfaZh0BeoG5sVzR-XYbOJO4YlOkRw?e=wHWOBE)/[github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_l.pth) |
|[YOLOX-x](./exps/default/yolox_x.py)   |640  |**51.2**      | 17.3 |99.1 |281.9 | [onedrive](https://megvii-my.sharepoint.cn/:u:/g/personal/gezheng_megvii_com/EdgVPHBziOVBtGAXHfeHI5kBza0q9yyueMGdT0wXZfI1rQ?e=tABO5u)/[github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_x.pth) |
|[YOLOX-Darknet53](./exps/default/yolov3.py)   |640  | 47.4      | 11.1 |63.7 | 185.3 | [onedrive](https://megvii-my.sharepoint.cn/:u:/g/personal/gezheng_megvii_com/EZ-MV1r_fMFPkPrNjvbJEMoBLOLAnXH-XKEB77w8LhXL6Q?e=mf6wOc)/[github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_darknet53.pth) |


#### Light Models.

|Model |size |mAP<sup>val<br>0.5:0.95 | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---:  |  :---:       |:---:     |:---:  | :---: |
|[YOLOX-Nano](./exps/default/nano.py) |416  |25.8  | 0.91 |1.08 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth) |
|[YOLOX-Tiny](./exps/default/yolox_tiny.py) |416  |32.8 | 5.06 |6.45 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_tiny.pth) |



Legacy models

|Model |size |mAP<sup>val<br>0.5:0.95 | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---:  |  :---:       |:---:     |:---:  | :---: |
|[YOLOX-Nano](./exps/default/nano.py) |416  |25.3  | 0.91 |1.08 | [github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_nano.pth) |
|[YOLOX-Tiny](./exps/default/yolox_tiny.py) |416  |32.8 | 5.06 |6.45 | [github](https://github.com/Megvii-BaseDetection/storage/releases/download/0.0.1/yolox_tiny_32dot8.pth) |


## Quick Start
### Installation

Step1. Install YOLOX.
```shell
git clone https://github.com/DanielDoe/hd-map-optimization.git or git@github.com:DanielDoe/hd-map-optimization.git
cd hd-map-optimization
username: DanielDoe
password: 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
pip3 install -U pip && pip3 install -r requirements.txt
pip3 install -v -e .  # or  python3 setup.py develop
```

Step2. Install [pycocotools](https://github.com/cocodataset/cocoapi).

```shell
pip3 install cython; pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```



### Demo

[x] The crop function is implemented at the utils/visualize.py

[x] The image to downsample is the img variable

Step1. Download a pretrained model from the benchmark table.

Step2. Use either -n or -f to specify your detector's config. For example:

Change the image here to view1 or 2 or 3 or 4 for road maps
```shell
python tools/demo.py image -n yolox-s -c /path/to/your/yolox_s.pth --path assets/dog.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [cpu/gpu]
```
or
```shell
python tools/demo.py image -f exps/default/yolox_s.py -c /path/to/your/yolox_s.pth --path assets/dog.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [cpu/gpu]
```
Demo for video:
```shell
python tools/demo.py video -n yolox-s -c /path/to/your/yolox_s.pth --path /path/to/your/video --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [cpu/gpu]
```

Step 1.

Run Carla simulation to collect the data needed for the HD map, optimization step. The image below is a brief explanation on the use case of carla for the yolo:

![rviz setup](Docs/img/map_process.jpg "AD Demo")


Running the `yolo` commands on images obtained from carla simulation, you should obtain the optimized HD map as shown below:

![rviz setup](Docs/img/image_optimization.jpg "AD Demo")



## Cite YOLOX
If you use YOLOX in your research, please cite our work by using the following BibTeX entry:

```latex
 @article{yolox2021,
  title={YOLOX: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```

Licenses
-------

#### CARLA licenses

CARLA specific code is distributed under MIT License.

CARLA specific assets are distributed under CC-BY License.

#### CARLA Dependency and Integration licenses

The ad-rss-lib library compiled and linked by the [RSS Integration build variant](Docs/adv_rss.md) introduces [LGPL-2.1-only License](https://opensource.org/licenses/LGPL-2.1).

Unreal Engine 4 follows its [own license terms](https://www.unrealengine.com/en-US/faq).

CARLA uses three dependencies as part of the SUMO integration:
- [PROJ](https://proj.org/), a generic coordinate transformation software which uses the [X/MIT open source license](https://proj.org/about.html#license).
- [SQLite](https://www.sqlite.org), part of the PROJ dependencies, which is [in the public domain](https://www.sqlite.org/purchase/license).
- [Xerces-C](https://xerces.apache.org/xerces-c/), a validating XML parser, which is made available under the [Apache Software License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

CARLA uses one dependency as part of the Chrono integration:
- [Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page), a C++ template library for linear algebra which uses the [MPL2 license](https://www.mozilla.org/en-US/MPL/2.0/).

CARLA uses the Autodesk FBX SDK for converting FBX to OBJ in the import process of maps. This step is optional, and the SDK is located [here](https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2020-0)

This software contains Autodesk® FBX® code developed by Autodesk, Inc. Copyright 2020 Autodesk, Inc. All rights, reserved. Such code is provided "as is" and Autodesk, Inc. disclaims any and all warranties, whether express or implied, including without limitation the implied warranties of merchantability, fitness for a particular purpose or non-infringement of third party rights. In no event shall Autodesk, Inc. be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of such code."
  
  ## Vehicle selection process
OpenAI's `gym` is a fantastic tool for creating custom reinforcement learning agents. It includes a number of pre-built environments, such as CartPole and MountainCar, as well as a plethora of free Atari games to play with.

These environments are excellent for learning, but we eventually want to set up an agent to solve a specific problem (vehicle selection for HD map update). To accomplish this, we must first create a custom environment tailored to our problem domain. We will later build a custom vehicle-server environment to simulate the vehicle selection process.

Let us begin by learning what an environment is. An environment contains all of the functionality required to run an agent and allow it to learn. The following gym interface must be implemented in each environment:

```shell
import gym
from gym import spaces

class CustomEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, arg1, arg2, ...):
    super(CustomEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    ...
  def reset(self):
    # Reset the state of the environment to an initial state
    ...
  def render(self, mode='human', close=False):
    # Render the environment to the screen
    ...
```

In the constructor, we first define the type and shape of our action space, which will contain all of the actions that an agent can perform in its environment. Similarly, we will define the observation space, which will contain all of the environment's data that the agent will observe.

Our reset method will be called on a regular basis to return the environment to its initial state. This is followed by a series of steps through the environment, where the model will provide action and must be executed, and the subsequent observation returned. This is also the location where rewards are computed; more on that later.

Finally, the render method can be called on a regular basis to print a representation of the environment. This function call could be as simple as a print statement or as complex as OpenGL rendering of a 3D environment. We'll stick with print statements for this example.

#### Vehicle-Server Environment
To demonstrate how this all works, we will create a vehicle-server environment. We will then train our agent to select the optimal vehicle-server pair within the environment for HD map updates. Let’s get started!

We must first consider how a server perceives its surroundings. What observations would it make prior to deciding on a vehicle to use for our HD map updates?

A server would most likely examine a vehicle information action chart, which could be overlaid with a number of technical indicators. It would then combine this visual information with their prior knowledge of similar vehicle actions to determine which vehicle is most likely to be chosen.

Let us now translate this into how our agent should perceive its surroundings.

![observation_space](Docs/img/observation_space.jpg "observation_space")

Our `observation space` includes all of the input variables that we want our agent to consider before making a decision. In this example, we want our agent to "see" the vehicle-server data points from our Carla datasets `(vehicle location, server location, image size, detected objects)`.

The intuition here is that we want our agent to consider the vehicle-server pair's actions leading up to the current system latency for each time step in order to make an informed decision for the next action.

Once a server has assessed its surroundings, it must take action. In the case of our agent, its `action space` will have three options: `pairing a vehicle and a server, unpairing a vehicle and a server, or doing nothing`.

But this isn't enough; we also need to know how many of a given vehicle pair with or unpair from the server each time. We can create an action space with a discrete number of `action types (pair, unpair, and hold)` and a continuous spectrum of amounts to pair and unpair using the gym's Box space.

You'll notice that the amount isn't required for the hold action but is provided anyway. Our agent is unaware of this at first, but should learn that the amount is unnecessary for this action over time.

![observation_space](Docs/img/reward.jpg "observation_space")

The reward is the last thing to consider before implementing our environment. We'd like to reduce the `latency of our vehicle-server selection process`. We will set the reward at each time step to be equal to the time it takes to make a vehicle-server selection decision multiplied by some fraction of the total number of time steps.

The goal is to delay rewarding the agent too quickly in the early stages, allowing it to explore sufficiently before optimizing a single strategy too deeply. It will also reward agents who maintain a lower latency for a longer period of time rather than those who reduce latency quickly using unsustainable strategies.

#### Implementation
It's time to put our environment into action now that we've defined our `observation space, action space, and rewards`. First, in the environment's constructor, we must define the action space and observation space. The environment expects a pandas data frame containing the stock data to be learned from to be passed in.

```shell
class VehicleServerEnvironment(gym.Env):
  """A vehicle server environment for OpenAI gym"""
  metadata = {'render.modes': ['human']}
  def __init__(self, df):
    super(VehicleServerEnv, self).__init__()
    self.df = df
    self.reward_range = (0, MAX_LATENCY) 
    # Actions of the format pair x%, unpair x%, Hold, etc.
    self.action_space = spaces.Box(
      low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)
    # Prices contains the OHCL values for the last five prices
    self.observation_space = spaces.Box(
      low=0, high=1, shape=(6, 6), dtype=np.float16)
```
Next, we'll write the reset method, which is called whenever a new environment is created or to reset the state of an existing environment. We'll set each agent's start time and initialize its open positions to an empty list here.

```shell
def reset(self):
  # Reset the state of the environment to an initial state
  self.latency = INITIAL_LATENCY
  self.total_latency = INITIAL_LATENCY
  self.max_latency = INITIAL_LATENCY
  self.vehicles_held = 0
  self.time_basis = 0
  self.total_vehicles_unpaired = 0
  self.total_unpair_vehicles = 0
 
  # Set the current step to a random point within the data frame
  self.current_step = random.randint(0, len(self.df.loc[:, 'Open'].values) - 6)
  return self._next_observation()
```
We set the current step to a random point within the data frame, because it essentially gives our agent’s more unique experiences from the same data set. The `_next_observation` method compiles the stock data for the last five time steps, appends the agent’s latency information, and scales all the values to between 0 and 1.

```shell
def _next_observation(self):
  # Get the data points for the last 5 days and scale to between 0-1
  frame = np.array([
    self.df.loc[self.current_step: self.current_step +
                5, 'vehicle_location'].values,
    self.df.loc[self.current_step: self.current_step +
                5, 'server_location'].values,
    self.df.loc[self.current_step: self.current_step +
                5, 'image_size'].values,
    self.df.loc[self.current_step: self.current_step +
                5, 'detected_objects'].values
   ])
  # Append additional data and scale each value to between 0-1
  obs = np.append(frame, [[
    self.latency / MAX_LATENCY,
    self.max_total_latency / MAX_LATENCY,
    self.vehicle_pair / MAX_NUM_VEHICLE,
    self.time_basis / MAX_NUM_VEHICLE,
    self.total_vehicle_unpair / MAX_NUM_VEHICLE,
  ]], axis=0)
  return obs
```
#### Results
![convergence](Docs/img/convergence.jpg "convergence_result")

![convergence_1](Docs/img/convergence_1.jpg "convergence_1_result")

![learning_rate](Docs/img/lr_latency.jpg "lr_latency_result")

![convergStorage](Docs/img/storage_size.jpg "storage")