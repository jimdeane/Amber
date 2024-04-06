from primes import is_prime

def test_five_is_prime():
    assert is_prime(5) == True

def test_four_is_not_prime():
    assert is_prime(4) == False
    
def test_eleven_is_prime():
    assert is_prime(11) == True

def test_twelve_is_not_prime():
    assert is_prime(12) == False
    