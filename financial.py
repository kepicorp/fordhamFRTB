#####
#
# @Author: Pierre Quemard
# @Version: 0.1
#
# _: This File is where you code your financial model :_
# _-- The expected result is a CSV file with the followint format --_
#     Column1:PK;Column2;Column3
#     string;double;string
#     val1;200;val2
#
# _-- PK indicate the primary column --_
# /!\ Check the sample.csv file as an example
#
####


def compute():
    try:
        file = open('sample.csv','r')
    except:
        return "Fail to open sample.csv"
    else:
        return file.read()

