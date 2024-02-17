#  Hue Engine ©️
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

from HueEngine.__core__ import psutil, tk, filedialog, _DICT, _TIME, _NULL
__DHM__ = False
__logging__ = 1
__logMessage__ = "<LOG>\t"
_PROCESSTIMES: _DICT[str, int] = {}

def _LOGFUNC(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if (__logging__):
            print(f"\n{__logMessage__} FUNCTION: {func.__name__}()")
            print(f"{__logMessage__} RETURNS: {result}\n")
        return result
    return wrapper

@_LOGFUNC
def _LOGINTERNAL(*args) -> str:
    return str(args)

def _RUNTEST(func):
    def wrapper(*args, **kwargs):
        print(f"\n~|\tEntering {func.__name__}")
        result = func(*args, **kwargs)
        print(f"\n~|\tExiting {func.__name__}")
        return result
    return wrapper

def _LOGRUN(func):
    def wrapper(*args, **kwargs):
        start_time = _TIME.time()
        result = func(*args, **kwargs)
        end_time = _TIME.time()
        print(f"\n~|\tEXECUTION PROFILER\n________\nMETHOD: {func.__name__} | TIME: {end_time - start_time:.3f}s\n")
        return result
    return wrapper

def _SYSTEMHEALTH() -> _NULL:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    #print(f"CPU Usage: {cpu_usage}%")
    #print(f"Memory Usage: {memory_usage}%")
    return f"<CPU> | {cpu_usage}% | <MEM> | {memory_usage}%"

def _ERRORCATCH(func, *args, **kwargs) -> str:
    """
    Executes a function safely with given arguments, catching and handling common exceptions.

    Parameters:
    func (callable): The function to be executed.
    *args: Variable length argument list for the function.
    **kwargs: Keyworded, variable-length argument dictionary for the function.
    """
    try:
        return func(*args, **kwargs)
    except ValueError as ve:
        print("\n🚫 ValueError Encountered:")
        print(f"    Description: {ve}\n")
    except TypeError as te:
        print("\n🚫 TypeError Encountered:")
        print(f"    Description: {te}\n")
    except IOError as ie:
        print("\n🚫 IOError Encountered:")
        print(f"    Description: {ie}\n")
    except ZeroDivisionError as zde:
        print("\n🚫 ZeroDivisionError Encountered:")
        print(f"    Description: {zde}\n")
    except IndexError as ie:
        print("\n🚫 IndexError Encountered:")
        print(f"    Description: {ie}\n")
    except KeyError as ke:
        print("\n🚫 KeyError Encountered:")
        print(f"    Description: {ke}\n")
    except AttributeError as ae:
        print("\n🚫 AttributeError Encountered:")
        print(f"    Description: {ae}\n")
    except ImportError as imp:
        print("\n🚫 ImportError Encountered:")
        print(f"    Description: {imp}\n")
    except NameError as ne:
        print("\n🚫 NameError Encountered:")
        print(f"    Description: {ne}\n")
    except SyntaxError as se:
        print("\n🚫 SyntaxError Encountered:")
        print(f"    Description: {se}\n")
    except Exception as e:
        print("\n🚫 Unexpected Error Encountered:")
        print(f"    Description: {e}\n")
