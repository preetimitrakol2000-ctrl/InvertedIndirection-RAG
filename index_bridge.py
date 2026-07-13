import ctypes
import os
import sys

class IndexBridge:
    def __init__(self):
        if not os.path.exists("./libinverted.so") and not os.path.exists("./libinverted.dll"):
            if sys.platform.startswith("win"):
                os.system("gcc -shared -o libinverted.dll inverted_index.c")
                lib_path = "./libinverted.dll"
            else:
                os.system("gcc -shared -fPIC -o libinverted.so inverted_index.c")
                lib_path = "./libinverted.so"
        else:
            lib_path = "./libinverted.dll" if sys.platform.startswith("win") else "./libinverted.so"

        self.lib = ctypes.CDLL(lib_path)
        self.lib.init_index.restype = ctypes.c_void_p
        self.lib.map_token.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        self.lib.gather_chunks.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
        
        self.index_ptr = self.lib.init_index()

    def index_word(self, word: str, chunk_id: int):
        self.lib.map_token(self.index_ptr, word.lower().encode('utf-8'), chunk_id)

    def search_word(self, word: str) -> list:
        out_array = (ctypes.c_int * 10)()
        out_count = ctypes.c_int(0)
        self.lib.gather_chunks(self.index_ptr, word.lower().encode('utf-8'), out_array, ctypes.byref(out_count))
        return [out_array[i] for i in range(out_count.value)]
# ProbabilisticFilter-RAG // Bit-Vector Metadata Guard

A lightweight validation engine written in C to instantly reject non-existent document lookups before hitting heavy semantic infrastructure.

## Test Run
```bash
python probabilistic_rag.py
