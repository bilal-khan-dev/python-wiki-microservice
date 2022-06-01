import wikipedia


def wiki(name="War Goddess", length=1):
    """
    This is a wikipedia fetcher
    """
    the_wiki = wikipedia.summary(name, length)
    return the_wiki
