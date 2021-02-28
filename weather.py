#importing libraries
from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality Index")
root.geometry("500x500")

#connecting to api
def get_aqi():	
	city = e_city.get().capitalize()
	try:	
		url = f"https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd0000011db07e15614c408d7c4cd9c353884a91&format=json&offset=0&limit=7&filters[city]={city}"
		r = requests.get(url)
		api = json.loads(r.text)
		print(api["records"])
		print(api["records"][0]["city"])
		pollutant_id_0 = api["records"][0]["pollutant_id"]
		pollutant_id_1 = api["records"][1]["pollutant_id"]
		pollutant_id_2 = api["records"][2]["pollutant_id"]
		pollutant_id_3 = api["records"][3]["pollutant_id"]
		pollutant_id_4 = api["records"][4]["pollutant_id"]
		pollutant_id_5 = api["records"][5]["pollutant_id"]
		pollutant_id_6 = api["records"][6]["pollutant_id"]

		#pollutant_id = [pollutant_id_0,pollutant_id_1,pollutant_id_2,
		#				pollutant_id_3,pollutant_id_4,pollutant_id_5,
		#				pollutant_id_6]
		
		pollutant_avg_0 = api["records"][0]["pollutant_avg"]
		pollutant_avg_1 = api["records"][1]["pollutant_avg"]
		pollutant_avg_2 = api["records"][2]["pollutant_avg"]
		pollutant_avg_3 = api["records"][3]["pollutant_avg"]
		pollutant_avg_4 = api["records"][4]["pollutant_avg"]
		pollutant_avg_5 = api["records"][5]["pollutant_avg"]
		pollutant_avg_6 = api["records"][6]["pollutant_avg"]

		max_pollutant = max([pollutant_avg_0,pollutant_avg_1,
							pollutant_avg_2,pollutant_avg_3,pollutant_avg_4,
							pollutant_avg_5,pollutant_avg_6])

	except EXCEPTION as e:
		label_correct = Label(root, text = "Please enter correct spelling!",
								 padx = 10, pady = 10)
		label_correct.grid(row = 2, column = 0)
		print("Error in connecting...")
	#Creting widgets
	city_label = Label(root, text = city, padx = 10, pady = 10)
	pol_lab_0 = Label(root, text = pollutant_id_0, padx = 10, pady = 10)
	pol_lab_1 = Label(root, text = pollutant_id_1, padx = 10, pady = 10)
	pol_lab_2 = Label(root, text = pollutant_id_2, padx = 10, pady = 10)
	pol_lab_3 = Label(root, text = pollutant_id_3, padx = 10, pady = 10)
	pol_lab_4 = Label(root, text = pollutant_id_4, padx = 10, pady = 10)
	pol_lab_5 = Label(root, text = pollutant_id_5, padx = 10, pady = 10)
	pol_lab_6 = Label(root, text = pollutant_id_6, padx = 10, pady = 10)

	pol_avg_0 = Label(root, text = pollutant_avg_0, padx = 10, pady = 10)
	pol_avg_1 = Label(root, text = pollutant_avg_1, padx = 10, pady = 10)
	pol_avg_2 = Label(root, text = pollutant_avg_2, padx = 10, pady = 10)
	pol_avg_3 = Label(root, text = pollutant_avg_3, padx = 10, pady = 10)
	pol_avg_4 = Label(root, text = pollutant_avg_4, padx = 10, pady = 10)
	pol_avg_5 = Label(root, text = pollutant_avg_5, padx = 10, pady = 10)
	pol_avg_6 = Label(root, text = pollutant_avg_6, padx = 10, pady = 10)

	aqi = Label(root, text = "AQI", padx = 10, pady = 10, 
					borderwidth=1, relief="solid")
	max_pollutant_lab = Label(root, text = max_pollutant, 
								padx = 10, pady = 10, borderwidth=1, relief="solid")

	#placing widgets
	city_label.grid(row=2, column = 0)

	pol_lab_0.grid(row=3, column = 0)
	pol_lab_1.grid(row=4, column = 0)
	pol_lab_2.grid(row=5, column = 0)
	pol_lab_3.grid(row=6, column = 0)
	pol_lab_4.grid(row=7, column = 0)
	pol_lab_5.grid(row=8, column = 0)
	pol_lab_6.grid(row=9, column = 0)

	pol_avg_0.grid(row=3, column = 1)
	pol_avg_1.grid(row=4, column = 1)
	pol_avg_2.grid(row=5, column = 1)
	pol_avg_3.grid(row=6, column = 1)
	pol_avg_4.grid(row=7, column = 1)
	pol_avg_5.grid(row=8, column = 1)
	pol_avg_6.grid(row=9, column = 1)

	aqi.grid(row = 4, column = 2)
	max_pollutant_lab.grid(row=5, column = 2)



e_city = Entry(root, width=50, borderwidth = 5)
city_lab = Label(root, text ="Enter a city: ", padx = 10, pady = 10)
button = Button(root, text = "Get values", padx = 10, pady = 10, command = get_aqi)

e_city.grid(row = 0, column = 1, columnspan = 5) 
city_lab.grid(row = 0, column= 0)
button.grid(row = 1, column = 2)


root.mainloop()