from creative_ai.utils.print_helpers import ppGramJson

class BigramModel():

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
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.
        """
        for list in text:
            for i in range(len(list) - 1):
                if list[i] in self.nGramCounts:
                    if list[i+1] in self.nGramCounts[list[i]]:
                        self.nGramCounts[list[i]][list[i+1]] += 1
                    else:
                        self.nGramCounts[list[i]][list[i+1]] = 1
                else:
                    self.nGramCounts[list[i]] = {}
                    self.nGramCounts[list[i]][list[i+1]] = 1

        

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """
        if sentence[len(sentence) - 1] in self.nGramCounts:
            return True
        else:
            return False


    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        return self.nGramCounts[sentence[len(sentence) - 1]]


###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    bi = BigramModel()
    text = [['the', 'brown','fox'],['the', 'lazy', 'dog']]
    bi.trainModel(text)
    # should print: { 'the': { 'brown': 1, 'lazy':1}, 'brown': {'fox':1}, 'lazy': {'dog':1}}
    print(bi)
    sentence = ['Eagles','fly','in','the']
    print(bi.trainingDataHasNGram(sentence)) #should be True
    print(bi.getCandidateDictionary(sentence))
    #should print {brown: 1 , lazy: 1}
    sentence = ['Eagles','fly','in','the','sky']
    print(bi.trainingDataHasNGram(sentence)) #should be False

    bi1 = BigramModel()
    text = [['this','is','a','test'],['this','is','a','big','test']]
    bi1.trainModel(text)
    print(bi1)

    bi2 = BigramModel()
    text = [['the', 'bitter','coffee'],['the','dark','hot','bitter','coffee']]
    bi2.trainModel(text)
    print(bi2)
    sentence = ['This','is','bitter']
    print(bi2.trainingDataHasNGram(sentence)) #should be True
    print(bi2.getCandidateDictionary(sentence)) 
    #should print {coffee: 2}
    sentence = ['This','is','bitter','very']
    print(bi2.trainingDataHasNGram(sentence)) #should be False

    bi3 = BigramModel()
    text = [['the', 'red', 'balloon'], ['the', 'shiny', 'big', 'red', 'balloon'],['the', 'ugly', 'blue', 'balloon']]
    #should print: { 'the': { 'red': 1, shiny':1, 'ugly':1 }, 'red': {'balloon':2}, 'shiny': {'big':1}, 'big': {'red':1}, 'ugly': {'blue':1}, 'blue': {'balloon':1}, }
    bi3.trainModel(text)
    print(bi3)

    bi4 = BigramModel()
    text = [['the', 'bougie', 'bathroom'], ['the', 'beautiful', 'bougie', 'bathroom']]
    #should print:  { 'the': { 'bougie': 1, 'beautiful':1}, 'beautiful': {'bougie':1}, 'bougie': {'bathroom':2}}
    bi4.trainModel(text)
    print(bi4)
