def import_dict_from_ini_file(file: str):
    import configparser
    loader = configparser.ConfigParser()
    try:
        result = loader.read(file)
    except (FileNotFoundError, configparser.Error):
        result = {}
    return result
