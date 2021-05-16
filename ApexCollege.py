try:
	#Empty pupil list
	list_of_pupil=[ ]

	#Accept pupil data
	list_of_pupil=input("Please enter pupil data separated with comma: ")
	splitdata=list_of_pupil.split(",")

	#NPM: Number of pupils to be moved
	NPM=str(input("Please enter number of pupils to be moved: "))

	#Given data
	print("\nGiven data: " + str(splitdata) + ": "+ NPM +"\n")

	#Length of pupil data
	length_of_data=len(splitdata)
	
	#Addition of '-' to length of data
	string_of_length=str(length_of_data)
	neg="-"+string_of_length
	#NI: neg_to_int
	NI=int(neg)
	
	#Function to solve the movement
	def shuffleclass(pupil_list, movement):
		#if length of movement greater than length of list
		if int(movement) > int(length_of_data):
			movement=int(movement) - int(length_of_data)
			movement=str(movement)
			#To move from end to front
			if "-" not in movement:
				move="-" + movement
			#MCI: movement_conversion_to_int
				MCI=int(move)
				first_slice=splitdata[MCI:]
				second_slice=splitdata[NI:MCI]
			#Arg: Arragement of solution
				Arg=first_slice + second_slice
				print("=========================\n")
				print(Arg)
				print("\n")
				print("=========================")
			
			
		#To move from front to end
			elif "-" in movement:
			#Convert to positive
				move=movement[1: ]
				MCI=int(move)
				first_slice=splitdata[MCI: ]
				second_slice=splitdata[0: MCI]
				Arg=first_slice + second_slice
				print("=========================\n")
				print(Arg)
				print("\n")
				print("=========================")
				#if length of movement not greater than lenhth of data
		elif int(movement) <= int(length_of_data):
			#To move from end to front
			if "-" not in movement:
				move="-" + movement
			#MCI: movement_conversion_to_int
				MCI=int(move)
				first_slice=splitdata[MCI:]
				second_slice=splitdata[NI:MCI]
			#Arg: Arragement of solution
				Arg=first_slice + second_slice
				print("=========================\n")
				print(Arg)
				print("\n")
				print("=========================")
			
			
		#To move from front to end
			elif "-" in movement:
			#Convert to positive
				move=movement[1: ]
				MCI=int(move)
				first_slice=splitdata[MCI: ]
				second_slice=splitdata[0: MCI]
				Arg=first_slice + second_slice
				print("=========================\n")
				print(Arg)
				print("\n")
				print("=========================")
			
			
			
			
	#Call function		
	shuffleclass(splitdata,NPM)
			
except:
	print("Error in input")