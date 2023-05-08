import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given a number a equals 3 and a number b equals -1
    a = 3
    b = -1

    # when we calculate the sum
    output = methods.sum(a, b)
    
    # then the sum should be 2
    assert output == 2

def test_difference():
    # given a number a equals 3 and a number b equals -1
    a = 3
    b = -1

    # when we calculate the difference
    output = methods.difference(a, b)
    
    # then the difference should be 4
    assert output == 4

def test_product():
    # given a number a equals 3 and a number b equals -1
    a = 3
    b = -1

    # when we calculate the product
    output = methods.product(a, b)
    
    # then the product should be -3
    assert output == -3

def test_quotient():
    # given a number a equals 4 and a number b equals 3
    a = 4
    b = 2

    # when we calculate the quotient
    output = methods.quotient(a, b)
    
    # then the division should be 2
    assert output == 2