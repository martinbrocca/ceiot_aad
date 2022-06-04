from configparser import ConfigParser

from pandas import isnull



def config(filename, section):
#def config(filename, section):
    if filename == "":
        filename ='C:\\Users\\marti\\OneDrive\\Documents\\CEIOT\\AAD\\TP_Final\\database.ini'
  
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db