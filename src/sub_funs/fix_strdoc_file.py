'''This function is used to insert a strdoc into the first line of the function without strdoc by the function name'''
__author__ = 'Chao Zhang'
import re
def fix_strdoc(file_path):
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