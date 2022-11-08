from tkinter import *
import json
import requests

root = Tk()
root.geometry("400x500")
root.title("Country Info")
root.config(bg="lightblue")

label_head = Label(root,text="Capital City Name",font=("Arial",20,"bold"),bg="lightblue")
label_head.place(relx=0.3,rely=0.15,anchor=CENTER)

city_entry = Entry(root)
city_entry.place(relx=0.22,rely=0.23,anchor=CENTER)

label_country = Label(root,text="Country: ",font=("Arial",15,"bold"),bg="lightblue")
label_country.place(relx=0.2,rely=0.43,anchor=CENTER)

label_region = Label(root,text="Region: ",font=("Arial",15,"bold"),bg="lightblue")
label_region.place(relx=0.19,rely=0.53,anchor=CENTER)

label_language = Label(root,text="Language: ",font=("Arial",15,"bold"),bg="lightblue")
label_language.place(relx=0.23,rely=0.63,anchor=CENTER)

label_population = Label(root,text="Population: ",font=("Arial",15,"bold"),bg="lightblue")
label_population.place(relx=0.24,rely=0.73,anchor=CENTER)

label_area = Label(root,text="Area: ",font=("Arial",15,"bold"),bg="lightblue")
label_area.place(relx=0.16,rely=0.83,anchor=CENTER)

def city_details():
    api_requests = requests.get("https://restcountries.com/v2/capital/"+city_entry.get())
    api_output_json = json.loads(api_requests.content)
    
    country = api_output_json[0]["name"]
    label_country["text"]="Country: "+country
    print(country)
    
    region = api_output_json[0]["region"]
    label_region["text"]="Region: "+region
    print(region)
    
    language = api_output_json[0]["languages"][0]["name"]
    label_language["text"]="Language: "+language
    print(language)
    
    populaiton = api_output_json[0]["population"]
    label_population["text"]="Population: "+str(populaiton)
    print(populaiton)
    
    area = api_output_json[0]["area"]
    label_area["text"]="Area: "+str(area)
    print(area)

btn = Button(root,text="City Details",relief=FLAT,command=city_details,bg="Yellow")
btn.place(relx=0.19,rely=0.33,anchor=CENTER)
root.mainloop()