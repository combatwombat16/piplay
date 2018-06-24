import subprocess

def get_memoryinfo():
	mem_stats = {}
	ms = str(subprocess.check_output(["free"]), "utf-8")
	ms_split_col = ms.split('\n')
	names = ["total","used","free","shared","buffer","available"]
	for col in range(len(ms_split_col)):
		row =  ms_split_col[col].split()
		if(col == 1):
			for field in range(len(row)):
				if(field > 0):
					mem_stats[names(field)] = col[field]
	return mem_stats
#		if(col == 0):
#			for field in range(len(row)):
#				names[str(field, "utf-8")] = col[field]
#	mem_stats["free"] = ms_split[0]

def get_sysinfo():
	sys_dict = {}
	sys_dict["temperature_cpu"] = float(str(subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]), "utf-8").replace('\n','').split("=")[1].split("'")[0])
	sys_dict["frequency_cpu"] = int(str(subprocess.check_output(["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"]),"utf-8").replace('\n',''))
	#sys_dict["memory"] = get_memory_stats()
	return sys_dict

#print(get_memoryinfo())
