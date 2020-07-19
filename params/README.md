## Global Parameters
Yaml file in this folder are "global paramters", you can modify paramters here to directly change parameters of [AMR_project].

## How to load global parameters
These yaml file can be load into rosparam server by launch file command , for example:

* rosparam command="load" file="$(find robot_unique_parameters)/params/docking_navigation.yaml" ns="$(arg ns_param)"

it will1 find yaml in this package(robot_unique_parameters), and load all the parameters to rosparam server. Note that "ns" is important when calling parameters. A indistinguishable namespace may cause user confused or even confilct when loading parameters.


## Contents:
This package includes the following files: 
1. amcl_aux_localization.yaml
	- Loaded at [amcl_aux_localization_all.launch], and parameters are use in [amcl_aux_localization.py] 
2. amcl_aux_tag_description.yaml
	- Loaded at [tag_detection_amclaux.launch], and parameters are use in [apriltag_ros] 
3. docking_navigation.yaml
	- Loaded at [docking_navigation_all.launch], and use in both [docking_navigation.py] and [move_operation.py]
4. docking_navigation_tag_description.yaml
	- Loaded at [tag_detection_docking.launch], and parameters are use in [apriltag_ros] 
5. base.yaml
	- An example of global paramters
