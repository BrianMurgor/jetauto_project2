# JetAuto Project 2 – ROS & Gazebo

This repository contains the required files for **Project 2** of the JetAuto robotics assignment using **ROS Melodic** and **Gazebo** simulation.

---

## Folder Structure

```
jetauto_gazebo/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── worlds.launch
├── scripts/
│   └── square_motion.py
project2_answers.txt
```

---

## How to Run

1. Copy this package into your ROS workspace:
   ```bash
   cd ~/jetauto_ws/src
   cp -r jetauto_gazebo .
   ```

2. Rebuild the workspace:
   ```bash
   cd ~/jetauto_ws
   catkin_make
   source devel/setup.bash
   ```

3. Launch Gazebo with JetAuto:
   ```bash
   roslaunch jetauto_gazebo worlds.launch
   ```

4. In another terminal, run the movement script:
   ```bash
   rosrun jetauto_gazebo square_motion.py
   ```

---

# Assessment Answers

See `project2_answers.txt` for all five required question responses.

---

##  Demo Video

video included

---




