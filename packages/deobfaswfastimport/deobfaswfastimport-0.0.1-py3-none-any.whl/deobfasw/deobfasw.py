def run(filecode,path):
    import ctypes
    dll = ctypes.CDLL(path) 
    dll.deobfuscator.restype = ctypes.c_char_p
    with open(filecode,"r+") as codef:
        code = codef.read()
        codef.close()
    codef.close()
    result = dll.deobfuscator(code.encode('utf-8'))
    exec(result)