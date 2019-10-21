from creative_ai.utils.print_helpers import ppGramJson

class UnigramModel():

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
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary,
                  which is a dictionary of {string: integer} pairs.
                  For further explanation of UnigramModel's version of
                  self.nGramCounts, see the spec.
        """
        
        for list in text:
            for words in list:
                if words in self.nGramCounts and words != '^::^' and words != '^:::^':
                    self.nGramCounts[words] += 1
                elif words != '^::^' and words != '^:::^':
                    self.nGramCounts[words] = 1

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the UnigramModel, see the spec.
        """
        if self.nGramCounts == {}:
            return False
        else:
            return True

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  UnigramModel sees as candidates, see the spec.
        """
        return self.nGramCounts

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

# This is the code python runs when unigramModel.py is run as main
if __name__ == '__main__':

    # An example trainModel test case
    uni = UnigramModel()
    text = [ [ 'brown' ] ]
    uni.trainModel(text)
    # Should print: { 'brown' : 1 }
    print(uni)

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    uni.trainModel(text)
    # Should print: { 'brown': 2, 'dog': 1, 'fox': 1, 'lazy': 1, 'the': 2 }
    print(uni)
    
    
    text = [['hello','there','buddy'], ['hello','there','friend']]
    
    # Should print: { 'hello': 2, 'there': 2, 'buddy': 1, 'friend': 1}
    uni.trainModel(text)
    print(uni)
    
    text = [['hello'],['hello'],['hello']]
    #Should print: {'hello': 3}
    uni.trainModel(text)
    print(uni)

    text = [['hello','hello','hello']]
    #Should print: {'hello': 3}
    uni.trainModel(text)
    print(uni)
    
    text = [['hello','hello','hello'], ['^::^', '^:::^']]
    #Should print: {'hello': 3}
    uni.trainModel(text)
    print(uni)

    # An example trainingDataHasNGram test case
    uni = UnigramModel()
    sentence = "Eagles fly in the sky"
    print(uni.trainingDataHasNGram(sentence)) # should be False
    uni.trainModel(text)
    print(uni.trainingDataHasNGram(sentence)) # should be True

    uni2 = UnigramModel()
    print(uni2.trainingDataHasNGram(sentence)) #should be False
    uni2.trainModel(text)
    print(uni2.trainingDataHasNGram(sentence)) #should be True

    uni3 = UnigramModel()
    text = [['weekend','weekend','weekend','weekend'],['^::^', '^:::^']]
    uni3.trainModel(text)
    print(uni3)
    #should print {'weekend':4}

