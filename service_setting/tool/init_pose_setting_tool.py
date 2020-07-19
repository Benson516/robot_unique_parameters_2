import json
import rospkg

init_pose_dict = {
    # 'room_id': [x, y, z, w, Ori_Release, Position_tolerance]
    'Station': [2.32, 5.03, 0.7, 0.7],
    'Lobby': [2.32, 6.25, 0.7, 0.7],
    'EVin': [5.44, 7.3, 1, 0],
    'EVW': [3.06, 7.3, 1, 0]
}


print(str(init_pose_dict))

ros_package = rospkg.RosPack()
param_path = ros_package.get_path('robot_unique_parameters')
param_path += '/service_setting/init_pose_setting.txt'

mydatafile = "init_pose_setting.txt"

with open(param_path, 'w') as f:
    json.dump(init_pose_dict, f)

print("END")

"""
with open(mydatafile) as f:
    a = json.load(f)
    for key in a.keys():
        temp = key.encode('UTF8')
        a[temp] = a.pop(key)
    print a

for key in hotelGoal_dict.keys():
    print key
    print hotelGoal_dict[key]
"""