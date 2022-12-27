# autonomius_navigation_project_2022w
2022冬学期 智能移动机器人大作业
![](demo/demo.gif)
## 0 代码结构与分工
此次作业由陈俊豪和田娅斌两人共同完成，贡献基本各占50%。

代码结构如下：
- eband_local_planner：ROS内置包
- hallucination：主要代码实现部分，LfH算法（[参考文献](https://ieeexplore.ieee.org/abstract/document/9636402)，[参考代码](https://github.com/Daffan/nav-competition-icra2022/tree/LfH)）
  - data：不同最大速度下的数据集
  - ego_timer：Ego_planner
  - interesting_models：存放训练练好的模型权重
  - LfD2D/3D：分别对应2D导航和3D导航时运动规划器模型及训练
  - LfH：训练hallucination函数
- jackal
- jackal_desktop
- jackal_helper
- jackal_simulator
- res
- rviz_tool：可视化部分代码
- scripts
## 1 导航算法：Learn from Hallucination
算法原理如下：
- 在自由空间中使用随机策略$\pi$收集自由空间中的运动规划$(p, c_c, c_g)$，得到运动规划数据集$P$；
- 通过编码器-解码器方式学习参数$\psi^*$，得到对应的幻觉函数$g_{\psi^*}(p|c_c, c_g)$；
- 对于$P$中的每个数据$(p, c_c, c_g)$，从$g_{\psi^*}(p|c_c, c_g)$中随机采样障碍物$C_{obst}$，将数据$(C_{obst}, p, c_c, c_g)$加入训练数据集$D_{train}$；
- 利用训练数据学习运动规划器$f_{\theta}(\cdot )$

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
单独测试
- 打开gazebo gui，加上--gui
- 打开rviz可视化，加上--rviz
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
对结果进行平均评分：
```bash
cd src/scripts
sudo chmod +x ./run.py
python3 report_test.py --out_path out_LfLH.txt
```
训练幻觉函数：
```bash
cd src/hallucinatio/LfH
sudo chmod +x ./LfH_main.py
python3 LfH_main.py
```
根据幻觉函数采样数据训练规划函数
```bash
cd src/hallucinatio/LfD_2D
sudo chmod +x ./LfD_main.py
python3 LfD_main.py
```