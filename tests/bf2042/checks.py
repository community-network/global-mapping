def main(
    test: str, print_item: str, statistic: dict, except_statistic: dict, data: dict
):
    temp = {}
    for key, result in data.items():
        if test in key:
            temp[key.replace(test, "")] = result

    for item, result in temp.items():
        if (
            item not in statistic
            and item not in except_statistic
            and "_all" not in item
            and item != "all"
        ):
            print(f"{item} - {data.get(f'{print_item}{item}')}")
