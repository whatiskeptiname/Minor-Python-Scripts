def validate_dict(data, structure):
    for key in structure:
        try:
            if type(structure[key]) == list:
                data_type, minm, maxm = structure[key]
                if type(data[key]) is data_type:
                    if data_type == str:
                        str_len = len(data[key])
                        if str_len < minm or str_len > maxm:
                            return False
                    if data_type == int:
                        if data[key] < minm or data[key] > maxm:
                            return False
            else:
                if type(data[key]) is data_type:
                    return True
                else:
                    return False
        except KeyError:
            return False
    return True


structure = {
    "Name": [str, 3, 20],
    "age": [int, 1, 125],
}

data = {"Name": "Same", "age": 30}

print(validate_dict(data, structure))
