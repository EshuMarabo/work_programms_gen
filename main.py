import pandas as pd;
import data_classes as dc
import settings
import os
import re;
import work_program_parser0
import copy;

def parse_lit():
    try:
        lit_df=pd.read_excel(settings.cfg.path_to_lit,header=None)
        i=0;
        lit=[]
        while i<lit_df.shape[0]:
            lit.append(lit_df.iloc[i,0])
            i+=1
        return lit
    except:
        return []
    
    
def balance(number1,number2):
    import random
    indexes=range(0,number2)
    k=number1/number2
    d=int(number1-int(k)*number2)
    indexes_for_add=random.sample(list(indexes),d)
    balance=[int(k)]*number2
    for i in indexes_for_add:
        balance[i]+=1
    return balance

def balance_list(number1,number2):
    bal = balance(number1,number2)
    bal_ret=[]
    indexes=range(0,len(bal))
    add=0
    for i in indexes:
        bal_ret.append(list(range(add,bal[i]+add)))
        add+=bal[i]
    return bal_ret

def prepair_value_to_str(value):
    if value is None:
        return "-"
    if pd.isna(value):
        return "-"
    try:
        float(value)
        int(value)
    except:
        return "-" 
    if value==0:
        return "-"
    else:
        return str_(value)
    
def str_(value):
    if (type(value)==str):
        return value
    if pd.isna(value):
        return ""
    if float(value)==int(value):
        str_v= str(int(value));
    else:
        str_v=str(round(value,2))
        str_v=str_v.replace('.',',')
    return str_v

def find_work_program(name,program_type="бак",path_to_dir=None):
    if path_to_dir is None:
        path_to_dir = settings.cfg.path_to_old_programms
    list_filenames = os.listdir(path_to_dir)
    #print()
    #print(list_filenames)
    for file_name in list_filenames:
        if (pd.isna(file_name) or pd.isna(name) or pd.isna(program_type) ):
            continue
        res=re.search(name, file_name);
        res2=re.search(program_type, file_name);
        if res is not None:
            if res2 is not None:
                return res.string;
    return None;

def get_disc_content(name):
    print(name)
    table = pd.read_excel(settings.cfg.path_to_table_sootv,header=0)
    old_names = table[settings.cfg.year-1]
    program_types= table['key']
    names = table[settings.cfg.year]
    indexes = range(0,len(names))
    for i in indexes:

        if (names[i]==name):
            res=find_work_program(old_names[i],program_types[i]);
            if res is not None:
                return work_program_parser0.old_work_program_parse(settings.cfg.path_to_old_programms+'/'+res)
            else:
                return None
    return None;

def competentions_from_plan_splitting(string_for_split:str,delimiter:str='; '):
    import re;
    return re.split(delimiter,string_for_split)

def prepair_value(value):
    if (pd.isna(value) or value is None):
        return 0;
    try:
        return float(value);
    except:
        return 0

def float_to_string(value: float)-> str:
    if value == round(value,0):
        str_value = str(value)
        return str_value.replace(".0","")
    else:
        str_value=str(round(value,2))
        return str_value.replace('.',',')
        
def plan_reader():
    #plan_headers = list(pd.read_excel(settings.path_to_plan,sheet_name=settings.xlx.plan.plan_sheet_name,header=0).columns.values)
    plan1=pd.read_excel(settings.cfg.path_to_plan,sheet_name=settings.cfg.xlx.plan.plan_sheet_name,header=0)
    plan_book = pd.read_excel(settings.cfg.path_to_plan,sheet_name=settings.cfg.xlx.plan.plan_sheet_name,header=2)
    sem = list(plan1.loc[0,:])
    head= list(plan1.loc[1,:])
    headers =  list(plan_book.columns.values)
    
    indexes=range(0,len(headers))
    add ="";
    for i in indexes:
        if not pd.isna(sem[i]):
            #print(~(pd.isna(sem[i])))
            add = ' '+str(sem[i]);
        if (head[i]!=settings.cfg.xlx.plan.competentions and 
            head[i]!=settings.cfg.xlx.plan.kaf_code):
            head[i]+=add;
        
    plan_book.columns=head
    return plan_book;

