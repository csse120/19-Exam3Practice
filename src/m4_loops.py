"""
PRACTICE Exam 3.

This problem provides practice at:  LOOPS, including:
  ***  FOR and WHILE loops.  ***
  ***  LOOPS within LOOPS. ***

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################

import simple_testing as st
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_practice_problem3()

# -----------------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
# -----------------------------------------------------------------------------

def practice_problem3a(start, stop, threshold):
    """
    What comes in:
      -- Nonnegative integers start and stop, with stop >= start
      -- A number:  threshold
    What goes out:  Returns a list of all the integers,  starting at start
      and ending at stop (inclusive), for which the sum of the integer's
      sine and cosine is bigger than the given threshold.
    Side effects: None.
    Examples:
       practice_problem3b(-2, 2, 1.3)  returns  [1, 7]
    as you can see if you work through this example using
    the numbers presented below. (Do so!)

    For these examples, the following (and more) numbers
    (each is rounded to 2 decimal places for the sake of brevity)
    are relevant:
        -5:  sin =  0.96,  cos =  0.28,  sum =  1.24
        -4:  sin =  0.76,  cos = -0.65,  sum =  0.10
        -3:  sin = -0.14,  cos = -0.99,  sum = -1.13
        -2:  sin = -0.91,  cos = -0.42,  sum = -1.33
        -1:  sin = -0.84,  cos =  0.54,  sum = -0.30
         0:  sin =  0.00,  cos =  1.00,  sum =  1.00
         1:  sin =  0.84,  cos =  0.54,  sum =  1.38
         2:  sin =  0.91,  cos = -0.42,  sum =  0.49
         3:  sin =  0.14,  cos = -0.99,  sum = -0.85
         4:  sin = -0.76,  cos = -0.65,  sum = -1.41
         5:  sin = -0.96,  cos =  0.28,  sum = -0.68
         6:  sin = -0.28,  cos =  0.96,  sum =  0.68
         7:  sin =  0.66,  cos =  0.75,  sum =  1.41
         8:  sin =  0.99,  cos = -0.15,  sum =  0.84
         9:  sin =  0.41,  cos = -0.91,  sum = -0.50
        10:  sin = -0.54,  cos = -0.84,  sum = -1.38
        11:  sin = -1.00,  cos =  0.00,  sum = -1.00
        12:  sin = -0.54,  cos =  0.84,  sum =  0.31
        13:  sin =  0.42,  cos =  0.91,  sum =  1.33

    So if start is -5 and threshold is 0.25 and:
       -- n is 3, then this function returns [-5, 0, 1]
             because sin(-5) + cos(-5) IS > 0.25 and
                     sin(-4) + cos(-4) is NOT > 0.25 and
                     sin(-3) + cos(-3) is NOT > 0.25 and
                     sin(-2) + cos(-2) is NOT > 0.25 and
                     sin(-1) + cos(-1) is NOT > 0.25 and
                     sin(0) + cos(0) IS > 0.25 and
                     sin(1) + cos(1) IS > 0.25 and
             and that makes the required  3  such numbers.
       -- n is 4, then this function returns [-5, 0, 1, 2]
       -- n is 5, then this function returns [-5, 0, 1, 2, 6]
       -- n is 6, then this function returns [-5, 0, 1, 2, 6, 7]
       -- n is 7, then this function returns [-5, 0, 1, 2, 6, 7, 8]

    while if start is -3 and the threshold is -1.0 and:
       -- n is 3, then this function returns [-1, 0, 1]
       -- n is 4, then this function returns [-1, 0, 1, 2]
       -- n is 5, then this function returns [-1, 0, 1, 2, 3]
       -- n is 6, then this function returns [-1, 0, 1, 2, 3, 5]

    and if n is 0 (regardless of what start is),
       this function returns []

    and if threshold is more than the square root of 2,
       this function returns (regardless of what start and n are):
          [start, start + 1, start + 2, ... start + n - 1].

    Type hints:
      :type start: int
      :type n:     int
      :type threshold: float
    """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above),
    #          but you are required to write ADDITIONAL tests (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   < 15 minutes.
    ###########################################################################


def run_test_practice_problem3():
    """ Tests the   practice_problem3b  function. """
    ###########################################################################
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  practice_problem3b  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #
    #   Try to choose tests that might expose errors in your code!
    #
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################

    # -------------------------------------------------------------------------
    # 13 tests, plus a 14th after these.
    # They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3b(-2, 2, 1.3)
    # and compare the returned value against [1, 7] (the correct answer).
    # -------------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3b,
                               [-2, 2, 1.3],
                               [1, 7]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 3, 0.25],
                               [-5, 0, 1]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 4, 0.25],
                               [-5, 0, 1, 2]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 5, 0.25],
                               [-5, 0, 1, 2, 6]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 6, 0.25],
                               [-5, 0, 1, 2, 6, 7]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 7, 0.25],
                               [-5, 0, 1, 2, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 3, -1.0],
                               [-1, 0, 1]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 4, -1.0],
                               [-1, 0, 1, 2]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 5, -1.0],
                               [-1, 0, 1, 2, 3]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 6, -1.0],
                               [-1, 0, 1, 2, 3, 5]),
             st.SimpleTestCase(practice_problem3b,
                               [30, 0, -1000],
                               []),
             st.SimpleTestCase(practice_problem3b,
                               [100, 5, 1.414],
                               [139, 183, 516, 560, 849]),
             st.SimpleTestCase(practice_problem3b,
                               [0, 1, 1.414213562373],
                               [286602]),
             ]
    # 14th test:
    big_list = []
    for k in range(888, 1888):
        big_list.append(k)
    tests.append(st.SimpleTestCase(practice_problem3b,
                                   [888, 1000,
                                    - math.sqrt(2) - 0.00000000001],
                                   big_list))

    # -------------------------------------------------------------------------
    # Run the 14 tests in the   tests   list constructed above.
    # -------------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3b', tests)

    ###########################################################################
    # TO DO 2 continued:  More tests:
    #      YOU add at least **   2   ** additional tests here.
    #
    # You can use the   SimpleTestCase  class as above, or use
    # the ordinary   expected/actual   way, your choice.
    #
    # SUGGESTION: Ask an assistant to CHECK your tests to confirm
    #             that they are adequate tests!
    ###########################################################################


def practice_problem3b(start, n, threshold):
    """
    What comes in:
      -- An integer:  start
      -- An nonnegative integer:  n
      -- A number:  threshold
    What goes out:  Returns a list of the first n integers,
      starting at start, for which the sum of the integer's
      sine and cosine is bigger than the given threshold.
    Side effects: None.
    Examples:
       practice_problem3b(-2, 2, 1.3)  returns  [1, 7]
    as you can see if you work through this example using
    the numbers presented below. (Do so!)

    For these examples, the following (and more) numbers
    (each is rounded to 2 decimal places for the sake of brevity)
    are relevant:
        -5:  sin =  0.96,  cos =  0.28,  sum =  1.24
        -4:  sin =  0.76,  cos = -0.65,  sum =  0.10
        -3:  sin = -0.14,  cos = -0.99,  sum = -1.13
        -2:  sin = -0.91,  cos = -0.42,  sum = -1.33
        -1:  sin = -0.84,  cos =  0.54,  sum = -0.30
         0:  sin =  0.00,  cos =  1.00,  sum =  1.00
         1:  sin =  0.84,  cos =  0.54,  sum =  1.38
         2:  sin =  0.91,  cos = -0.42,  sum =  0.49
         3:  sin =  0.14,  cos = -0.99,  sum = -0.85
         4:  sin = -0.76,  cos = -0.65,  sum = -1.41
         5:  sin = -0.96,  cos =  0.28,  sum = -0.68
         6:  sin = -0.28,  cos =  0.96,  sum =  0.68
         7:  sin =  0.66,  cos =  0.75,  sum =  1.41
         8:  sin =  0.99,  cos = -0.15,  sum =  0.84
         9:  sin =  0.41,  cos = -0.91,  sum = -0.50
        10:  sin = -0.54,  cos = -0.84,  sum = -1.38
        11:  sin = -1.00,  cos =  0.00,  sum = -1.00
        12:  sin = -0.54,  cos =  0.84,  sum =  0.31
        13:  sin =  0.42,  cos =  0.91,  sum =  1.33

    So if start is -5 and threshold is 0.25 and:
       -- n is 3, then this function returns [-5, 0, 1]
             because sin(-5) + cos(-5) IS > 0.25 and
                     sin(-4) + cos(-4) is NOT > 0.25 and
                     sin(-3) + cos(-3) is NOT > 0.25 and
                     sin(-2) + cos(-2) is NOT > 0.25 and
                     sin(-1) + cos(-1) is NOT > 0.25 and
                     sin(0) + cos(0) IS > 0.25 and
                     sin(1) + cos(1) IS > 0.25 and
             and that makes the required  3  such numbers.
       -- n is 4, then this function returns [-5, 0, 1, 2]
       -- n is 5, then this function returns [-5, 0, 1, 2, 6]
       -- n is 6, then this function returns [-5, 0, 1, 2, 6, 7]
       -- n is 7, then this function returns [-5, 0, 1, 2, 6, 7, 8]

    while if start is -3 and the threshold is -1.0 and:
       -- n is 3, then this function returns [-1, 0, 1]
       -- n is 4, then this function returns [-1, 0, 1, 2]
       -- n is 5, then this function returns [-1, 0, 1, 2, 3]
       -- n is 6, then this function returns [-1, 0, 1, 2, 3, 5]

    and if n is 0 (regardless of what start is),
       this function returns []

    and if threshold is more than the square root of 2,
       this function returns (regardless of what start and n are):
          [start, start + 1, start + 2, ... start + n - 1].

    Type hints:
      :type start: int
      :type n:     int
      :type threshold: float
    """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above),
    #          but you are required to write ADDITIONAL tests (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   < 15 minutes.
    ###########################################################################

def run_test_integers():
    """ Tests the    integers    function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  integers  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    #
    #   Try to choose tests that might expose errors in your code!
    #
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]
    answer = integers([(3, 1, 4),
                       (10, 'hi', 10),
                       [1, 2.5, 3, 4],
                       'hello',
                       [],
                       ['oops'],
                       [[55], [44]],
                       [30, -4]
                       ])
    print('Expected is:', expected)
    print('Actual is:  ', answer)


