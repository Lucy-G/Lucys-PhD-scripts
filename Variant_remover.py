#Variant remover#

def main():
	list_of_variants = [469139,543347,841573,841590,884111,893005,893011,895450,899534,899927,901997,905099,905105,905624,905645,905654,905687,905711,905720,905754,905879,905930,908037,908045,908082,908092,908385,908484,912794,913238,913265,913640,913664,913676,913682,913691,913703,913715,913737,913746,913761,923914,923953,923968,948405,960955,960966,961704,1113790,1680108,1786427,1938542,2365550,2456278,2822462,3434131,3650554,3684736,3774418,4457632,4458470,4813799,4844157]
	new_file = open("Variant_remover_output.txt", "w+")
	list_excluding_sample_names_line_beginnings = ["CHROM","TA98_"]
	
	with open("/Users/d1762785/Documents/PhD_Millard/Miseq_Data/Snippy_Analysis_salmonellas/salmonella_snippies.txt", 'rt') as f:
		#make a list of all the lines in the CSV
		all_csv_lines = f.readlines()
		#Put the names of samples in to the new output file:	
		for line in all_csv_lines:
			if line[0:5] not in list_excluding_sample_names_line_beginnings:
				new_file.write(line)
		#If the variant isn't on the blacklist, also put it in the new output file
			if line[0:6] == "TA98_g":
				#grab the whole string, split it, turn the BP into integer to match start list
				chopped = line.split(",")
				Position = int(chopped[1])
	#			print(line)

				if Position not in list_of_variants:
					new_file.write(line)
main()