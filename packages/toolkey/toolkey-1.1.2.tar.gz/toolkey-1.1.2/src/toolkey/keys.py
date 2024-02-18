import os
import inspect
def isimport(module_name: str = None, file_name: str = None, message = None) -> bool:
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
def isnumber(number_name: str = None, number_value: True = None, message:True = None) -> bool:
    """Return the bool value
        this version support number names from 0 to 100
    Args:
        number_name (str)   : The name you want check if number name.
        number_value (True) : Optional; to return name value.
        message(True)         : Optional; message explain why return for.

    Returns:
        (None) if error or name not updateed yet in this version
        number_name (bool): True if number name, False if not. 
    """    
    try:
        n = number_name
        output = "".join(filter(str.isalpha, n))
        if (
          output == "onehundred"
          or output == "onethousand"
          or output == "onemillion"
        ):
          output = output[3:]
        number_names_dict = {
            "zero" : 0,
            "one"  : 1 , 
            "two"  :  2 ,
            "three"  : 3 , 
            "four"  :  4 ,
            "five"  : 5 , 
            "six"  :  6 ,
            "seven"  : 7 , 
            "eight"  :  8 ,
            "nine"  : 9 , 
            "ten"  :  10 ,
            "eleven"  : 11 , 
            "twelve"  :  12 ,
            "thirteen"  : 13 , 
            "fourteen"  :  14 ,
            "fifteen"  : 15 , 
            "sixteen"  :  16 ,
            "seventeen"  : 17 , 
            "eighteen"  :  18 ,
            "nineteen"  : 19 , 
            "twenty"  :  20 ,
            "twentyone"  : 21 , 
            "twentytwo"  :  22 ,
            "twentythree"  : 23 , 
            "twentyfour"  :  24 ,
            "twentyfive"  : 25 , 
            "twentysix"  :  26 ,
            "twentyseven"  : 27 , 
            "twentyeight"  :  28 ,
            "twentynine"  : 29 , 
            "thirty"  :  30 ,
            "thirtyone"  : 31 , 
            "thirtytwo"  :  32 ,
            "thirtythree"  : 33 , 
            "thirtyfour"  :  34 ,
            "thirtyfive"  : 35 , 
            "thirtysix"  :  36 ,
            "thirtyseven"  : 37 , 
            "thirtyeight"  :  38 ,
            "thirtynine"  : 39 , 
            "forty"  :  40 ,
            "fortyone"  : 41 , 
            "fortytwo"  :  42 ,
            "fortythree"  : 43 , 
            "fortyfour"  :  44 ,
            "fortyfive"  : 45 , 
            "fortysix"  :  46 ,
            "fortyseven"  : 47 , 
            "fortyeight"  :  48 ,
            "fortynine"  : 49 , 
            "fifty"  :  50 ,
            "fiftyone"  : 51 , 
            "fiftytwo"  :  52 ,
            "fiftythree"  : 53 , 
            "fiftyfour"  :  54 ,
            "fiftyfive"  : 55 , 
            "fiftysix"  :  56 ,
            "fiftyseven"  : 57 , 
            "fiftyeight"  :  58 ,
            "fiftynine"  : 59 , 
            "sixty"  :  60 ,
            "sixtyone"  : 61 , 
            "sixtytwo"  :  62 ,
            "sixtythree"  : 63 , 
            "sixtyfour"  :  64 ,
            "sixtyfive"  : 65 , 
            "sixtysix"  :  66 ,
            "sixtyseven"  : 67 , 
            "sixtyeight"  :  68 ,
            "sixtynine"  : 69 , 
            "seventy"  :  70 ,
            "seventyone"  : 71 , 
            "seventytwo"  :  72 ,
            "seventythree"  : 73 , 
            "seventyfour"  :  74 ,
            "seventyfive"  : 75 , 
            "seventysix"  :  76 ,
            "seventyseven"  : 77 , 
            "seventyeight"  :  78 ,
            "seventynine"  : 79 , 
            "eighty"  :  80 ,
            "eightyone"  : 81 , 
            "eightytwo"  :  82 ,
            "eightythree"  : 83 , 
            "eightyfour"  :  84 ,
            "eightyfive"  : 85 , 
            "eightysix"  :  86 ,
            "eightyseven"  : 87 , 
            "eightyeight"  :  88 ,
            "eightynine"  : 89 , 
            "ninety"  :  90 ,
            "ninetyone"  : 91 , 
            "ninetytwo"  :  92 ,
            "ninetythree"  : 93 , 
            "ninetyfour"  :  94 ,
            "ninetyfive"  : 95 , 
            "ninetysix"  :  96 ,
            "ninetyseven"  : 97 , 
            "ninetyeight"  :  98 ,
            "ninetynine"  : 99 , 
            "hundred"  :  100 
            }
        if type(output) == str :
            output = output.strip().lower()
            len_output = len(output)
        if len_output != 0:
            found_value = False
            if output in number_names_dict:
                found_value = True
                if number_value == True:
                    name_value = number_names_dict[number_name]
        elif len_output == 0:
            if  message == True:
                return None , 'nonNumberName'
            else:
                return None
        if found_value == False:
            if  message == True:
                return False, 'unNumberOrUnSupport'
            else:
                return False
        elif found_value == True:
            if  message == True:
                if number_value == True:
                    return True, name_value, 'number'
                else:
                    return True, 'number'
            else:
                if number_value == True:
                    return True, name_value
                else:
                    return True
    except Exception as Exceptions:
        Exception_message = Exceptions
        if message == True:
            return None, Exception_message
        else:
            return None