import pandas as pd
import settings
import os
import re;
import work_program_parser0

def find_work_program(name,program_type="бак",path_to_dir=None):
    if path_to_dir is None:
        path_to_dir = settings.path_to_old_programms
    list_filenames = os.listdir(path_to_dir)
    for file_name in list_filenames:
        res=re.search(name, file_name);
        res2=re.search(program_type, file_name);
        if res is not None:
            if res2 is not None:
                return res.string;
    return None;

def get_disc_content(name,program_type="бак"):
    table = pd.read_excel(settings.path_to_table_sootv,header=0)
    old_names = table[settings.year-1]
    names = table[settings.year]
    indexes = range(0,len(names))
    for i in indexes:
        if (names[i]==name):
            res=find_work_program(old_names[i],program_type);
            if res is not None:
                return work_program_parser0.old_work_program_parse(settings.path_to_old_programms+'/'+res)
            else:
                return None
    return None;


    
    


