
#Script to automatically make graphs from the excel output file from the plate reader in lab230 on Andys bench.
#This SHOULD look at blank corrected based on raw data from platereader.

#Creates the dataframe ACTUAL_RESULTS_DATAFRAME which has wells as columns and blank corrected OD as rows going down.
#The well order for a 96 well plate is to go along the rows from top left then go down a row, like the platereader output.

def main():

	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt

#read in as csv

	#input_file = input("Please paste filepath to CSV ere:   ")

	data = pd.read_csv('/Users/d1762785/Documents/PhD_Millard/Potential_ecoli_BIMs/Platereader_Growth_Assays/06.08.2020/06.08.2020 ecoli mutant growth curves.csv')

	number_of_cycles = input("How many cycles did platereader run?   ")
	number_of_cycles = int(number_of_cycles)


#Create empty dataframes to store outputs in
	actual_results_dataframe = pd.DataFrame()
	my_dataframe = pd.DataFrame()

#The MOST OUTER loop goes down the rows of the excel spreadsheet, or the rows in 96 well plate.
	for k in range(0,8):
#The list of lists is the 96well plate row, each well has a list of ODs for different timepoints to store the data.
		well_A1 = []
		well_A2 = []
		well_A3 = []
		well_A4 = []
		well_A5 = []
		well_A6 = []
		well_A7 = []
		well_A8 = []
		well_A9 = []
		well_A10 = []
		well_A11 = []
		well_A12 = []

		listy_list_empties = [well_A1, well_A2, well_A3, well_A4, well_A5, well_A6, well_A7, well_A8, well_A9, well_A10, well_A11, well_A12]

#OUTSIDE LOOP is to chunk along row A of the 96 well plate.
#INSIDE LOOP is to bounce down 34 rows on excel sheet to get the OD for timepoints OF THE SAME WELL


		for j in range(0,12):

			column_location = j+1

			for i in range(1,(number_of_cycles+1)):
				#i goes in jumps of 34 because there are 34 rows in excel between readings of OD at different timepoints.
				iteration_jump_down_to_next_blank_corrected_OD = (i*23+2+k)
				OD = data.iloc[iteration_jump_down_to_next_blank_corrected_OD,column_location]
				
#When you put a log scale on a negative number or 0, it ruins
#your growth curve graph

#This is for catching tiny numbers, such as negative or 0 and putting them on the same
#scale as the rest of the log base 10 growth curves otherwise the y scale can't have 0 and goes crazy.

				OD=float(OD)
				if OD < 0.0001:
					OD = 0.001

				listy_list_empties[j].append(OD)
		#each well has list of ODs at timepoints, row gets stored in listy list empties then changed to a dataframe.
		out_dataframe = pd.DataFrame(listy_list_empties)
		#The dataframe for wells in one row is transposed so wells are columns and time goes down the columns.
		out_dataframe_v2 = out_dataframe.transpose()
		#The dataframe for wells in one row gets stuck onto the end of actual results dataframe, and the numbers stored
		#in out_dataframe_v2 get overwritten every time loop k rotates.
		#AFTER each row loop, append the out_dataframe_v2 onto the end of actual_results_dataframe so you don't copy into 
		#it over the data for the row above.
		actual_results_dataframe = pd.concat([actual_results_dataframe, out_dataframe_v2], axis=1)

	column_names = ['well_A1', 'well_A2', 'well_A3', 'well_A4', 'well_A5', 'well_A6', 'well_A7', 'well_A8', 'well_A9', 'well_A10', 'well_A11', 'well_A12', 'well_B1', 'well_B2', 'well_B3', 'well_B4', 'well_B5', 'well_B6', 'well_B7', 'well_B8', 'well_B9', 'well_B10', 'well_B11', 'well_B12','well_C1', 'well_C2', 'well_C3', 'well_C4', 'well_C5', 'well_C6', 'well_C7', 'well_C8', 'well_C9', 'well_C10', 'well_C11', 'well_C12','well_D1', 'well_D2', 'well_D3', 'well_D4', 'well_D5', 'well_D6', 'well_D7', 'well_D8', 'well_D9', 'well_D10', 'well_D11', 'well_D12','well_E1', 'well_E2', 'well_E3', 'well_E4', 'well_E5', 'well_E6', 'well_E7', 'well_E8', 'well_E9', 'well_E10', 'well_E11', 'well_E12','well_F1', 'well_F2', 'well_F3', 'well_F4', 'well_F5', 'well_F6', 'well_F7', 'well_F8', 'well_F9', 'well_F10', 'well_F11', 'well_F12','well_G1', 'well_G2', 'well_G3', 'well_G4', 'well_G5', 'well_G6', 'well_G7', 'well_G8', 'well_G9', 'well_G10', 'well_G11', 'well_G12','well_H1', 'well_H2', 'well_H3', 'well_H4', 'well_H5', 'well_H6', 'well_H7', 'well_H8', 'well_H9', 'well_H10', 'well_H11', 'well_H12']

	actual_results_dataframe.columns = column_names

#Although actual_results_dataframe contains numbers from excel, they are strings not integers. Change them to floats.
	actual_results_dataframe_floats = actual_results_dataframe.applymap(float)

