import ctypes
from ctypes import c_char_p, c_void_p
import platform
import os


class OnlyScraper:
    def __init__(self):
        # Determine the operating system
        self.os_name = platform.system()
        self.lib = self._load_library()

    def _load_library(self):
        # Get the directory of the current file (__file__ is the path to the current module)
        current_dir = os.path.dirname(__file__)

        # Select the correct binary file based on the operating system
        if self.os_name == "Linux":
            lib_name = "only_scraper.so"
        elif self.os_name == "Darwin":
            lib_name = "only_scraper.dylib"
        elif self.os_name == "Windows":
            lib_name = "only_scraper.dll"
        else:
            raise Exception(f"Unsupported operating system: {self.os_name}")

        # Construct the absolute path to the binary
        lib_path = os.path.join(current_dir, lib_name)
        print(lib_path)
        # Load the library
        lib = ctypes.CDLL(lib_path)
        # Setup argument and return types for the Rust functions
        lib.c_scrape.argtypes = [ctypes.c_char_p]
        lib.c_scrape.restype = (
            ctypes.c_void_p
        )  # Use c_void_p for the pointer return type
        lib.free_rust_string.argtypes = [ctypes.c_void_p]
        return lib

        # Load the library
        lib = ctypes.CDLL(lib_name)
        # Setup argument and return types for the Rust functions
        lib.c_scrape.argtypes = [c_char_p]
        lib.c_scrape.restype = c_void_p  # Use c_void_p for the pointer return type
        lib.free_rust_string.argtypes = [c_void_p]
        return lib

    def scrape(self, url):
        # Call the Rust function and get a pointer to the result string
        result_ptr = self.lib.c_scrape(url.encode("utf-8"))

        if not result_ptr:
            raise Exception("An error occurred or no data was returned.")

        # Convert the pointer to a Python string
        result_str = ctypes.c_char_p(result_ptr).value.decode("utf-8")

        # Free the Rust-allocated string after copying
        self.lib.free_rust_string(ctypes.c_void_p(result_ptr))

        return result_str
