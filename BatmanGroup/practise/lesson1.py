import os
import random
from pprint import pprint

# print(os.getcwd())
# os.chdir("put path")
# print(os.listdir())
#
# os.mkdir('temp2')
#os.makedirs('temp3/temp4') # creates also sub-dirs
# print(os.listdir())
# os.rmdir('temp2')
#os.removedirs('temp3/temp4') # removes also sub-dirs
# print(os.listdir())

# os.rename('file.txt', 'demo.txt')

# os.chdir("/tmp")
# print(os.listdir())
#
# print(os.stat('demo.txt'))
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))


# os.makedirs('/tmp/demo')
# os.chdir("/tmp/demo")
dir2create = ['demo_dir1', 'demo_dir2/demo_dir3', 'demo_dir4/demo_dir5/demo_dir6']
file2create = ['file1.txt', 'file2.xml', 'file3.jpeg', 'file4.sh', 'file5.pdf']
# for d in dir2create:
#     os.makedirs(d)

# for d in os.listdir('/tmp/demo'):
#     c = random.choice(range(1, 6))
#     while c > 0:
#         f = open(random.choice(file2create), "w")
#         f.close()
#         c -= 1

# created_dirs = []
# for dirpath, dirnames, filenames in os.walk('/tmp/demo'):
#     created_dirs.append(dirpath)
# created_dirs = ['/tmp/demo', '/tmp/demo/demo_dir1', '/tmp/demo/demo_dir2', '/tmp/demo/demo_dir2/demo_dir3', '/tmp/demo/demo_dir4', '/tmp/demo/demo_dir4/demo_dir5', '/tmp/demo/demo_dir4/demo_dir5/demo_dir6']

# for d in created_dirs:
#     c = random.choice(range(1, 6))
#     while c > 0:
#         f = open(os.path.join(d, random.choice(file2create)), "w")
#         f.close()
#         c -= 1


# def pretty_print(p: str) -> list:
#     list2print= []
#     for dirpath, dirnames, filenames in os.walk(p):
#         list2print.append(dirpath)
#         for fn in filenames:
#             list2print.append(os.path.join(dirpath, fn))
#     return list2print


def pretty_print(p: str, ind=0):
    print(u'\u2503' * ind + u'\u2523' + os.path.basename(p))
    if os.path.isdir(p):
        for f in os.listdir(p):
            pretty_print(os.path.join(p, f), ind+1)


def pretty_print2(p: str, ind=4):
    pprint(os.path.basename(p), indent=4)
    if os.path.isdir(p):
        for f in os.listdir(p):
            pretty_print2(os.path.join(p, f), ind+4)


# pprint(pretty_print('/tmp/demo'))
pprint(pretty_print2('/tmp/demo'))
# for e in pretty_print('/tmp/demo'):
#     print(os.path.abspath(e))

#
#
#
# print(random.choice(file2create))
# print(random.choice(range(1, 4)))

#
# for dirpath, dirnames, filenames in os.walk('\\Users\\zhovnrom\\git_projects\\CursorPython\\temp'):
# print('Current Path:', dirpath)
# print('Directories:', dirnames)
# print('Files:', filenames)
#
# print(os.environ.get('USERPROFILE'))
#
# filepath = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
# print(filepath)
#
# print(os.path.basename(filepath))
# print(os.path.dirname(filepath))
# print(os.path.exists(filepath))
