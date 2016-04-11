'''check and format spaces around the word'''
__author__ = 'Chao Zhang'
import re
def fix_space_bracket(file_path):
    '''read python file, check and format spaces around the word'''
    try:
        file_space = open(file_path, 'r+')
        content_list = file_space.readlines()
        cur_line = ''
        for line_index in range(0, len(content_list)):
            cur_line = content_list[line_index]  #cur_line use to get the current line
            if re.match(r'\s*def\s+\w*', cur_line):  # find the function defination
                left_parenthesis = cur_line.find('(')
                right_parenthesis = cur_line.find(')')
                forward_content = cur_line[0:left_parenthesis+1:1]
                behind_content = cur_line[right_parenthesis:]
                pts_content = cur_line[left_parenthesis+1:right_parenthesis]
                pts_content = pts_content.replace(' ', '')
                update_sen = forward_content+pts_content+behind_content
                content_list[line_index] = update_sen  #insert the strdoc into the content_list
        #file_space.close()
        file_space = open(file_path, 'w+')
        file_space.writelines(content_list)  #rewrite the file
        file_space.flush()

    except BaseException, expr:
        print expr

    finally:
        if file_space:
            file_space.close()