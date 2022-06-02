import wikipedia


def wiki(name="War Goddess", length=1):
    """
    This is a wikipedia fetcher
    """
    the_wiki = wikipedia.summary(name, length)
    return the_wiki

def search_wiki(name):
    """
    Search wikipedia for names
    """
    return wikipedia.search(name)