'''delete tail spaces'''
__author__ = 'Chao Zhang'
import re
def fix_tail_spaces(file_path):
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
