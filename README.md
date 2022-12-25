# autonomius_navigation_project_2022w
2022冬学期 智能移动机器人大作业
## 1 导航算法
W.I.P
## 2 运行方式
### 2.1 python虚拟环境搭建
为了更方便进行库管理，首先需要搭建python虚拟环境，python自带的venv或者conda环境均可，下面以venv为例：
```bash
sudo apt -y update
sudo apt-get -y install python3-venv
python3 -m venv ~/nav_challenge
export PATH="~/nav_challenge/bin:$PATH"
```
然后激活虚拟环境：
```bash
source ~/nav_challenge/bin/activate
```
安装下列需要的库：
```bash
pip3 install defusedxml rospkg netifaces numpy pyyaml scipy torch==1.7 torchvision==0.8 tensorboard
```
### 2.2 安装ros包依赖
进入工作区，运行：
```bash
source /opt/ros/noetic/setup.bash
rosdep init 
rosdep update
rosdep install -y --from-paths . --ignore-src --rosdistro=noetic
```
### 2.3 构建环境
```bash
catkin_make
source ./devel/setup.bash(.zsh)
```
### 2.4 运行
单独测试（打开gui界面）：
```bash
cd src/scripts
sudo chmod +x ./run.py
python3 run.py --gui --world_idx 0
```
在多张地图中进行测试：
```bash
cd src/scripts
sudo chmod +x test.sh
./test.sh
```