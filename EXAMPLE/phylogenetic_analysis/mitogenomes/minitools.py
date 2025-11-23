import os
import re
import time
def current_time(time_scale):
    if time_scale in ["d", "day"]:
        c_time = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    elif  time_scale in ["s", "S", "second"]:
        c_time = time.strftime('%Y%m%d_%H_%M_%S', time.localtime(time.time()))
    return c_time

def listdir(dirname, extension=False, not_endwith=False):
    '''
    old name:files_absolute_path_in_folder
    It's a minitool.

    文件夹下，文件的绝对路径，保存在列表中
    Parameters
        ----------
        dirname: folder path 
        extension: str. 如果extension为False，则不考虑扩展名，全部文件路径返回列表，如果有扩展名，则仅保留扩展名对应的文件路径
        not_endwith: str. 如果not_endwith为False，则不考虑文件路径结尾，否则返回文件不包含以此结尾的路径。
        Returns : a list
    '''
    files_path_list = []
    files = os.listdir(dirname)
    # print(files)
    if extension:
        extension = "." + extension.replace(".","")
        for file in files:
            if os.path.splitext(file)[-1] == extension:
                if not_endwith:
                    if not file.endswith(not_endwith):
                        files_path_list.append(os.path.join(dirname, file))
                else:
                    files_path_list.append(os.path.join(dirname, file))
    else:
        if not_endwith:
            files_path_list = [os.path.join(dirname, file) for file in files if not file.endswith(not_endwith) ]
        else:
            files_path_list = [os.path.join(dirname, file) for file in files]

    return files_path_list

# a = listdir("E:/Zesk/self/Gackage/Amber_src/test/output/onlinegb", ".gb")
# print(a)

def dictdir(dirname, file_dir="file", basename_list=False, extension=False, key_extension=False):
    '''
    basename_list: basename列表, 如果extension=False则basename是带有extension的，否则不带
    extension: False 意味着没有basename_list中自带extension，不需要额外添加
    key_extension：boolen. key_extension=False 意味着返回的dic中的key中不包含extension，
    '''

    path_dic = {}
    if basename_list == False:
        filepath_list, file_list = listdir(dirname), os.listdir(dirname)
        for filepath, basename in zip(filepath_list, file_list):
            # print(filepath)
            if file_dir == "file":
                if os.path.isfile(filepath):
                    # basename = os.path.basename(filepath)
                    if key_extension:
                        path_dic[basename] = filepath
                    else:
                        basename_None = os.path.splitext(basename)[0]
                        path_dic[basename_None] = filepath
            if file_dir == "dir":
                if os.path.isdir(filepath):
                    # basename = os.path.basename(filepath)
                    if key_extension:
                        path_dic[basename] = filepath
                    else:
                        basename_None = os.path.splitext(basename)[0]
                        path_dic[basename_None] = filepath
    else:
        if isinstance(basename_list, list):
            if extension == False:
                if key_extension:
                    for basename in basename_list:
                        filepath = os.path.join(dirname, basename)
                        path_dic[basename] = filepath
                else:
                    for basename in basename_list:
                        filepath = os.path.join(dirname, basename)
                        basename_None = os.path.splitext(basename)[0]
                        path_dic[basename_None] = filepath
            else: 
                extension = "." + extension.replace(".","")
                if key_extension:
                    for basename_None in basename_list:
                        basename = basename_None + extension
                        filepath = os.path.join(dirname, basename)
                        path_dic[basename] = filepath
                else:
                    for basename_None in basename_list:
                        basename = basename_None + extension
                        filepath = os.path.join(dirname, basename)
                        path_dic[basename_None] = filepath
        else:
            print("{} is not a list. Please reset the parameters".format(basename_list))

    return path_dic

# a = dictdir("E:/Zesk/self/Gackage/Amber_src/amber")
# a = dictdir("E:/Zesk/self/Gackage/Amber_src/test/LiHui/Ciaviceps/lab_fas/rbp2")
# a = dictdir("E:/Zesk/self/Gackage/Amber_src/test/output/")
# print(a)

def walk_file(file):
    paths_dic = {"dirs":[], "files":[]}
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # print("===================================================")
        # 遍历文件
        for f in files:
            # print(os.path.join(root, f))
            paths_dic["files"].append(os.path.join(root, f))
        # print("===================================================")
        # 遍历所有的文件夹
        for d in dirs:
            # print(os.path.join(root, d))
            paths_dic["dirs"].append(os.path.join(root, d))
    return paths_dic
# paths_dic = walk_file("E:/Zesk/self/Gackage/Amber_src/test/output")
# print(len(paths_dic))
# print(paths_dic)

# for i in os.walk("E:/Zesk/self/Gackage/Amber_src/test/output"):
#     print("***************************************************")
#     print(i)

def output_dirname(filepath, makedirs=True, output="output"):
    '''
    Set the output folder as the input file folder
    返回文件夹"output"目录，为文件所在文件夹，并能够设置是否创立该文件夹
    '''
    output = os.path.join(os.path.dirname(filepath), output)
    if makedirs==True:
        if not os.path.exists(output):
            print("makedirs: {}".format(output))
            os.makedirs(output)
    return output


def out_path_is_in_path_change(in_path, file_name=None):
    '''
    返回路径，为输入路径的添加‘_norm’版
    用于out_path设置
    '''
    if file_name == None:
        file, extension = os.path.splitext(os.path.basename(in_path))
        file_name = file + "_norm" + extension
    out_path = os.path.join(os.path.dirname(in_path), file_name)
    return out_path


def split_strings_by_fixed_length_no_abandon(strings, length):
    strings_list = re.findall(r'.{%d}'%length, strings)
    strings_list_end_length = len(strings)%length
    if strings_list_end_length != 0:
        strings_list_end = strings[-strings_list_end_length:]
        strings_list.append(strings_list_end)
    return strings_list




