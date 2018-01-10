def get_mac_addr_from_TORS(top_of_rack_switch_ipv4, top_of_rack_interface):
	import netmiko
	try:
		connection = netmiko.ConnectHandler(ip=top_of_rack_switch_ipv4, device_type='cisco_ios', username='hmussa', password='Wrx90Sti!')
		#print(connection.send_command('show mac address-table | inc Gi1/0/35'))
		con = connection.send_command('show mac address-table | inc ' + top_of_rack_interface)
		#Port36 = connection.send_command('show mac address-table | inc Gi1/0/36')
	except:
		# If we have any issues with netmiko or connectivity in general, we can gracefully fail out of this
		print ("Unable to connect to Top of Rack Switch")
		return None
	connection.disconnect()
	#r = get_mac_addr_from_TORS('r08r15-tors.sjc23.lint', 'Gi1/0/35')
	my_list = con.split()
	try:
		mac_address = str(my_list[1])
	except:
		print ("Unable to parse return from Top of Rack Switch")
		return None
	#print(r)
	#r = get_mac_addr_from_TORS('r08r15-tors.sjc23.lint', 'Gi1/0/36')
	return mac_address