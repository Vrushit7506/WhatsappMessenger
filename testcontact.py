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
  print(lead, name)
  time.sleep(2)
  message = "Hey, This Is Social Conclave"
  web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
  time.sleep(3)
  pg.hotkey('ctrl', 'w')

  