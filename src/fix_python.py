'''for pylint check\
   version: 1.5
   new: add delete spaces around the word in (...)
        the function name is check_space_bracket
        this function should be execute before fix_comma
'''
__author__ = 'zhangchao'
import re
import os
import os.path
import ass_cmp_file

#(1).format_comma()
def fix_comma(file_path):
    '''read python file, check and format one line by anther'''
    try:
        file_comma = open(file_path, 'r+')
        content_list = file_comma.readlines()
        for line_index in range(0, len(content_list)):
            if re.match(r"(\".*\"|'.*')[.]join", content_list[line_index]):
                continue
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

#(2).check and format strdoc
def check_strdoc(file_path):
    '''read python file, check and format one line by anther
    :rtype : object
    '''
    try:
        file_strdoc = open(file_path, 'r+')
        content_list = file_strdoc.readlines()
        cur_line = ''
        pre_line = ''
        for line_index in range(0, len(content_list)):
            pre_line = cur_line  #pre_line use to get the pre line
            cur_line = content_list[line_index]  #cur_line use to get the current line
            if re.match(r'\s*def\s+\w*', pre_line):  # find the function defination
                fun_name = get_fun_name(pre_line)
                if (not re.match(r"\s*'''\w*", cur_line)) and (not re.match(r'\s*"""\w*', cur_line)):
                #if there are no strdoc in the body of one certain function
                    def_location = pre_line.find('def')  #find the location of def
                    update_sen = ' '*(def_location+4)  #print def_location+4 space to start print '''...'''
                    update_sen = update_sen + "'''"+fun_name+"'''\n"
                    content_list.insert(line_index, update_sen)  #insert the strdoc into the content_list
        #file_strdoc.close()
        file_strdoc = open(file_path, 'w+')
        file_strdoc.writelines(content_list)  #rewrite the file
        file_strdoc.flush()

    except BaseException, expr:
        print expr

    finally:
        if file_strdoc:
            file_strdoc.close()
#get function name
def get_fun_name(temp_line):
    '''this function is used to get the object file's functions' name'''
    temp_line = temp_line[temp_line.find('def')+3:temp_line.find('(')].strip()
    fun_name = ''
    for index_i in range(0, len(temp_line)):
        if temp_line[index_i] <= 'Z' and temp_line[index_i] >= 'A':
            fun_name = fun_name + ' ' + temp_line[index_i].lower()
        elif '_' == temp_line[index_i]:
            fun_name = fun_name + ' '
        else:
            fun_name = fun_name + temp_line[index_i]
    return fun_name

#(3).check and format spaces around the word
def check_space_bracket(file_path):
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
        check_tail_spaces(file_name)
        check_space_bracket(file_name)
        fix_comma(file_name)
        check_strdoc(file_name)

