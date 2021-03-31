import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv("leads.csv")
print(data)
data_dict = data.to_dict('list')
print(data_dict)
leads = data_dict['LeadNumber']
names = data_dict['Name']
messages = data_dict['Message']

combo = zip(leads,messages,names)
first = True
for lead,message,name in combo:
    time.sleep(2)
    message = "Hi Guys, %0a%0aWelcome to Social Conclave. %0a%0aI am attaching a link for y'all to check how to register for the conference.%0a%0a https://drive.google.com/file/d/1n8PqX6kKoNbeK8TqaDupKEcecRD9cJmv/view?usp=sharing %0a%0aEnjoy the Madnessss for the next 4 daysss! 💙💙"
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')