def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers
    in the subsequences of the given sequence, in the order that they
    appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    Type hints:
      :type sequence_of_sequences: (list|tuple) of (list|tuple|string)
      :rtype: list of int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    ###########################################################################
    # HINT: The
    #           type
    #       function can be used to determine the type of
    #       its argument (and hence to see if it is an integer).
    #       For example, you can write expressions like:
    #         -- if type(34) is int: ...
    #         -- if type(4.6) is float: ...
    #         -- if type('three') is str: ...
    #         -- if type([1, 2, 3]) is list: ...
    #       Note that the returned values do NOT have quotes.
    #       Also, the   is   operator tests for equality (like ==)
    #       but is more appropriate than == in this situation.
    # -------------------------------------------------------------------------
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------


def run_test_big_letters():
    """ Tests the    big_letters    function. """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this TEST function.
    #   It TESTS the  big_letters  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    # -------------------------------------------------------------------------
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   big_letters   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 'OTSSSOOPSAPSBOSCOPDOO'
    answer = big_letters([(3, 1, 4),  # not a string
                          'Ok what is ThiSSS?',  # OTSSS
                          (10, 'Ok what is ThiSSS?', 10),  # not a string
                          [],  # not a string
                          ['oops'],  # not a string
                          'oops',  #
                          ['OOPS'],  # not a string
                          '1 OOPS !',  # OOPS
                          'A',  # A
                          'ooPS $$&*#%&&',  # PS
                          'B',  # B
                          'oOpS',  # OS
                          'C',  # C
                          'OoPs'  # OP
                          'D',  # D
                          'OOps'  # OO
                          ])
    print('Expected is:', expected)
    print('Actual is:  ', answer)


