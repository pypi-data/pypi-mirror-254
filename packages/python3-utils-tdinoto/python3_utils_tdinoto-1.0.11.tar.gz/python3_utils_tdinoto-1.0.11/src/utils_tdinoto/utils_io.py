import os


def create_dir_if_not_exist(dir_to_create: str) -> None:
    """This function creates the input dir if it doesn't exist.
    Args:
        dir_to_create (str): directory that we want to create
    """
    if not os.path.exists(dir_to_create):  # if dir doesn't exist
        os.makedirs(dir_to_create)  # create it
