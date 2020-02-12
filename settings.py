class xls:
    def __init__(self ):
        self.plan = self.plan_params();
        self.competentions = self.competentions_params();
    class plan_params:
        def __init__(self ):
            self.plan_sheet_name='План'
            self.competentions_sheet_name='Компетенции'
            self.disc_name="Наименование"
            self.disc_code="Индекс"
            self.lec_key="Лек"
            self.lab_key="Лаб"
            self.pract_key="Пр"
            self.self_key="СР"
            self.krpa_key="КрПА"
            self.control_key="Конт роль"
            self.zach_ed_key="з.е."
            self.kaf_code="Код"
            self.competentions="Компетенции"
            self.ecz="Экза мен"
            self.zach="Зачет"
            self.zach_o="Зачет с оц."
            self.kr="КР"
            self.sem_suffix=" Сем. "
            self.summary="Итого"
            
    class parser_parameters():
        def __init__(self):
            self.labs="4.3. Л";
            self.practs="4.3. Л";
            
        def lab_check(self,text):
            return re.match("4.3. Л",text)
        
    class competentions_params:
        def __init__(self):
            self.znat = "Знать "
            self.umet = "Уметь"
            self.vladet = "Владеть"
            
        def comp_check(self,text):
            import re;
            #print((re.match('\w+-\w+',text)))
            return (re.match('\w+-\w+',text)) is not None
        
        def znat_check(self, text):
            return text==self.znat
            
        def umet_check(self, text):
            return text==self.umet
        def vladet_check(self, text):
            return text==self.vladet

class course_settings():
    def __init__(self,course,year):
        self.xlx=xls();
        self.course=course
        if (course=='бак'):
            self.path_to_titul = "content/titul_b.docx";
            self.temp_path = "content/test.docx";
            self.path_to_common = "content/1ty.docx";
            self.path_to_lit = "content/lit.xlsx";
            self.path_to_doc = "results/tit_bak2019.docx";
            self.path_to_test_save = "results/test.docx";
            self.path_to_result_dir = "results/";
            self.path_to_emblem = "content/emblem.png";
            self.path_to_plan = "content/plan_bak.xls";
            self.path_to_comp = "content/comp_bak.xlsx";
            self.path_to_table_sootv = "content/bak_tabl.xlsx";
            self.path_to_old_programms = "content/for_parse";
            self.year=year
            self.kaf_code=160;
        if (course=='маг'):
            self.path_to_titul = "content/titul_m.docx";
            self.temp_path = "content/test.docx";
            self.path_to_common = "content/2ty.docx";
            self.path_to_lit = "content/lit.xlsx";
            self.path_to_doc = "results/tit_mag2019.docx";
            self.path_to_test_save = "results/test.docx";
            self.path_to_result_dir = "results/";
            self.path_to_emblem = "content/emblem.png";
            self.path_to_plan = "content/plan_mag.xls";
            self.path_to_comp = "content/comp_mag.xlsx";
            self.path_to_table_sootv = "content/mag_tabl.xlsx";
            self.path_to_old_programms = "content/for_parse";
            self.year=year
            self.kaf_code=160;
        if (course=='спец'):
            self.path_to_titul = "content/titul_s.docx";
            self.temp_path = "content/test.docx";
            self.path_to_common = "content/3ty.docx";
            self.path_to_lit = "content/lit.xlsx";
            self.path_to_doc = "results/tit_spec2019.docx";
            self.path_to_test_save = "results/test.docx";
            self.path_to_result_dir = "results/";
            self.path_to_emblem = "content/emblem.png";
            self.path_to_plan = "content/plan_spec.xls";
            self.path_to_comp = "content/comp_spec.xlsx";
            self.path_to_table_sootv = "content/spec_tabl.xlsx";
            self.path_to_old_programms = "content/for_parse";
            self.year=year
            self.kaf_code=160;
        
cfg=course_settings('спец',2019)


#path_to_titul = "C:/1/titul_m.docx";
#path_to_titul = "C:/1/titul_s.docx";

#patn_to_plan = "C:/1/plan_mag.xls";
#patn_to_plan = "C:/1/plan_spec.xls";
        