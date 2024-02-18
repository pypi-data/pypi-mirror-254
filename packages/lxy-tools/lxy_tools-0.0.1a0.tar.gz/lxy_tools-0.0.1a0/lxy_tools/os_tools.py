import os


def listdir_with_abs(path: str) -> str:
    '''
        2 in 1 os.listdir() tool that returns both relative and absolute paths
        ================================================================================
        Inputs:
        - path:     str,                        path to be listed
        --------------------------------------------------------------------------------
        Outputs:
        - $0:       zip[List[str], List[str]],  zipped tuples as (rel_path, abs_path)
    '''
    rel_list = []
    abs_list = []
    for item in os.listdir(path):
        rel_list.append(item)
        abs_list.append(os.path.join(path, item))
    return zip(rel_list, abs_list)
