def get_intended_IP_add(location,port):

	import csv

	# Check to make sure that the port identifier came to us in the right format. Return None if it didn't.
	if port != 'PDU1' or port != 'PDU2':
		print ("Port identifier seems to be in the wrong format.")
		return None

	with open('Lint_IPs.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0].strip() == location.strip():
				if port == 'PDU1':
					return row[1]
				elif port == 'PDU2':
					return row[2]
#get_intended_IP_add('R08R15','PDU1')
	return None