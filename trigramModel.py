from creative_ai.utils.print_helpers import ppGramJson

class TrigramModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.
        
        This function is done for you.
        """

        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.
        
        This function is done for you.
        """

        return ppGramJson(self.nGramCounts)


###############################################################################
# Begin Core >> FOR CORE IMPLEMENTION, DO NOT EDIT ABOVE OF THIS SECTION <<
###############################################################################

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.
        """
        for list in text:
            for i in range(len(list)-2):
                if list[i] in self.nGramCounts:
                    if list[i+1] in self.nGramCounts[list[i]]:
                        if list[i+2] in self.nGramCounts[list[i]][list[i+1]]:
                            self.nGramCounts[list[i]][list[i+1]][list[i+2]] += 1
                        else:
                            self.nGramCounts[list[i]][list[i+1]][list[i+2]] = 1
                    else:
                        self.nGramCounts[list[i]][list[i+1]] = {}
                        self.nGramCounts[list[i]][list[i+1]][list[i+2]] = 1
                else:
                    self.nGramCounts[list[i]] = {}
                    self.nGramCounts[list[i]][list[i+1]] = {}
                    self.nGramCounts[list[i]][list[i+1]][list[i+2]] = 1



    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the TrigramModel, see the spec.
        """
        if sentence[len(sentence) - 2] in self.nGramCounts:
            if sentence[len(sentence) - 1] in self.nGramCounts[sentence[len(sentence) - 2]]:
                return True
            else:
                return False
        else:
            return False


    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  TrigramModel sees as candidates, see the spec.
        """
        return self.nGramCounts[sentence[len(sentence) - 2]][sentence[len(sentence) - 1]]

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # An example trainModel test case
    tri = TrigramModel()

    text = [ ['the', 'brown', 'fox','the', 'lazy', 'dog'] ]
    tri.trainModel(text)
    # Should print: { 'the': {'brown': {'fox': 1}, 'lazy': {'dog':1}}, 'brown':{'fox': {'the':1}}, 'fox': {'the': {'lazy':1}}
    print(tri)
    sentence = ['I','hate','brown','fox']
    print(tri.trainingDataHasNGram(sentence))
    #should print True
    print(tri.getCandidateDictionary(sentence))
    #should print {'the':1}
    sentence = ['I','hate','brown','fox', 'lazy']
    print(tri.trainingDataHasNGram(sentence))
    #should print False


    tri1 = TrigramModel()
    text = [['you', 'take', 'Wednesday'], ['you', 'take', 'Wednesday']]
    tri1.trainModel(text)
    #Should print: { 'you': {'take ': {'Wednesday': 2}}}
    print(tri1)
    
    tri2 = TrigramModel()
    text = [['you', 'take', 'Wednesday'], ['you', 'take', 'Wednesday', 'Thursday'], ['then', 'just', 'send']]
    tri2.trainModel(text)
    #Should print: { 'you': {'take ': {'Wednesday': 2}}, 'take':{'Wendesday': {'Thursday':1}}, 'then': {'just': {'send':1}}
    print(tri2)
    sentence = ['I','love','you','take']
    print(tri2.trainingDataHasNGram(sentence))
    #should print True
    print(tri2.getCandidateDictionary(sentence))
    #should print {'Wednesday' : 2}
    sentence = ['I','love','Wednesday','Thursday']
    print(tri2.trainingDataHasNGram(sentence))
    #should print False

    tri3 = TrigramModel()
    text = [['Little', 'darlin'], ['Its', 'been', 'a', 'long', 'cold', 'lonely'
            , 'winter'], ['Little', 'darlin'] , ['It','feels', 'like', 'years',
                                                 'since', 'its', 'been', 'here']]
    tri3.trainModel(text)
    print(tri3)

    tri5 = TrigramModel()
    text = [['Oh', 'I', 'will', 'return'], ['Yes', 'I', 'will', 'return'],
            ['Ill', 'come', 'back'], ['For', 'the', 'honey', 'and', 'you'],
            ['Ill', 'come', 'back']]
    tri5.trainModel(text)
    print(tri5)
