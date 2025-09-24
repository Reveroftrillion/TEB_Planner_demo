# TEB Planner Demo

이 저장소는 **ROS1 환경에서 TEB Local Planner**를 테스트하기 위한 스터디용 데모 패키지입니다.  
`stage_ros` 시뮬레이터와 `move_base`를 기반으로 간단한 맵(`parallel_park.world`와 `t_course.world`)에서 TEB 로컬 플래너를 실행할 수 있도록 구성되어 있습니다.

## Features
- `stage_ros` 시뮬레이터를 이용한 2D 환경 구성
- `move_base` + `teb_local_planner` 연동
- Global / Local costmap 파라미터 제공
- RViz 시각화 지원 (`bringup.launch` 실행 시 자동 실행)

## 실행 방법
1. 워크스페이스 빌드
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

2. 실행
```
# Terminal 1
roscore

# Terminal 2
rosrun stage_ros stageros $(rospack find teb_stage_demo)/worlds/t_course.world
# OR
rosrun stage_ros stageros $(rospack find teb_stage_demo)/worlds/parallel_park.world

# Terminal 3
roslaunch teb_stage_demo bringup.launch
```

## Repository 구조
```
teb_stage_demo/
├── launch/
│   └── bringup.launch
├── config/
│   ├── move_base_params.yaml
│   ├── teb_local_planner_params.yaml
│   ├── global_costmap_params.yaml
│   ├── local_costmap_params.yaml
│   └── costmap_common_params.yaml
├── worlds/
│   └── t_course.world
│   └── parallel_park.world
└── CMakeLists.txt
```

## 참고
- [teb_local_planner ROS Wiki](http://wiki.ros.org/teb_local_planner)
- [stage_ros](http://wiki.ros.org/stage_ros)
