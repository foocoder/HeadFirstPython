#!/usr/bin/python3
#FileName: nester.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1);
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t'),
            print(each_item);

#Testing Module
if __name__ == '__main__':
    names = ['John','Eric',['Cleese','Idle'],'Michael',['Palin']];
    print_lol(names,True);

