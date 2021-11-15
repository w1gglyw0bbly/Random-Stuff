def summation(sequence):
        """
        Input: sequence: python list 
        Return: summation of the numeric elements: int or float
        """
        total_sum = 0
        for s in sequence:
                total_sum += float(s)
        return total_sum	

def reciprocal(n):
        """
        Input: n: int or float
        Returns: reciprocal of n if n is int or float otherwise
        returns error message
        """
        return 1/float(n)
        
	
def getList(filename):
        """
        Input: filename: string
        Returns: list: content of the file in list
        if file can be opened otherwise returns False
        """
        f = open('AAAAAA.txt')
        temp = f.readline()
        return [t.split('\n')[0] for t in temp.split(',') ] #returns the sequence
        

def main():
        sequence = getList('AAAAAA.txt')
        if sequence == False:
                print ("File I/O error")
        else:
                print('The sequence is: ', sequence)
                
                print ("**** Calculating Summation  ****")
                print (summation(sequence))

                print (" **** Calculating Reciprocal  ****")
                for s in sequence:
                        print ('{} : {}'.format(s , reciprocal(s)))

	

main()
