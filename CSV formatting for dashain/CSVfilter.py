import csv
with open('member_extended.csv') as csvRead, open ('member.csv','w') as csvWrite:
	fieldnames = ['id','first_name','last_name','phone','address','email']
	writer = csv.DictWriter(csvWrite,fieldnames=fieldnames)
	writer.writeheader()

	reader = csv.DictReader(csvRead)
	for row in reader:
		writer.writerow({'id' : row['ID'], 'first_name' : row['first_name'], 'last_name' : row['last_name'], 'phone' : row['phone'], 'address' : row['address'], 'email' : row['email']})
		if((row['family_member_1_name']).strip().lower()!='n/a'):
			tempFName = (row['family_member_1_name'].strip().split(' ')[0]).capitalize()
			tempLName = (row['family_member_1_name'].strip().split(' ')[-1]).capitalize()
			writer.writerow({'id' : row['ID']+"00001",'first_name' : tempFName, 'last_name' : tempLName, 'phone' : row['phone'], 'address' : row['address'], 'email' : row['email']})
			print row['family_member_1_name'],":",tempFName,tempLName 
		if((row['family_member_2_name']).strip().lower()!='n/a'):
			tempFName = (row['family_member_2_name'].strip().split(' ')[0]).capitalize()
			tempLName = (row['family_member_2_name'].strip().split(' ')[-1]).capitalize()
			writer.writerow({'id' : row['ID']+"00002",'first_name' : tempFName, 'last_name' : tempLName, 'phone' : row['phone'], 'address' : row['address'], 'email' : row['email']})
		if((row['family_member_3_name']).strip().lower()!='n/a'):
			tempFName = (row['family_member_3_name'].strip().split(' ')[0]).capitalize()
			tempLName = (row['family_member_3_name'].strip().split(' ')[-1]).capitalize()
			writer.writerow({'id' : row['ID']+"00003",'first_name' : tempFName, 'last_name' : tempLName, 'phone' : row['phone'], 'address' : row['address'], 'email' : row['email']})
		if((row['family_member_4_name']).strip().lower()!='n/a'):
			tempFName = (row['family_member_4_name'].strip().split(' ')[0]).capitalize()
			tempLName = (row['family_member_4_name'].strip().split(' ')[-1]).capitalize()
			writer.writerow({'id' : row['ID']+"00004",'first_name' : tempFName, 'last_name' : tempLName, 'phone' : row['phone'], 'address' : row['address'], 'email' : row['email']})