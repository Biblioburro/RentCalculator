import tkinter as tk
import os
from os.path import exists
root = tk.Tk()

canvas1 = tk.Canvas(root,width = 300,height = 300 )
canvas1.pack()

calculated = False


#create a label and input field for power
powerLabel = tk.Label(root,text="Power")
powerField = tk.Text(root,height = 1,width = 10)
canvas1.create_window(50,50,window = powerField)
canvas1.create_window(50,25,window = powerLabel)
#create a label and input field for Internet
internetLabel = tk.Label(root,text="Internet")
internetField = tk.Text(root,height = 1,width = 10)
canvas1.create_window(150,50,window = internetField)
canvas1.create_window(150,25,window = internetLabel)
#create a label and input field for Rent
rentLabel = tk.Label(root,text="Rent")
rentField = tk.Text(root,height = 1,width = 10)
canvas1.create_window(250,50,window = rentField)
canvas1.create_window(250,25,window = rentLabel)
#create a label and input field for Gas
gasLabel = tk.Label(root,text="Gas")
gasField = tk.Text(root,height = 1,width = 10)
canvas1.create_window(50,150,window = gasField)
canvas1.create_window(50,125,window = gasLabel)
#create labels to display the calculated rent to
rentInfo = tk.Label(root, text='Total Due', fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(50,200, window=rentInfo)
totalPayment = tk.Label(root, text='$0.0', fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(50, 250, window=totalPayment)
indvRentInfo = tk.Label(root, text='Split Due', fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(150,200, window=indvRentInfo)
indvtotalPayment = tk.Label(root, text='$0.0', fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 250, window=indvtotalPayment)

def calculateRent():
    sum = 0
    sum += 0 if powerField.get("1.0","end-1c") == '' else float(powerField.get("1.0","end-1c"))
    sum += 0 if internetField.get("1.0","end-1c") == '' else float(internetField.get("1.0","end-1c"))
    sum += 0 if rentField.get("1.0","end-1c") == '' else float(rentField.get("1.0","end-1c"))
    sum += 0 if gasField.get("1.0","end-1c") == '' else float(gasField.get("1.0","end-1c"))
    totalPayment.config(text = "$"+str(float(sum)))
    indvtotalPayment.config(text = "$"+str(sum/2))
    global calculated
    calculated = True
def ExportRent():
    #if rent hasnt been calculated
    if totalPayment['text'] != "$0.0":
        #choose appropriate open mode based on whether the file exists
        if exists(os.getcwd()+"\\rent.csv"):
           f= open("rent.csv",'a')
        else:
           f=open("rent.csv","x")
           f.write("TotalDue,IndividualDue\n")

        f.write(totalPayment["text"]+","+indvtotalPayment['text']+"\n")
        f.close()
    else:
        errLabel['text'] = 'Calculate rent before exporting'


errLabel = tk.Label(root ,text = "Error")
canvas1.create_window(200,150,window = errLabel)
button1 = tk.Button(text='Calculate',command=calculateRent, bg='brown',fg='white')
canvas1.create_window(250, 250, window=button1)
exportButton = tk.Button(text = 'Export',command=ExportRent,bg='brown',fg='white')
canvas1.create_window(250, 200, window=exportButton)
root.mainloop()