def test_play_both_sports(self):
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    self.assertEqual(baseball.intersection(basketball), set(['Carmen', 'Alicia']))
    print("Play both sports: ", baseball.intersection(basketball))
    
def test_play_either_sports(self):
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    self.assertEqual(baseball.union(basketball), set(['Eva', 'Carmen', 'Alicia', 'Sarah', 'Jodi', 'Aida']))
    print("Play either sports: ", baseball.union(basketball))
    
def test_play_baseball_not_basketball(self):
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    self.assertEqual(baseball.difference(basketball), set(['Jodi', 'Aida']))
    print("Play baseball, not basketball: ", baseball.difference(basketball))
    
def test_play_basket_but_not_base_and_base_not_basket(self):
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    self.assertEqual(basketball.difference(baseball), set(['Eva', 'Sarah']))
    print("Play basketball, not baseball: ", basketball.difference(baseball))
    self.assertEqual(baseball.difference(basketball), set(['Jodi', 'Aida']))
    print("Play baseball, not basketball: ", baseball.difference(basketball))
    
def test_play_one_sport_not_both(self):
    baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    self.assertEqual(baseball.symmetric_difference(basketball), set(['Aida', 'Jodi', 'Eva', 'Sarah']))
    print("Play one sport, not both: ", baseball.symmetric_difference(basketball))
    
    
    