def big_letters(sequence_of_sequences):
    """
    Returns a new STRING that contains all the upper-case letters
    in the subsequences of the given sequence that are strings,
    in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),                          # not a string
        'Ok what is ThiSSS?',                # OTSSS
        (10, 'Ok what is ThiSSS?', 10),      # not a string
        [],                                  # not a string
        ['oops'],                            # not a string
        'oops',                              #
        ['OOPS'],                            # not a string
        '1 OOPS !',                          # OOPS
        'A',                                 # A
        'ooPS $$&*#%&&',                     # PS
        'B',                                 # B
        'oOpS',                              # OS
        'C',                                 # C
        'OoPs'                               # OP
        'D',                                 # D
        'OOps'                               # OO
         ]
    then this function returns:
        'OTSSSOOPSAPSBOSCOPDOO'

    Precondition:  the given argument is a sequence of sequences.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    ###########################################################################
    # IMPORTANT:
    #   There is a STRING METHOD that determines whether or not
    #   a string contains upper-case letters.  To find that method,
    #   somewhere in this file type:
    #           "".
    #   and pause after the dot.
    #   That will display ALL the STRING methods.
    #
    #   Look for a method whose name begins with
    #           is
    #       e.g.   isalnum()  isdigit() ... [but find the one for upper]
    #
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  12 minutes.
    # -------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()