import docx
import settings
def balance(number1,number2):
    import random
    indexes=range(0,number2)
    k=number1/number2
    d=number1-int(k)*number2
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


def parse_tituls(course_part='бак'):
    doc= docx.Document(settings.path_to_old_programms+'/tituls_'+course_part+'.docx')
    
    
parse_tituls()