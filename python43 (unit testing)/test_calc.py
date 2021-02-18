# here we need to import the unittest module.
import unittest
# we also need to import that module that we want to test which is calc.py
import calc

# now we need to create some test cases for the function we need to test.
# in order to create those test cases we first need to create a test class that inherits from unittest.TestCase
# this inheritance gives us lot of capabilities of that class.

class TestClac(unittest.TestCase):
    # lets write our first test. to do this we need to write a method.
    # the method needs to start with test_.
    # it is a convention and it is required so that when we run this it actually knows which method we want to test
    # so if the method dont start with test_, it wont be run.
    def test_add(self):
        # now within our method we can write our test.
        # since we have inherited from the unittest.TestCase we have the ability of all the assert methods.
        # we can find them in this url.
        """https://www.python.org/3/library/unittest.html#unittest.TestCase.debug"""

        # we are going to use asserEqual to test our add function.
        result = calc.add(10,5)
        self.assertEqual(result,15)

        # now we need to run this module we can do this in our prompt. "run the unit test.cmd"
        # NOTE: we cant use- """python test_calc.py"""
        # because it wont return anything, instead of we need to run unittest as our main module and passed in the test_calc module.
        # we can do this by -m tag.
        """python -m unittest test_calc.py"""
        # we can see that it prints a dot and says ran 1 test and at the bottom it says OK that means everything passed.
        
        # now it would be nice if we could run our test using this NOTE-d method.
        # and setting up the run that way will also allow us to test our code directly from vs code editor.
        # to do this we can use the if __name__ technic.
        # now in the prompt we can use the first method.
        # we can also run this in the editor.
    
    # we have said earliar that we have to start the name our test method test_.
    # what if we dont do that?
    def sub_test(self):
        result = calc.sub(10,5)
        self.assertEqual(result,5)
        # we can see that the number of our test haven't increased. so we cant do that.
        # so we have to be careful that all of our methods are named properly and start with test_.
    
    # what happend if our test fails?
    def test_sub(self):
        # result = calc.sub(10,5)
        # self.assertEqual(result,20)
        # we can see that instead of a dot we got an F for fail.
        # and it also shows us that the test fails with an assertion error 5 != 20
        # now lets comment our that and add some more testing.
        self.assertEqual(calc.sub(10,5),5)
        # we usually want to test some edge cases. 
        # one edge case might be one negative and one posative number.
        self.assertEqual(calc.sub(-1,1),-2)
        # two negative number will also be another edge case.
        self.assertEqual(calc.sub(-1,-1),0)
        self.assertEqual(calc.sub(10,10),0)
        # if we run it, it says that it have ran 1 test but we expected 4 test.
        # but really, the 4 assert methods here are just within this single test_add() function
        # even though it says there is one test, we can make this test better by adding in additional checks.
        
        # NOTE: it is note our goal to write as many tests as possible,
        # we need to just make sure that we write good test.

    # lets add more test.
    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)
        self.assertEqual(calc.mul(-1,-1),1)
        self.assertEqual(calc.mul(-1,1),-1)
        self.assertEqual(calc.mul(-1,0),0)
        self.assertEqual(calc.mul(0,1),0)
        self.assertEqual(calc.mul(0,0),0)

    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(-1,-1),1)
        self.assertEqual(calc.div(-1,1),-1)
        self.assertEqual(calc.div(0,-1),0)
        self.assertEqual(calc.div(0,1),0)
        # update for the floor division bug
        self.assertEqual(calc.div(5,2),2.5)

        # exception test
        # method 1: we can use the assertRaises() method
        self.assertRaises(ValueError,calc.div,10,0) 
        # first we need to pass the exception,
        # then the name of the function we want to test (without parenthesis)
        # then pass the arguments of that functions separate by comma one by one
        # the reason we have to do is this way is -
        # if we use the asserEqual() then our value will raise that error and our test will think something failed.
        
        # method 2:
        # but testing the exceptions in the previous method is not recommanded
        # because sometimes it is easy to call the function of that we want to test normally
        # instead of passing all of the arguments separately like we are doing here.
        # and we can do this by using a context manager for the exception.
        # that will allow us to handle and check the exceptions properly and also call our function normally.

        with self.assertRaises(ValueError):
            # now within this context manager we can call our function normally
            calc.div(20,0)



    
    # we can see that we get 4 dots and says that Ran 4 tests and lastly says OK.
    # and all of those tests passed with those assertEqual method.
    # so we can imagine how useful this is if we have a module with complicated functions,
    # then when we have write good test like this 
    # and then we can come here and see if all the programs run correctly or not.
    # so if we change something in our program and we think that it would work.
    # but if it broke our code, then our test should catch that.

    # for example, in our calc module's mul() function, we enter 2 * instead of 1
    # then if we come back our test_calc.py module run this,
    # we can see that in our output we have 2 dot and then a F and then again a dot
    # that means 3 of our test pass and one fails.
    
    # sometimes we might make a change that doesn't actually break our test, but unexpectedly break our code.
    # for example, in our calc module's div() function, we use the floor division(//) instead of regular division(/).
    # our current test wont catch this because right now all of our divisions are whole numbers.
    # so lets say some point floor division broke our code, 
    # and after some debugging we traced that and found that problem.
    # in that case it is a good practise to update our tests with the test that we have caught the error
    # so that we dont leave those same bugs again and again for future.
    # so lets update our test_div() function.

    # there is one more thing that we can see in our calc.py file.
    # we can see that we are checking that if the number we are divided by is 0 or not.
    # if so then we are raising a value error with the message that Can not divide by zero!
    # we likely want to test that if our expectation are working in that test as well.
    # but this is done a little differently that other assertions. 
    # there is actually 2 ways that we can do this. 
    " see above in the test_div() function"




if __name__ == "__main__":
    unittest.main()


""" 
go to the main module 
python43 (unit testing).py
"""