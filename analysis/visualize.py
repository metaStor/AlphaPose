import json
from pyecharts import Line, Overlap

path1 = r'/home/meta/software/AlphaPose/examples/demo/res1/video1.json'
path2 = r'/home/meta/software/AlphaPose/examples/demo/res2/video2.json'
path3 = r'/home/meta/software/AlphaPose/examples/demo/res3/video3.json'


def read(path):
    with open(path, 'r') as f:
        return json.load(f)


def extract(data):
    x = []
    for i in data:
        x.append(i['keypoints'][36])
    return x


x1, x2, x3 = extract(read(path1)), extract(read(path2)), extract(read(path3))

line = Line('line')

line.add('1', list(range(len(x1))), x1, mark_point=['max', 'min'],
         is_datazoom_show=True, is_datazoom_extra_show=True, datazoom_type='both')

line.add('2', list(range(len(x2))), x2, mark_point=['max', 'min'],
         is_datazoom_show=True, is_datazoom_extra_show=True, datazoom_type='both')

line.add('3', list(range(len(x3))), x3, mark_point=['max', 'min'],
         is_datazoom_show=True, is_datazoom_extra_show=True, datazoom_type='both')

# line.add('y坐标变化', attr, y, mark_point=['max', 'min'],
#          is_datazoom_show=True, is_datazoom_extra_show=True, datazoom_type='both')


line.render('./examples/demo/res1/video1.html')
line.show_config()
