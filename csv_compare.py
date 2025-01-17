#This will be the bulk of the program, asking user to select the CSV file they wish to compare or if this is the first CSV to be stored of the day

#Import tkinter to allow user selection of files
#Import pandas to read csv and manipulate as needed
import tkinter as tk
import pandas as pd
import csv

from tkinter import filedialog

#set max rows above Pandas default
pd.options.display.max_rows = 99999

root = tk.Tk()
root.withdraw

file_path = filedialog.askopenfilename()
print (file_path)

print ("Here is your file path!", (file_path))

df1 = pd.read_csv(file_path)

file_path2 = filedialog.askopenfilename()
print (file_path2)

df2 = pd.read_csv(file_path2)



def compare(df1, df2):
    differences = []
    
    
    with open(df1, 'r') as csv_df1, open (df2, 'r') as csv_df2
        reader1 = csv.reader(csv_df1)
        reader2 = csv
    














#diff = df1.compare(df2)



#if diff is False:
    #print ("There are no differences!")

#else:
    #print ("Differences between selected Schedules")
    #print (diff)






