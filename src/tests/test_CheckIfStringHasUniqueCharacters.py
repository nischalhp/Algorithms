from main.CheckIfStringHasUniqueCharacters import CheckIfStringHasUniqueCharacters 

from nose.tools import eq_

def test_CISHUC_non_unique():

    obj = CheckIfStringHasUniqueCharacters()
    unique = obj.find_if_string_has_unique_chars('hello')
    eq_(unique, False)

def test_CISHUC_unique():

    obj = CheckIfStringHasUniqueCharacters()
    unique = obj.find_if_string_has_unique_chars('Nischal')
    eq_(unique, True)
