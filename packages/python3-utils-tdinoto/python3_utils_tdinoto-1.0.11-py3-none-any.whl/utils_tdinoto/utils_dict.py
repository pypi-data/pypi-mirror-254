import pickle
import os


def key_with_max_val(d: dict):
    """This function takes as input a dict and returns the key with the max value by
    a) creating a list of the dict's keys and values;
    b) returning the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def save_dict_to_disk_with_pickle(dict_to_save: dict,
                                  out_dir: str,
                                  out_filename: str) -> None:
    """This function saves a dict to disk using pickle.
    Args:
        dict_to_save (dict): dict to save
        out_dir (str): output directory
        out_filename (str): output filename
    """
    if not os.path.exists(out_dir):  # if output folder does not exist
        os.makedirs(out_dir)  # create it
    open_file = open(os.path.join(out_dir, out_filename), "wb")
    pickle.dump(dict_to_save, open_file)  # save dict with pickle
    open_file.close()  # close file
    
    
def load_dict_from_disk_with_pickle(path_to_dict: str) -> dict:
    """This function loads a dict from disk
    Args:
        path_to_dict: path to where the dict is saved
    Returns:
        loaded_dict: loaded list
    Raises:
        AssertionError: if dict path does not exist
    """
    assert os.path.exists(path_to_dict), "Path {} does not exist".format(path_to_dict)
    open_file = open(path_to_dict, "rb")  # open file
    loaded_dict = pickle.load(open_file)  # load from disk
    open_file.close()  # close file

    return loaded_dict


def main():
    pass


if __name__ == '__main__':
    main()
