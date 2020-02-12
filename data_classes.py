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
class cource_part:
    def __init__(self,name,contain,number):
        self.name=name;
        self.number=int(number);
        self.contain=contain;
        self.total_contact_hours=0
        self.lab_works: list[lab_work]=[]
        self.practicals: list[practical]=[]
        self.lectures: list[lecture]=[]
        
    def get_lab_hours(self):
        s=0;
        for l in self.lab_works:
            s+=l.hours;
        return s
    def get_pract_hours(self):
        s=0;
        for p in self.practicals:
            s+=p.hours;
        return s   
    
    def add_lab_work(self,lab_work_theme):
        if self.lab_works is None:
            self.lab_works=[]
        self.lab_works.append(self.lab_work(self,lab_work_theme))
        
    def add_practical(self,practical_work_contain: str=None,hours=None):
        if self.practicals is None:
            self.practicals=[]
        self.practicals.append(self.practical(self,practical_work_contain))

    def _get_clear_theme(self):
        return self.name;
    
class course_content():
    def __init__(self):
        self.autor='к.т.н., доц. Кузнецов В.В,'
        self.themes=[]
        self.labs=[]
        self.practic=[]
        self.main_lit=[]
        self.additional_lit=[]
        self.current_questions=[]
        self.control_questions=[]
        self.material_base=[]
        self.IT=[]

        
class lab_work:
    def __init__(self,cource_part: cource_part,lab_work_theme=None,hours=None):
        self.theme =lab_work_theme;
        self.hours =hours;
        self.cource_part = cource_part;
        self.cource_part.lab_works.append(self);
        
class lecture:
    def __init__(self,hours,cource_part):
        self.hours=hours;
        self.cource_part = cource_part;
        self.cource_part.lab_works.append(self);

class practical:
    def __init__(self,cource_part:cource_part,practical_work_contain=None,hours=None):
        if practical_work_contain is None:
            practical_work_contain=cource_part._get_clear_theme();
        self.contain =practical_work_contain;
        self.hours=hours;
        self.cource_part = cource_part;    
        self.cource_part.practicals.append(self);
        
class semester:
    class attestation:
        def __init__(self,examen=False,zachet=False,course_work=False,zachet_s_ocenk=False):
            self.examen=examen;
            self.zachet=zachet;
            self.zachet_s_ocenk=zachet_s_ocenk;
            self.course_work=course_work;
            self.semester=None;
            #self.course_porject=course_porject;
    class hours:
        def __init__(self,lections=0,practic=0,labs=0,self_work=0,control=0):
            self.lections=lections;
            self.practic=practic;
            self.labs=labs;
            self.self_work=self_work;
            self.control=control;

        def get_summary_contact_work(self):
            return self.control+self.labs+self.lections+self.practic;

        def get_summary(self):
            return self.get_summary_contact_work() +self.self_work;

    def __init__(self,number,examen=False,zachet=False,course_work=False,zachet_s_ocenk=False):
        self.number=number;
        self.zach_ed=None;
        self.krpa=None;
        self.attestation=self.attestation(examen,zachet,course_work,zachet_s_ocenk);
        self.hours_summary =self.hours();
        self.themes: list[cource_part]=[]
        
    def calculate_labs_pract(self):
        indexes = range(0,len(self.themes))
        lab=0;
        pract=0;
        for i in indexes:
            lab+= len(self.themes[i].lab_works)
            pract+= len(self.themes[i].practicals)
        return lab,pract
            
    def update_hours(self):
        #import main
        lab,pract= self.calculate_labs_pract()
        #self.hours_summary.labs
        #self.hours_summary.practic
        indexes = range(0,len(self.themes))

        
        
        for i in indexes:
            if lab!=0:
                bal_lab = balance(self.hours_summary.labs,lab)
                indexes2 = range(0,len(self.themes[i].lab_works))
                for i2 in indexes2:
                    self.themes[i].lab_works[i2].hours=bal_lab[i2];
            if pract!=0:
                bal_pract = balance(self.hours_summary.practic,pract)
                indexes2 = range(0,len(self.themes[i].practicals))
                for i2 in indexes2:
                    self.themes[i].practicals[i2].hours=bal_pract[i2];


    def add_theme(self,theme:cource_part):
        #number = len(self.themes)+1
        #theme.number=number;
        theme.semester=self;
        self.themes.append(theme);


