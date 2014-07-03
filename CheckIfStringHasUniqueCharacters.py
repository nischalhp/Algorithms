# to find if strings have unique characters

class CheckIfStringHasUniqueCharacters:

    def find_if_string_has_unique_chars(self,string):
        
        # convert all chars to Upper case, because ord of 'a' & 'A' are different
        string = string.upper()
        
        character_list = list(string)
        boolean_hash= {}
        for i in xrange(len(character_list)):
            if ord(character_list[i]) in boolean_hash:
                return False
            else:
                boolean_hash[ord(character_list[i])] = True 

        return True

