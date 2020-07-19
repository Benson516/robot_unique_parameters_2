import json
import rospkg
from pyexcel_ods import get_data
import collections


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


hotelGoal_dict = {
    # 'room_id': [x, y, z, w, Ori_Release, Position_tolerance]
    'Station': [2.32, 5.03, 0.7, 0.7,  False, 0.1],
    'Station_out': [2.32, 6.25, 0.7, 0.7, False, 0.1],
    'Lobby': [2.32, 6.25, 0.7, 0.7,  False, 0.3],
    '101':   [2.94, -3.77, 0, 1,  True, 0.1],
    '102':   [3.45, 3.74, 0, 1,  True, 0.1],
    '201':   [2.94, -3.77, 0, 1,  True, 0.1],
    '202':   [3.45, 3.74, 0, 1,  True, 0.1],
    '301':   [2.94, -3.77, 0, 1,  True, 0.1],
    '302':   [3.45, 3.74, 0, 1,  True, 0.1],
    '401':   [2.94, -3.77, 0, 1,  True, 0.1],
    '402':   [3.45, 3.74, 0, 1,  True, 0.1],
    '404':   [-0.72, 3.33, 0.7, 0.7,  True, 0.1],
    'EVin':  [5.44, 7.3, 1, 0,  True, 0.1],
    'EVW1':  [3.06, 7.3, 1, 0,  False, 0.1],
    'EVW2':  [3.06, 7.3, 1, 0,  False, 0.1],
    'EVW3':  [3.06, 7.3, 1, 0,  False, 0.1],
    'EVW4':  [3.06, 7.3, 1, 0,  False, 0.1],
    'EVW1S': [-0.72, 3.33, 0.7, 0.7,  True, 0.1],
    'EVW2S': [-0.72, 3.33, 0.7, 0.7,  True, 0.1],
    'EVW3S': [-0.72, 3.33, 0.7, 0.7,  True, 0.1],
    'EVW4S': [-0.72, 3.33, 0.7, 0.7,  True, 0.1]
}

data = get_data("room_id_sheet.ods")

setting = convert(data)







print(str(hotelGoal_dict))

ros_package = rospkg.RosPack()
param_path = ros_package.get_path('robot_unique_parameters')
param_path += '/service_setting/hotelGoal.txt'

mydatafile = "hotelGoal.txt"

with open(param_path, 'w') as f:
    json.dump(hotelGoal_dict, f)

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