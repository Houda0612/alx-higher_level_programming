#!/usr/bin/python3
def element_at(my_list, idx):
  """
    Gets an element in a list at given index
    And returns it
    """
    my_list_len = len(my_list)
    if idx < 0 or idx > my_list_len - 1:
        return 'None'
    else:
        return my_list[idx]
