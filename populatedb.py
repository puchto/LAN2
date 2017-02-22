	# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys, os

con = lite.connect('db.sqlite3')
cur = con.cursor()


directory = '/home/puchto/Dropbox/Nauka2015/pythonscripts/pliki_robocze/krowa_workfiles/'
filelist = [f for f in os.listdir(directory) if os.path.isfile(directory + f)]
for f in filelist:
	if 'klienci' in f:
		with open(directory + f) as currf:
			for i, line in enumerate(currf, 0):
				rec = line.split('|')
				with con:
					###cur.execute('delete from LAN_Sosnowiec_klienci')
					cur.execute("INSERT INTO LAN_Sosnowiec_klienci(loc_file, cl_address, mac, ip_add, kl_service, downl, upl) values (?, ?, ?, ?, ?, ?, ?)",(f, rec[0], rec[1], rec[2], rec[3], rec[4], rec[5]))
					
    				
    							
    
