def run_deo(filecode,path,password):
    import ctypes
    dll = ctypes.CDLL(path) 
    dll.deobfuscator.restype = ctypes.c_char_p

    with open(filecode,"r+") as codef:
        code = codef.read()
        codef.close()
    codef.close()
	
    code = dll.deobfuscator(code.encode('utf-8'),password.encode('utf-8'))
    exec(code)

def run_deo2(code,path,password):
    import ctypes
    dll = ctypes.CDLL(path) 
    dll.deobfuscator.restype = ctypes.c_char_p
	
    code = dll.deobfuscator(code.encode('utf-8'),password.encode('utf-8'))
    exec(code)

def run_obf(filecode,path,password):
	import ctypes
	dll = ctypes.CDLL(path) 
	dll.obfuscator.restype = ctypes.c_char_p
	
	with open(filecode,"r+") as codef:
        	code = codef.read()
        	codef.close()
    	codef.close()

	dll.obfuscator(code.encode('utf-8'),password.encode('utf-8'))

def run_obf2(code,path,password):
	import ctypes
	dll = ctypes.CDLL(path) 
	dll.obfuscator.restype = ctypes.c_char_p

	dll.obfuscator(code.encode('utf-8'),password.encode('utf-8'))