def competentions_parser() -> list:
    com_list=[]
    compet_book = pd.read_excel(settings.cfg.path_to_comp,header=None)
    indexes=range(0,compet_book.shape[0])
    for i in indexes:
        znat=None;
        umet=None;
        vladet=None;
        temp=compet_book.loc[i,0]
        #print(temp)
        if settings.cfg.xlx.competentions.comp_check(temp):
            #print ("ok")
            j=0;
            while j<=3:
                if (settings.cfg.xlx.competentions.umet_check(compet_book.loc[i+j,0])):
                    umet=compet_book.loc[i+j,1]
                if (settings.cfg.xlx.competentions.znat_check(compet_book.loc[i+j,0])):
                    znat=compet_book.loc[i+j,1]
                    #print(znat)
                if (settings.cfg.xlx.competentions.vladet_check(compet_book.loc[i+j,0])):
                    vladet=compet_book.loc[i+j,1]
                j+=1
            com_list.append(dc.competention(compet_book.loc[i,1],compet_book.loc[i,0],znat,umet,vladet));
    return com_list;

def disciplins_parser(stop_value=None):
    plan_book=plan_reader()
    indexes=range(0,plan_book.shape[0]-1)
    discs=[]
    for  i in indexes:
        current_row = plan_book.loc[i,:];
        if stop_value is not None:
            if i >stop_value:
                break;
            stop_value+=1;
        if (type(current_row[settings.cfg.xlx.plan.disc_name]) is str):
            kaf=current_row[settings.cfg.xlx.plan.kaf_code];
            if (pd.isna(kaf)) or int(kaf)!=settings.cfg.kaf_code:
                continue;
                
            komps=competentions_from_plan_splitting(current_row[settings.cfg.xlx.plan.competentions]);
            
            name=current_row[settings.cfg.xlx.plan.disc_name];
            code=current_row[settings.cfg.xlx.plan.disc_code];
        
            zach=current_row[settings.cfg.xlx.plan.zach];
            zach_o=current_row[settings.cfg.xlx.plan.zach_o];
            ecz=current_row[settings.cfg.xlx.plan.ecz];
            kr=current_row[settings.cfg.xlx.plan.kr];
            
            semesters_temp =[]
            semesters =[]
            for h in current_row.index.values:
                q = re.split("Сем. ",h)
                if (len(q)>1):
                    if (semesters_temp.count(q[1])==0):
                        semesters_temp.append(q[1])
            for s_t in semesters_temp:
               # print(current_row['Итого '+"Сем. "+s_t])
                #print((pd.isna(current_row['Итого '+"Сем. "+s_t])))
              #  try:
               #     if (not pd.isna(current_row['Итого '+"Сем. "+s_t])):
                 #      # semesters.append(s_t)
                #except:
                if (not pd.isna(current_row['з.е. '+"Сем. "+s_t])):
                        semesters.append(s_t)
                    
            #print(name)
            #print(semesters)
            '''
            temp_for_control=""+str(zach)+str(zach_o)+str(ecz)+str(kr)
            for symbol in temp_for_control:
                try:
                    number = int(symbol);
                    if (number not in semesters) and (number!=0):
                        semesters.append(number)
                except:
                    continue;
                    
                    
                    '''
            semesters.sort()
            indexes2=range(0,len(semesters))
            for j in indexes2:
                tsn =semesters[j];
                #temp = dc.semester(temp_sem_number,~pd.isna(ecz),~pd.isna(zach),~pd.isna(kr),~pd.isna(zach_o))
                temp = dc.semester(tsn,
                                   list(str_(ecz)).count(str_(tsn))!=0,
                                   list(str_(zach)).count(str_(tsn))!=0,
                                   list(str_(kr)).count(str_(tsn))!=0,
                                   list(str_(zach_o)).count(str_(tsn))!=0)
                
                lec_key=settings.cfg.xlx.plan.lec_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                lab_key=settings.cfg.xlx.plan.lab_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                pract_key=settings.cfg.xlx.plan.pract_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                self_key=settings.cfg.xlx.plan.self_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                krpa_key=settings.cfg.xlx.plan.krpa_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                control_key=settings.cfg.xlx.plan.control_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                zach_ed_key=settings.cfg.xlx.plan.zach_ed_key+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                itog=settings.cfg.xlx.plan.summary+settings.cfg.xlx.plan.sem_suffix+str(tsn)
                
                temp.zach_ed=prepair_value(current_row[zach_ed_key]);
                temp.hours_summary.control=prepair_value(current_row[control_key]);
                temp.hours_summary.labs=prepair_value(current_row[lab_key]);
                temp.hours_summary.lections=prepair_value(current_row[lec_key]);
                temp.hours_summary.practic=prepair_value(current_row[pract_key]);
                temp.hours_summary.self_work=prepair_value(current_row[self_key]);
                temp.krpa=prepair_value(current_row[krpa_key]);
                semesters[j]=temp
            #for s in semesters:
               # print(s.number)
            dis = dc.disciplin(name,code);
            discs.append(dis)
        
            content=get_disc_content(name)
            if content is None:
                dis.isEmpty=True;
                continue;
            dis.additional_lit=content.additional_lit;
            dis.main_lit=content.main_lit;
            dis.control_questions=content.control_questions;
            dis.current_questions=content.current_questions;
            dis.IT=content.IT;
            dis.material_base=content.material_base;
            
            
            if (len(semesters)==1):
                for theme in content.themes:
                    semesters[0].add_theme(theme);
            elif len(semesters)>1:
                if (len(semesters)>len(content.themes)):
                    k=0;
                    counter=0;
                    while k<len(semesters):
                        if (k<len(content.themes)):
                            semesters[k].add_theme(content.themes[k])
                        else:
                            counter+=1
                            th=copy.copy(content.themes[-1]);
                            th.name+=" ч. "+str(counter);
                            semesters[k].add_theme(content.themes[-1])
                        k+=1
                else:
                    bal=balance_list(len(content.themes),len(semesters));
                    for j in indexes2:
                        for b in bal[j]:
                            semesters[j].add_theme(content.themes[b]);
                        
                        '''
                    parts = int(len(content.themes)/len(semesters))
                    diff=len(content.themes)-(float(parts)*float(len(semesters)))
                    #print()
                    #print(dis.name)
                    #print('сем: '+str(len(semesters)))
                    #print('тем/сем: '+str(parts))
                    #print('тем хвост: '+str(diff))
                    k=0
                    sem_co=0
                    while k<len(content.themes):
                        add=0
                        if int(k/parts)==k/parts:
                            add=1
                            if (diff>0):
                                semesters[sem_co].add_theme(content.themes[k])
                                k+=1
                                diff-=1;
                        if k<len(content.themes) and sem_co<len(semesters) :
                            semesters[sem_co].add_theme(content.themes[k])
                            #print("cont")
                            #continue;
                        
                        sem_co+=add;
                        k+=1
                        '''
           # print()
          # # for j in indexes2:
               # print(len(semesters[j].themes))
            for j in indexes2:
                semesters[j].update_hours()
            dis.semesters=semesters;

            for comp in komps:
                #print()
                #print(comp)
                current_comp=dc.competention.competention_finder(com_list,comp)
                if (current_comp is not None):
                    #print(current_comp.code)
                    dis.add_competention(current_comp)
    return discs;
com_list=competentions_parser();
disc_list= disciplins_parser();
lit=parse_lit()
table = pd.read_excel(settings.cfg.path_to_table_sootv,header=0)

for d in disc_list:
    d.lit_rotation(lit)
    i=0
    while i<table.shape[0]:
        if (table.iloc[i,0]==d.name):
            try:
                a=table.iloc[i,3]
                if (not pd.isna(a)):
                    d.autor=a
            except:
                None
        i+=1

            
