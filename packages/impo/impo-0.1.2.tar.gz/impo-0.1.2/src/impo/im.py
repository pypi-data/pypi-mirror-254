import os
import inspect
def port(module_name: str = None, file_name: str = None, message = None) -> bool:
    """Return the bool value
        port function import os, inspect modules.
    Args:
        module_name (str): The module name you want check if imported.
        file_name (str): Optional; The file name tha want check inside of it.
        message : Optional; message explain why return for.

    Returns:
        (None) if error
        module_name (bool): True if imported, False if not. 
    """
    
    try:
        if file_name != None and type(file_name) !=  str :
            message = file_name
            file_name = None
        if file_name == None:
            file_name = inspect.currentframe().f_back.f_code.co_filename
            file_name = os.path.basename(file_name).strip()
        if type(module_name) == str :
            module_name = module_name.strip()
            len_module_name = len(module_name)
        if len_module_name != 0:
            if not file_name.endswith('.py'):
                file_name = file_name + '.py'
            file_read = open(file_name,'r')
            file_lines = file_read.readlines()
            found_value = False
            if len(file_lines) != 0:
                for found1 in file_lines:
                    if ',' in found1:
                        found1= found1.replace(',',' ')
                    if '.' in found1:
                        found1= found1.replace('.',' ')
                    found_unslash = found1.strip()
                    len_found_unslash = len(found_unslash)                           
                    found_unslash_split = found_unslash.split()
                    len_found_unslash_split = len(found_unslash_split)
                    if 'import' in found_unslash_split:
                        if found_unslash_split.count('import') ==1 and '#' in found_unslash_split and found_unslash_split.index('import') > found_unslash_split.index('#'):
                            continue
                        if 'as' in found_unslash_split and found_unslash_split.count(module_name) ==1 and found_unslash_split.index(module_name) > found_unslash_split.index('as'):
                            continue
                        for key1,word1 in enumerate(found_unslash_split):
                            if module_name == word1 and key1 >= 1:
                                for key2,word2 in enumerate(found_unslash_split):
                                    if 'import' == word2:
                                        if key2 == 0:
                                            found_value = True
                                        elif found_unslash_split[0] == 'from':
                                            if key1 >= 1 and key1 < key2:
                                                found_value = True
                                            elif key1 >= 1 and key1 > key2:
                                                found_value = True
                                        else:
                                            continue
                            else:
                                continue
                    else:
                        continue
            elif len(file_lines) == 0:
                if message == 1 or message == True:
                    return None , 'fileEmpty'
                else:
                    return None
        elif len_module_name == 0:
            if message == 1 or message == True:
                return None , 'non-moduleName'
            else:
                return None
        if found_value == False:
            if message == 1 or message == True:
                return False, 'unimported'
            else:
                return False
        elif found_value == True:
            if message == 1 or message == True:
                return True, 'imported'
            else:
                return True
    except Exception as Exceptions:
        Exception_message = Exceptions
        if message == 1 or message == True:
            return None, Exception_message
        else:
            return None