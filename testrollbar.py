#! /usr/bin/python

import sys, getopt
import rollbar
	
def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ht:e:", ["token=", "environment="])
	except getopt.GetoptError:
		print 'rollbartest.py -t <token> -e <environemnt>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'rollbartest.py -t <token> -e <environemnt>'
			sys.exit()
		elif opt in ("-t", "--token"):
			token = arg
		elif opt in ("-e", "--environment"):
			environment = arg
	if (token == '') or (environment == ''):
			print "Token = ", token
			print "Environment = ", environment
			print 'rollbartest.py -t <token> -e <environemnt>'
			sys.exit()
	print "Token = ", token
	print "Environment = ", environment
	xyz = {'token' : token, 'environment' : environment};
	return xyz		

if __name__ == "__main__":
	creds=main(sys.argv[1:])
		
print "Token = ", creds['token']
print "Environment = ", creds['environment']


rollbar.init(creds['token'], creds['environment'])

try:
  rollbar.report_message("Report Message: Howdy");
 
except IOError:
   rollbar.report_message('Report Message: Got an IOError on testrollbar.py');
except:
   rollbar.report_exc_info(sys.exc_info())
