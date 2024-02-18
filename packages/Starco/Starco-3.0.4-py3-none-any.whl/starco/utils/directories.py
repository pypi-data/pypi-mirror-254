import os

def path_maker(path_list=[],relative_path='.',start_path=None):
    '''
    start_path=None=>os.getcwd()
    '''
    start_path = os.getcwd() if start_path==None else start_path
    p = os.path.abspath(os.path.join(start_path,relative_path))
    for i in path_list:
        p += '/'+str(i)
        if not os.path.exists(p):
            os.mkdir(p)
    return p
import zipfile
def zipfolder(zip_addr:str, target_dir): 
    if not zip_addr.endswith('.zip'):
        zip_addr=zip_addr + '.zip'
    zipobj = zipfile.ZipFile(zip_addr, 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
    return zip_addr

def unziper(path_to_zip_file,directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)