def get_IP_from_MAC(mac):

	import netmiko
	import json

	# Temporarily commented out to deal with silly debugging issues on the core. Sigh.

	connection = netmiko.ConnectHandler(ip='Core1.lint', device_type='cisco_nxos', username='hmussa', password='Wrx90Sti!')

	ip_arp_reply = connection.send_command('show ip arp Vlan12')
	connection.disconnect()

	# Strip out the stupid header information that we do not need
	ip_arp_strip_header = ip_arp_reply.split('Interface')

	# Split the rows from eachother
	ip_arp_rows = ip_arp_strip_header[1].strip().split('\n')

	#Create a blank table to prepare for our final output
	ip_arp_table = []

	# Run each row through the loop and split into collumns. Append those collumns to the final list
	for row in ip_arp_rows:
		collumn = row.split()
		ip_arp_table.append(collumn)

	# Now lets print out one entire collumn from our final table
	for row in ip_arp_table: 
		if row[2] == mac:
			result = row[0] + " is associated with this MAC address: " + row[2]
			return result
	

 