from __future__ import print_function
import re
import spacy
from pyclausie import ClausIE

re_spaces = re.compile(r'\s+')
nlp = spacy.load('en')

class Person(object):
    def __init__(self, name, likes=None, has=None, travels=None):
        """
        :param name: the person's name
        :type name: basestring
        :param likes: (Optional) an initial list of likes
        :type likes: list
        :param dislikes: (Optional) an initial list of likes
        :type dislikes: list
        :param has: (Optional) an initial list of things the person has
        :type has: list
        :param travels: (Optional) an initial list of the person's travels
        :type travels: list
        """
        self.name = name
        self.likes = [] if likes is None else likes
        self.dislikes = [] if dislikes is None else dislikes
        self.has = [] if has is None else has
        self.travels = [] if travels is None else travels