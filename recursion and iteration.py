Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

  def iterPower(base, exp):
      '''
      base: int or float.
      exp: int >= 0
 
      returns: int or float, base^exp
      '''
      # Your code here
      ans, iterator = 1, 1
      while iterator <= exp:
         ans = ans * base
         iterator += 1
      return ans
      
 # recursion     
 def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base 
    else:
        return base * recurPower(base, exp - 1)
