from django.template.defaulttags import register


@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Gets the item from the dictionary using key
    :param dictionary: dictionary data structure
    :param key: key to access dictionary with
    :return: item from dictionary
    """
    return dictionary.get(key)