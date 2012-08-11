#implementation of a Trie data structure, the path to the node is the value

#node class
class Node():
    
    #initializing method
    def __init__(self, data):
        print "got this far"
        self.data = data
        self.dict = {} #maps dictionary

    #gets the data
    def getData(self):
        return self.data

    #gets the dictionary
    def getDict(self):
        return self.dict

    #sets the child node connected via the path specified
    def setNext(self, path, aNode):
        self.dict[path] = aNode

    #gets the child node connected via the path requested
    def getNext(self, path):
        if (path in self.dict):
            return self.dict[path]

    #return string form of node
    def __str__(self):
        resultString = self.data
        #check to see if dict is empty, if empty, keys() returns false
        #so return the data within this node because its at the end
        if(not self.dict.keys()):
            return resultString
        #dict is not empty, so this has children
        resultString = resultString + "\nConnected to: "
        for path in self.dict.keys():
            resultString = resultString + path + "\t"
        return resultString

#trie structure
class Trie():
    print "got this far"
    #constructor
    def __init__(self, words):
        
        self.startNode=Node("")
        for word in words:
            currNode = self.startNode
            for path in word:
                prevNode = currNode
                if(not prevNode.getNext(path)):
                    
                    currNode = Node(prevNode.getString() + path)
                    prevNode.setNext(path,currNode)
                else:
                    currNode = prevNode.getNext(path)

    #returns whether string is present
    def wordStartsWith(self,string):
        currNode=self.startNode
        for letter in string:
            if(not currNode.getNext(letter)):
                return False
            else:
                currNode=currNode.getNext(letter)
        return True