#Rename the row names in from numbers to times(minutes).
	actual_results_dataframe_floats.rename(index={
	200:1000,199:995,198:990,197:985,196:980,195:975,194:970,193:965,192:960,191:955,190:950,
	189:945,188:940,187:935,186:930,185:925,184:920,183:915,182:910,181:905,180:900,179:895,178:890,177:885,176:880,175:875,174:870,173:865,172:860,171:855,170:850,
	169:845,168:840,167:835,166:830,165:825,164:820,163:815,162:810,161:805,160:800,159:795,158:790,157:785,156:780,155:775,154:770,153:765,152:760,151:755,150:750,
	149:745,148:740,147:735,146:730,145:725,144:720,143:715,142:710,141:705,140:700,139:695,138:690,137:685,136:680,135:675,134:670,133:665,132:660,131:655,130:650,
	129:645,128:640,127:635,126:630,125:625,124:620,123:615,122:610,121:605,
	120:600,119:595,118:590,117:585,116:580,115:575,114:570,113:565,112:560,111:555,110:550,109:545,108:540,107:535,106:530,
	105:525,104:520,103:515,102:510,101:505,100:500,99:495,98:490,97:485,96:480,95:475,94:470,93:465,92:460,91:455,90:450,89:445,88:440,87:435,86:430,85:425,84:420,83:415,82:410,81:405,80:400,
	79:395,78:390,77:385,76:380,75:375,74:370,73:365,72:360,71:355,70:350,69:345,68:340,67:335,66:330,65:325,64:320,63:315,62:310,61:305,60:300,
	59:295,58:290,57:285,56:280,55:275,54:270,53:265,52:260,51:255,50:250,49:245,48:240,47:235,46:230,45:225,44:220,43:215,42:210,41:205,40:200,
	39:195,38:190,37:185,36:180,35:175,34:170,33:165,32:160,31:155,30:150,29:145,28:140,27:135,26:130,25:125,24:120,23:115,22:110,21:105,20:100,
	19:95,18:90,17:85,16:80,15:75,14:70,13:65,12:60,11:55,10:50,9:45,8:40,7:35,6:30,5:25,4:20,3:15,2:10,1:5,0:0}, inplace=True)
	
	#print(actual_results_dataframe_floats.head)




#Have a go another go at subplots, do top row of 96 well plate

#squeeze = False, and axes = axes.ravel() are needed to change it from a 1D numpy array to a 2D array so subplots can be a grid.

	fig, axes = plt.subplots(nrows=8, ncols=12, figsize=(40,20), squeeze=False, sharey=True)
	axes = axes.ravel()

	fig.subplots_adjust(hspace=0.15, wspace=0.05)

#This first set of twelve almost the same codes are for the top row of the 96 well plate to create graphs.

	actual_results_dataframe_floats['well_A1'].plot(ax=axes[0])
	axes[0].set_yscale('log')

	actual_results_dataframe_floats['well_A2'].plot(ax=axes[1])
	axes[1].set_yscale('log')

	actual_results_dataframe_floats['well_A3'].plot(ax=axes[2])
	axes[2].set_yscale('log')

	actual_results_dataframe_floats['well_A4'].plot(ax=axes[3])
	axes[3].set_yscale('log')

	actual_results_dataframe_floats['well_A5'].plot(ax=axes[4])
	axes[4].set_yscale('log')

	actual_results_dataframe_floats['well_A6'].plot(ax=axes[5])
	axes[5].set_yscale('log')

	actual_results_dataframe_floats['well_A7'].plot(ax=axes[6])
	axes[6].set_yscale('log')

	actual_results_dataframe_floats['well_A8'].plot(ax=axes[7])
	axes[7].set_yscale('log')

	actual_results_dataframe_floats['well_A9'].plot(ax=axes[8])
	axes[8].set_yscale('log')

	actual_results_dataframe_floats['well_A10'].plot(ax=axes[9])
	axes[9].set_yscale('log')

	actual_results_dataframe_floats['well_A11'].plot(ax=axes[10])
	axes[10].set_yscale('log')

	actual_results_dataframe_floats['well_A12'].plot(ax=axes[11])
	axes[11].set_yscale('log')


#Each of these for loops generates the graphs for the next row of the 96 well plate.

	for i in range(1,13):
		axes_number = i+11
		column_name_creator = 'well_B'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')
					
	for i in range(1,13):
		axes_number = i+23
		column_name_creator = 'well_C'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	for i in range(1,13):
		axes_number = i+35
		column_name_creator = 'well_D'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	for i in range(1,13):
		axes_number = i+47
		column_name_creator = 'well_E'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	for i in range(1,13):
		axes_number = i+59
		column_name_creator = 'well_F'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	for i in range(1,13):
		axes_number = i+71
		column_name_creator = 'well_G'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	for i in range(1,13):
		axes_number = i+83
		column_name_creator = 'well_H'+str(i)
		actual_results_dataframe_floats[column_name_creator].plot(ax=axes[axes_number])
		axes[axes_number].set_yscale('log')

	plt.savefig('Most recent killing growth curve.png')

main()

