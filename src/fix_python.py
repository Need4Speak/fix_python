'''for pylint check\
   version: 1.5
   new: add delete spaces around the word in (...)
        the function name is check_space_bracket
        this function should be execute before fix_comma
'''
from src.sub_funs import fix_comma_file, fix_strdoc_file, fix_space_word_file, fix_tail_spaces_file

__author__ = 'zhangchao'
import re
import os
import os.path
#(4).delete tail spaces
def check_tail_spaces(file_path):
    '''delete tail spaces'''
    try:
        file_tail_spaces = open(file_path, 'r+')
        content_list = file_tail_spaces.readlines()
        for line_index in range(0, len(content_list)):
            update_sen = re.sub(r'[ \t]+\r*\n', '\n', content_list[line_index])
            content_list[line_index] = update_sen
        file_tail_spaces.close()
        file_tail_spaces = open(file_path, 'w+')
        file_tail_spaces.writelines(content_list)
        file_tail_spaces.flush()

    except BaseException, expr:
        print expr

    finally:
        if file_tail_spaces:
            file_tail_spaces.close()

#(5)format the assignment operator and comparison operator  [><!-+*/%]=?|=
#main
rootdir = r'D:\pylint_runtime'
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print "parent is:" + parent
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(parent, filename)
        file_name = os.path.join(parent, filename)
        #file_name='test.py'
        #ass_cmp_file.check_ass_cmp(file_name) not complete
        fix_tail_spaces_file.fix_tail_spaces(file_name)
        fix_space_word_file.fix_space_bracket(file_name)
        fix_comma_file.fix_comma(file_name)
        fix_strdoc_file.fix_strdoc(file_name)

