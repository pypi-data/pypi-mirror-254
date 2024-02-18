"""
Module that gather the most common functions of imports
"""


def imports_summary_str(imports_dict: dict) -> str:
    """
    Create a string to output the imports result for a single file.

    Args:
        imports_dict (dict): Imports found in a file.

    Returns:
        str: String with file name and its various imports.
    """
    out = []
    for file in imports_dict.keys():
        out.append(f"{file} :")
        if imports_dict[file]:
            for imported_from in imports_dict[file].keys():
                list_str = "\n       - " + "\n       - ".join(
                    imports_dict[file][imported_from]
                )
                out.append(f"    Functions imported from {imported_from} :{list_str}")

    return "\n".join(out)
