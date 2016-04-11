'''format the form of operator， like a=b to a = b'''
__author__ = 'Chao Zhang'
import re
#import os
def fix_ass_cmp(file_path):
    try:
        file_ass_cmp = open(file_path, 'r+')
        content_list = file_ass_cmp.readlines()
        pattern_exp = re.compile('[-><!+*/%=][><*/]?=?|=')
        for line_index in range(0, len(content_list)):
            han_content = content_list[line_index]
            if re.search(pattern_exp, han_content):
                operator_list = pattern_exp.findall(han_content)
                #print line_index
                #print operator_list
                var_list = re.split(pattern_exp, han_content)
                #print var_list
                update_sen = ''
                for index in range(0, len(var_list)):
                    if index == 0:
                        var_list[index] = var_list[index].rstrip()
                    elif index == len(var_list)-1:
                        var_list[index] = var_list[index].lstrip()
                    else:
                        var_list[index] = var_list[index].strip()
                    if index < len(operator_list):
                        update_sen = update_sen+var_list[index]+' '+operator_list[index]+' '
                    else:
                        update_sen += var_list[index]
                #print  update_sen
                content_list[line_index] = update_sen
        file_ass_cmp.close()
        file_ass_cmp = open(file_path, 'w+')
        file_ass_cmp.writelines(content_list)
        file_ass_cmp.flush()

    except BaseException, expr:
        print expr

    finally:
        if file_ass_cmp:
            file_ass_cmp.close()
