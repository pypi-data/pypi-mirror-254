import logging

_logger = logging.getLogger("Add Fields")


def add_fields(xlsx_df, json_data, pos, column_to_compare, column_to_find):
    final_data = ""
    data = []
    result = []

    try:
        xlsx_df[column_to_compare] = xlsx_df[column_to_compare].astype(str)
    except KeyError:
        _logger.error(f"No se encuentra la columna {column_to_compare}")

    try:
        xlsx_df[column_to_find] = xlsx_df[column_to_find].astype(str)
    except KeyError:
        _logger.error(f"No se encuentra la columna {column_to_find}")
    for i in range(0, xlsx_df.shape[0]):
        try:
            value = xlsx_df.loc[
                xlsx_df[column_to_compare] == (json_data[pos]["value"]),
                column_to_find,
            ].values[i]
            value = value.replace(".0", "")
            data.append(value)
            if value == "None":
                data = list(filter(lambda x: x != "None", data))
                break
        except Exception:
            break
    if len(data) != 0:
        final_data = ";".join(data)
        final_data = final_data.replace("None;", "")
    new_value = {"name": column_to_find, "value": final_data, "valid": True}
    result.append(new_value)
    print(result)
    return result

def hola_mundo():
    print("Hola mundo desde Add_Fields")