import json


def json2list(filepath, keylist, encoding="utf-8"):
    """ json文件转列表数据工具,
        filepath：json文件路径,
        keylist：数据key列表集.
        :return 列表
    """
    file = filepath
    datas = []
    temp_tup = ()
    with open(file, encoding=encoding) as f:
        json_data = json.load(f)
        for case_data in json_data:
            for index in range(len(keylist)):
                keytup = (case_data.get(keylist[index]),)
                temp_tup += keytup
            datas.append(temp_tup)
            temp_tup = ()
    print(datas)
    return datas
