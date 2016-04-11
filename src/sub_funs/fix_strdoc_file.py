'''This function is used to insert a strdoc into the first line of the function without strdoc by the function name'''
__author__ = 'Chao Zhang'
import re
import os
def fix_strdoc(file_path, filename):
    '''read python file, check and format one line by anther
    :rtype : object
    '''
    try:
        file_strdoc = open(file_path, 'r+')
        content_list = file_strdoc.readlines()
        #1.check object file, if there is not docstring, then insert one
        file_name= ''.join(re.split(r'[.]', filename)[0])
        if (not re.match(r"\s*'''\w*", content_list[0])) and (not re.match(r'\s*"""\w*', content_list[0])):
             update_sen_file = "'''"+file_name+"'''\n"
             content_list.insert(0, update_sen_file)  #insert the strdoc into the content_list


        cur_line = ''
        pre_line = ''
        for line_index in range(0, len(content_list)):
            pre_line = cur_line  #pre_line use to get the pre line
            cur_line = content_list[line_index]  #cur_line use to get the current line
            if re.match(r'\s*def\s+\w*', pre_line):  # find the function defination

            #2.check function in the file, if there is not docstring, then insert one
                fun_name = get_fun_name(pre_line)
                if (not re.match(r"\s*'''\w*", cur_line)) and (not re.match(r'\s*"""\w*', cur_line)):
                #if there are no strdoc in the body of one certain function
                    def_location = pre_line.find('def')  #find the location of def
                    update_sen_fun = ' '*(def_location+4)  #print def_location+4 space to start print '''...'''
                    update_sen_fun = update_sen_fun + "'''"+fun_name+"'''\n"
                    print 1111111111111
                    content_list.insert(line_index, update_sen_fun)  #insert the strdoc into the content_list

            #3.check class in the file, if there is not docstring, then insert one
            elif re.match(r'\s*class\s+\w*', pre_line):  # find the function defination
                class_name = get_class_name(pre_line)
                if (not re.match(r"\s*'''\w*", cur_line)) and (not re.match(r'\s*"""\w*', cur_line)):
                #if there are no strdoc in the body of one certain class
                    class_location = pre_line.find('class')  #find the location of class
                    update_sen_class = ' '*(class_location+4)  #print class_location+4 space to start print '''...'''
                    update_sen_class = update_sen_class + "'''"+class_name+"'''\n"
                    content_list.insert(line_index, update_sen_class)  #insert the strdoc into the content_list


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

def get_class_name(temp_line):
    '''this function is used to get the object file's functions' name'''
    if re.match(r'.*\(.*', temp_line):
        # print '((((((('
        temp_line = temp_line[temp_line.find('class')+5:temp_line.find('(')].strip()
    else:
        temp_line = temp_line[temp_line.find('class')+5:temp_line.find(':')].strip()
    class_name = ''
    for index_i in range(0, len(temp_line)):
        if temp_line[index_i] <= 'Z' and temp_line[index_i] >= 'A':
            class_name = class_name + ' ' + temp_line[index_i].lower()
        elif '_' == temp_line[index_i]:
            class_name = class_name + ' '
        else:
            class_name = class_name + temp_line[index_i]
    return class_name