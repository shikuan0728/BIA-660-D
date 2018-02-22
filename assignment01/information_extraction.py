import re
import spacy
from __future__ import print_function
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
        self.has = [] if has is None else has
        self.travels = [] if travels is None else travels

    def __repr__(self):
        return self.name


class Pet(object):
    def __init__(self, pet_type, name=None):
        self.name = name
        self.type = pet_type

class Trip(object):
    def __init__(self, departs_to, departs_on=None):
        self.departs_to = departs_to
        self.departs_on = departs_on
persons = []
pets = []
trips = []

def get_data_from_file(file_path='./assignment_01.data'):
    with open(file_path) as infile:
        cleaned_lines = [line.strip() for line in infile if not line.startswith(('$$$', '###', '==='))]
    return cleaned_lines


def select_person(name):
    for person in persons:
        if person.name == name:
            return person


def add_person(name):
    person = select_person(name)
    if person is None:
        new_person = Person(name)
        persons.append(new_person)
        return new_person
    return person

def select_pet(name):
    for pet in pets:
        if pet.name == name:
            return pet

def add_pet(type, name=None):
    pet = None
    if name:
        pet = select_pet(name)
    if pet is None:
        pet = Pet(type, name)
        pets.append(pet)
    return pet

def select_trip(departs_to, departs_on):
    for trip in trips:
        if trip.departs_to == departs_to and trip.departs_on == departs_on:
            return trip

def add_trip(departs_to, departs_on):
    trip = None
    if departs_to and departs_on:
        trip = select_trip(departs_to, departs_on)
    if trip is None:
        trip = Trip(departs_to, departs_on)
        trips.append(trip)
    return trip


def get_persons_pet(person_name):
    person = select_person(person_name)
    for thing in person.has:
        return [thing for thing in person.has if isinstance(thing, Pet)]
def get_persons_dog(person_name):
    person_pets = get_persons_pet(person_name)
    if person_pets and [animal for animal in person_pets if animal.type == 'dog']:
        return [animal for animal in person_pets if animal.type == 'dog'][0]
def get_persons_cat(person_name):
    person_pets = get_persons_pet(person_name)
    if person_pets and [animal for animal in person_pets if animal.type == 'cat']:
        return [animal for animal in person_pets if animal.type == 'cat'][0]

def get_persons_destinations(person_name):
    person = select_person(person_name)
    for thing in person.
        return thing

