def countwords(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def countletters(text):
    """
    Counts the number of letters in a given text.

    Args:
        text (str): The text to count letters in.

    Returns:
        int: The number of letters in the text.
    """
    char_dict = {}
    lower_text = text.lower()
    for c in lower_text:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sortedcountletters(char_dict):
    """
    Sorts the letter counts in descending order.

    Args:
        char_dict (dict): A dictionary with letters as keys and their counts as values.

    Returns:
        list: A list of tuples sorted by letter count in descending order.
    """
    sorted_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list

def sortedcountlettesnew(char_dict):
    """
    Sorts the word counts in descending order.

    Args:
        word_dict (dict): A dictionary with words as keys and their counts as values.

    Returns:
        list: A list of tuples sorted by word count in descending order.
    """
    count_list = []
    for key in char_dict:
        char_count = {"char": key, "count": char_dict[key]}
        count_list.append(char_count)
    count_list.sort(key=lambda x: x["count"], reverse=True)
    return count_list
    
    # return count_list.sort(key=lambda x: x["count"], reverse=True)