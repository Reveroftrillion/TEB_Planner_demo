#!/usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

def main():
    rospy.init_node('headlight_marker')
    pub = rospy.Publisher('/headlight_marker', Marker, queue_size=1, latch=True)
    rate = rospy.Rate(2)  # 2 Hz로 재게시(라칭이라 한 번만으로도 충분하지만 안전하게)

    while not rospy.is_shutdown():
        m = Marker()
        m.header.frame_id = "base_link"   # 로봇에 붙여서 같이 움직임
        m.header.stamp = rospy.Time.now()
        m.ns = "headlight"
        m.id = 0
        m.type = Marker.SPHERE_LIST        # 점 두 개
        m.action = Marker.ADD

        # 로봇 길이가 1.3m이면 앞쪽이 x=+0.65 근처.
        # 살짝 안쪽(0.60)과 좌우폭 ±0.25 지점에 두 점
        m.points = [Point(0.60, 0.25, 0.20), Point(0.60, -0.25, 0.20)]

        # 구의 지름
        m.scale.x = 0.08
        m.scale.y = 0.08
        m.scale.z = 0.08

        # 노란색 RGBA
        m.color.r = 1.0
        m.color.g = 1.0
        m.color.b = 0.0
        m.color.a = 1.0

        m.lifetime = rospy.Duration(0)    # 0=영구
        pub.publish(m)
        rate.sleep()

if __name__ == "__main__":
    main()
