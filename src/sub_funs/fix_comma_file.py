'''This function is used to format the form of comma'''
__author__ = 'Chao Zhang'
import re
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