def process_relation_triplet(triplet):
    """
    Process a relation triplet found by ClausIE and store the data
    find relations of types:
    (PERSON, likes, PERSON)
    (PERSON, dislikes, PERSON)
    (PERSON, has, PET)
    (PET, has_name, NAME)
    (PERSON, travels, TRIP)
    (TRIP, departs_on, DATE)
    (TRIP, departs_to, PLACE)
     :param triplet: The relation triplet from ClausIE
     :type triplet: tuple
     :return: a triplet in the formats specified above
     :rtype: tuple
    """

    sentence = triplet.subject + ' ' + triplet.predicate + ' ' + triplet.object

    doc = nlp(unicode(sentence))

    for t in doc:
        if t.pos_ == 'VERB' and t.head == t:
            root = t

    """
        CURRENT ASSUMPTIONS:
        - People's names are unique (i.e. there only exists one person with a certain name).
        - Pet's names are unique
        - The only pets are dogs and cats
        - Only one person can own a specific pet
        - A person can own only one pet
        """
    '''test for root.lemma_
    if root.lemma_ != 'like' and root.lemma_ != 'be' and root.lemma_ != 'have' and root.lemma_ != 'name':
        print(root.lemma_, end=' <- ')
        print(root.text)
    '''

    if root.lemma_ == 'like':
        if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON'] and triplet.object in [e.text for e in doc.ents if e.label_ == 'PERSON']:
            s = add_person(triplet.subject)
            o = add_person(triplet.object)
            if o not in s.likes:
                s.likes.append(o)
    if root.lemma_ == 'be' and triplet.object.startswith('friends with'):
        fw_doc = nlp(unicode(triplet.object))
        with_token = [t for t in fw_doc if t.text == 'with'][0]
        fw_who = [t for t in with_token.children if t.dep_ == 'pobj'][0].text

    if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON'] and fw_who in [e.text for e in doc.ents if e.label_ == 'PERSON']:
        s = add_person(triplet.subject)
        o = add_person(fw_who)
     if o not in s.likes:
        s.likes.append(o)
     if s not in o.likes:
        o.likes.append(s)

    if root.lemma_ == 'like' and root.text == 'like':
        if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON'] and triplet.object in [e.text for e in doc.ents if e.label_ == 'PERSON']:
            s = add_person(triplet.subject)
            o = add_person(triplet.object)
            s.dislikes.append(o)

    if root.lemma_ == 'have':
        if ('dog' in triplet.object or 'cat' in triplet.object) and triplet.object.find('named') == -1:
            s = add_person(triplet.subject)
            if 'dog' in triplet.object:
                o = add_pet('dog')
            else:
                o = add_pet('cat')
            if s.has == []:
                s.has.append(o)
        elif 'dog' in triplet.object or 'cat' in triplet.object:
            s = add_person(triplet.subject)
            pet_name = triplet.object[triplet.object.find('named')+6:]
            if 'dog' in triplet.object:
                o = add_pet('dog', pet_name)
            else:
                o = add_pet('cat', pet_name)
            if s.has == []:
                s.has.append(o)

    if triplet.subject.endswith('name') and ('dog' in triplet.subject or 'cat' in triplet.subject):
        obj_span = doc.char_span(sentence.find(triplet.object), len(sentence))

        if obj_span[0].pos_ == 'PROPN':
            name = triplet.object
            subj_start = sentence.find(triplet.subject)
            subj_doc = doc.char_span(subj_start, subj_start + len(triplet.subject))

            s_people = [token.text for token in subj_doc if token.ent_type_ == 'PERSON']
            assert len(s_people) == 1
            s_person = select_person(s_people[0])

            s_pet_type = 'dog' if 'dog' in triplet.subject else 'cat'

            if s_person.has != []:
                s_person.has[0].name = name
            else:
                pet = add_pet(s_pet_type, name)
                s_person.has.append(pet)

def preprocess_question(question):
    q_words = question.split(' ')

    for article in ('a', 'an', 'the'):
        try:
            q_words.remove(article)
        except:
            pass
    return re.sub(re_spaces, ' ', ' '.join(q_words))


def has_question_word(string):
    for qword in ('when', 'what', 'who'):
        if qword in string.lower():
            return True
    return False

def get_question():
    question = ' '
    while question[-1] != '?':
        question = raw_input("Please enter your question: ")
        return question
        if question[-1] != '?':
            print('This is not a question... please try again')

def answer_questions(string):
    sents = get_data_from_file()
    cl = ClausIE.get_instance()
    triples = cl.extract_triples(sents)
    q_trip = cl.extract_triples([preprocess_question(string)])[0]
    answers = []
    print(q_trip)

    if q_trip.subject.lower() == 'who' and q_trip.object == 'dog':
        answer = '{} has a dog.'
        for person in persons:
            pet = get_persons_pet(person.name)
            if pet and pet.type == 'dog':
                answer = (answer.format(person.name))
                answers.append(answer)


    if q_trip.subject.lower() == 'who' and q_trip.object == 'cat':
        answer = '{} has a cat.'
        for person in persons:
            pet = get_persons_pet(person.name)
            if pet and pet.type == 'cat':
                answer = (answer.format(person.name))
                answers.append(answer)

def main():
 sents = get_data_from_file()

    cl = ClausIE.get_instance()

    triples = cl.extract_triples(sents)


for t in triples:
    r = process_relation_triplet(t)

    # Sorry I don't know how to the rest and things I missed above....