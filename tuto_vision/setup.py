<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>tuto_vision</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="bot@mb6.imt-nord-europe.fr">bot</maintainer>
  <license>TODO: License declaration</license>

  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>
  <depend>rclpy</depend>
  <depend>geometry_msgs</depend>
  <depend>sensor_msgs</depend>
  <depend>pyrealsense2</depend>
  <depend>cv_bridge</depend>
  <depend>signal</depend>
  <depend>time</depend>
  <depend>numpy</depend>
  <depend>sys</depend>
  <depend>cv2</depend>
  <depend>rclpy.node</depend>

  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
