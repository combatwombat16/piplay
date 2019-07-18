import sys, os, subprocess
sys.path.append("../")
from helpers.helpers import convertCToF

def get_memory_stats():
	mem_stats = {}
	tot_m, used_m, free_m, shared, buff, avail = map(int, os.popen('free -b').readlines()[-2].split()[1:])
	mem_stats["total"] = tot_m
	mem_stats["used"] = used_m
	mem_stats["free"] = free_m
	mem_stats["shared"] = shared
	mem_stats["buffered"] = buff
	mem_stats["available"] = avail
	return mem_stats

def get_swap_stats():
	swap_stats = {}
	tot_s, used_s, free_s = map(int, os.popen('free -b').readlines()[-1].split()[1:])
	swap_stats["total"] = tot_s
	swap_stats["used"] = used_s
	swap_stats["free"] = free_s
	return swap_stats

def get_sysinfo(impOrMet):
	sys_dict = {}
	if(impOrMet == "imperial"):
		sys_dict["temperature_cpu"] = convertCToF(float(str(subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]), "utf-8").replace('\n','').split("=")[1].split("'")[0]))
	else:
		sys_dict["temperature_cpu"] = float(str(subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]), "utf-8").replace('\n','').split("=")[1].split("'")[0])
	sys_dict["frequency_cpu"] = int(str(subprocess.check_output(["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"]),"utf-8").replace('\n',''))
	sys_dict["memory"] = get_memory_stats()
	sys_dict["swap"] = get_swap_stats()
	#sys_dict["timestamp"] = get_datetime()["timestamp"]
	return sys_dict

