'''imports'''
import pygeoip

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr('5.186.124.173')
for key,val in res.items():
	print('%s : %s' % (key,val))
