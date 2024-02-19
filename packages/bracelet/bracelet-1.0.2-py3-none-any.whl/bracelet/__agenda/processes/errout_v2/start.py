
'''
	https://stackoverflow.com/questions/27835746/encode-byte-string-in-utf8?rq=3
'''

'''
	bytes = chr(161)
utf8 = bytes.decode('iso-8859-1').encode('utf-8')
'''

'''
	bytestring:	b'this is a bytestring'
	
		to hex: 
			base16 = b'this is a bytestring'.hex ()
		
		from hex:
			bytestring = bytes.fromhex ("7468697320697320612062797465737472696e67")
			
		to UTF8:
			UTF8_string = b'this is a bytestring'.decode ('UTF8')
'''

from rich import print_json

import pexpect
SCRIPT = "python3 script.py"

report = {
	"journal": []
}

p = pexpect.spawn (SCRIPT)
while not p.eof ():
	line = p.readline ()	
	
	try:
		UTF8_line = line.decode ('UTF8')
		UTF8_parsed = "yes"
	except Exception:
		UTF8_line = ""
		UTF8_parsed = "no"
		
	try:
		hexadecagon_line = line.hex ()
		hexadecagon_parsed = "yes"
	except Exception:
		hexadecagon_line = ""
		hexadecagon_parsed = "no"
	
	
	line_parsed = {
		"UTF8": {
			"parsed": UTF8_parsed,
			"line": UTF8_line
		},
		"hexadecagon": {
			"parsed": hexadecagon_parsed,
			"line": hexadecagon_line
		}
	};
	
	report ["journal"].append (line_parsed)
	
	print (line, line_parsed)
	
print_json (data = report)

