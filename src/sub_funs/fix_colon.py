'''
this function is used to find colon(:),
and replace differnt forms of colon(like ' :' or '  :  ' or ': ')
with ':'
'''
__author__ = 'Chao Zhang'
import re
def fix_colon(file_path):
    '''read python file, check and format colon'''
    try:
        file_comma = open(file_path, 'r+')
        content_list = file_comma.readlines()
        for line_index in range(0, len(content_list)):
            update_sen = re.sub(r'[\s]+[,]', ',', content_list[line_index])
            update_sen = re.sub(r'[,][\s]*', ', ', update_sen)
            content_list[line_index] = update_sen
        #file_comma.close()
        file_comma = open(file_path, 'w+')
        file_comma.writelines(content_list)
        file_comma.flush()

    except BaseException, expr:
        print expr

    finally:
        if file_comma:
            file_comma.close()