import requests
from bs4 import BeautifulSoup
import csv

date= input("input your date mm/dd/yy")

    #عنوان الموقع الذي نريد الوصول اليه
url = f"https://www.yallakora.com/match-center/?date={date}"
    #نقوم بعمل طلب من خلال مكتبه requsts للوصول ال الموقع
page = requests.get(url)

    #نقوم بعمل داله ونعطيها الصفحه التي وصلنا اليه 
    #هذه الداله هي التي ستقوم باستخراج البيانات
def method(page):
        #يقوم هذا السطر بإرجاع  ال byte code الخاص بهذه الصفحه  وهو عباره عن كود يصف الصفحه من خلال اكواد html وغيرها ولكن علي شكل byt code
    src=page.content
        # ولتحويل هذا الكود الي كود يسهل فهمه نستخدم ال parser من خلال مكتبه beautifulSoup
    parsing=BeautifulSoup(src,"lxml")
        #في هذا المشروع نريد استخراج اسماء البطولات والبيانات الخاصه بها 
        #نذهب الي المكان الموجود فيه البيات  من خلال الدخول الي الموقع ثم الضغط علي الزر الايمن من الفاره ونختار فحص او inspect
        #من خلال الداله find_all تقوم باجاد كل ال div من نوع class والتي يكون اسمها matchCard
        #ملحوظه هذا السطر يقوم بارجاع متغير من نوع list
    champion= parsing.find_all("div",{'class':'matchCard'})
    #print(champion[1])
        #في هذه الداله نقوم باعطائها ال div التي وجدنا فيها البيانات الخاصه بالبطوله 
        #تقوم هذه الداله بالوصول الي بيانات البطوله 
    #print(champion[0].contents[3])
    matches_details=[]
    def get_champion_info(champion):
            #contents هي عباره عن الاطفال الذي يقعون تحت الdiv 
            #find هي داله تقوم باجاد الشي الذي نريده
            #strip تقوم بحذف الفواصل الموجوده قبل الكلمه وبعدها 
        champion_title=champion.contents[1].find("h2").text.strip()
        #في هذا السطر نقوم بالوصول الي الكود الخاص بالماتشات 
        all_matches= champion.find_all('div',{'class','item finish liItem'})
        #all_matches= champion.contents[3].find_all('div',{'class','item finish liItem'})
        
        for x in range (len(all_matches)):
             teams_data=all_matches[x].find('div',{'class':'teamsData'})

             team_A=teams_data.find('div',{'class':'teamA'})
             team_name_A=team_A.find('p').text

             team_B=teams_data.find('div',{'class':'teamB'})
             team_name_B=team_B.find('p').text

             match_result=teams_data.find('div',{'class':'MResult'})
             score_for_team_A=match_result.contents[1].text
             score_for_team_B=match_result.contents[5].text
             time=match_result.contents[7].text
             
             matches_details.append({'نوع البطوله':champion_title
                                     ,"الفريق الاول":team_name_A ,"الفريق الثاني":team_name_B
                                     ,'اهداف الفريق الاول':score_for_team_A,'اهداف الفريقالثاني':score_for_team_B
                                     ,'وقت المباراة':time})



    #get_champion_info(champion[0])

    for i in range (len(champion)):
        get_champion_info(champion[i])

    #print(matches_details)

    keys=matches_details[0].keys()
    with open('C:\\Users\\AL-HASSAN\OneDrive\\Desktop\\New folder (2)\\matces details.csv','w') as output:
        dict_writer=csv.DictWriter(output,keys,delimiter=';')
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        
method(page)
