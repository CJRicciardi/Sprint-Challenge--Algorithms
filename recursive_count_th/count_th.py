'''
Your function should take in a single parameter(a string `word`)
Your function should return a count of how manyoccurences of ***"th"*** occur within `word`.Case matters.
Your function must utilize recursion. It cannotcontain any loops.
'''

def count_th(word): 
      
    l = len(word); 
      
    if (l == 0 or l < 2): 
        return 0; 
  
    if (word[0 : 2] == 'th'): 
        return count_th(word[1:]) + 1; 
  
    return count_th(word[1:]);
    