class disciplin:
    
    def __init__(self,name,code):
        self.autor='к.т.н., доц. Кузнецов В.В.'
        self.name=name;
        self.code=code;
        self.competentions: list[competention]=[]
        self.semesters: list[semester]=[]
        self.main_lit: list[str]=[]
        self.additional_lit: list[str]=[]
        self.IT: list[str]=[]
        self.material_base:list[str]=[]
        self.current_questions:list[str]=[]
        self.control_questions:list[str]=[]
        self.isEmpty=False;
        
    def lit_rotation(self,liter:list):
        import datetime as dt;
        import re
        import random
        border_year=dt.datetime.now().year-5
        for_remove=[]
        for lit in self.main_lit:
            #print(lit)
            parse=re.findall('20\d\d|\19\d\d',lit)
            if parse!=[]:
                for date in parse:
                    try:
                        date = int(date)
                        #print("date parsed!")
                        if date<=border_year:
                            for_remove.append(lit)
                    except:
                        print("can't parse date")
        for lit in for_remove:
            
            try:
                #print('Removing:')
                #print(lit)
                self.additional_lit.append(lit);
                self.main_lit.remove(lit);
            except:
                print()
        
        d=abs(len(self.main_lit)-4)
        if d>len(liter):
            d=len(liter)
        
        temp_lit=random.sample(liter,d)
        #print(temp_lit)
        for l in temp_lit:
           # print('adding:')
            #print(l)
            if self.main_lit.count(l)==0:
                self.main_lit.append(l)

                        
    def add_material_base(self,base):
        self.material_base.append(base)
    def lab_check(self):
        for sem in self.semesters:
            if sem.hours_summary.labs!=0:
                return True;
        return False
    def get_attestation(self):
        for_rerurn = semester.attestation();
        for sem in self.semesters:
            for_rerurn.course_work=for_rerurn.course_work or sem.attestation.course_work
            for_rerurn.examen=for_rerurn.examen or sem.attestation.examen
            for_rerurn.zachet=for_rerurn.zachet or sem.attestation.zachet
            for_rerurn.zachet_s_ocenk=for_rerurn.zachet_s_ocenk or sem.attestation.zachet_s_ocenk
        return for_rerurn;
    def pract_check(self):
        for sem in self.semesters:
            if sem.hours_summary.practic!=0:
                return True;
        return False
    def sam_check(self):
        for sem in self.semesters:
            if sem.hours_summary.practic!=0:
                return True;
        return False
    def lec_check(self):
        for sem in self.semesters:
            if sem.hours_summary.self_work!=0:
                return True;
        return False
    
    def add_IT(self,it):
        self.main_lit.append(self._edit_source(it))

    def add_main_lit(self,book):
        self.main_lit.append(self._edit_source(book))

    def add_additional_lit(self,book):
        self.additional_lit.append(self._edit_source(book))

    def add_competention(self,competention):
        #$if (competention_finder(self.competentions,competention.code)) is not None:
        self.competentions.append(competention)
        competention.disciplins.append(self);

    def _edit_source(source:str,regular=r'^\W*\d*\W*') -> str:
        import re
        return re.sub(regular,"",source)

class competention:#todo сделать нормальную регулярку на входе
    def __init__(self,name,code,znat=None,umet=None,vladet=None):
        self.name=name;
        self.code=code;
        self.znat=znat;
        self.umet=umet;
        self.vladet=vladet;
        self.disciplins: list[disciplin]=[];

    def add_disciplin(self,disciplin : disciplin):
        self.disciplins.append(disciplin)
        disciplin.competentions.append(self)
        
    def competention_finder(competentions: list,comp_code):
        import re;
        try:
            for comp in competentions:
                res = re.match(comp_code,comp.code)
                if (res is not None):
                    return comp
            return None;
        except:
            return None;
    

    