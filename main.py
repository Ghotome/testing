import traceback

searching_list = [1, 17, 6, 4, 3, 2]
target_value = 2
result = {}
for item in searching_list:
    try:
        if target_value - item > 0:
            result[target_value - item] = item
            if target_value - item in searching_list:
                print(f"Target value {target_value} is sum of {target_value - item}(index {searching_list.index(item)}) "
                      f"and {result[target_value - item]}(index {searching_list.index(target_value - item)})")
            else:
                print(f'Pair for value {item}(index {searching_list.index(item)}) not found')
        elif target_value - item == 0:
            print(f'Value is duplicating itself, no need to math: '
                  f'target {target_value} and value is {item}(index {searching_list.index(item)})')
    except KeyError as key_error:
        raise key_error
    except IndexError as index_error:
        raise index_error
    except Exception as error:
        print(f'Error: {traceback.format_exc(error)}')
