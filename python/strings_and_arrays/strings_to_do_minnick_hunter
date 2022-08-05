def remove_blanks(str):
    str = str.split(' ')
    for i in range(len(str)):
        if str[i] == ' ':
            for j in range(i,len(str)-1):
                temp = str[j]
                str[j] = str[j+1]
                str[j+1] = temp
            str[:-1]

    return_str = ''
    for char in str:
        return_str += char
    return return_str

def getDigits(str):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    str_arr = list(str)

    i=0
    while(i < len(str_arr)-1):
        if str_arr[i] not in digits:
            for j in range(i,len(str_arr)-1):
                temp = str_arr[j]
                str_arr[j] = str_arr[j+1]
                str_arr[j+1] = temp
            str_arr.pop()
        i += 1

    return_str=''
    for char in str_arr:
        return_str += char
    return return_str

def acronyms(str):
    str_arr = str.split(' ')
    return_arr = []
    for word in str_arr:
        if word != ' ':
            return_arr.append(word[0])
    return_str=''
    for char in return_arr:
        return_str += char.upper()
    return return_str

def zip(arr1, arr2):
    dict = {}
    for i in range(len(arr1)):
        dict[str(arr1[i])] = arr2[i]
    return dict

def invert_hash(dict):
    new_dict = {}
    for key,value in dict.items():
        new_dict[value] = key
    return new_dict