from utils.task1 import create_dirs, create_files, pretty_print


# some data for input -> task1
dir2create = ['demo_dir1', 'demo_dir2/demo_dir3', 'demo_dir4/demo_dir5/demo_dir6']
file2create = ['file1.txt', 'file2.xml', 'file3.jpeg', 'file4.sh', 'file5.pdf']

if __name__ == "__main__":
    # creating directories and files
    create_dirs(dir2create, '/tmp/demo')
    create_files(file2create, '/tmp/demo')
    pretty_print('/tmp/demo')
