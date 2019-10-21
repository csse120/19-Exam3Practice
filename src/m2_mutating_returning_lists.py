"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  MUTATING  and  RETURNING-NEW  LISTS.  ***

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  [Note: same _TODO_ as its matching one in module m1.]
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_doubler()
    run_test_zero_changer()


def run_test_doubler():
    """ Tests the    doubler    function. """
    # -------------------------------------------------------------------------
    # TODO: 3. READ the tests that we supplied in this function, asking
    #  questions as needed.  Once you UNDERSTAND the tests that we supplied,
    #  ADD A PAIR OF TESTS of your own for the   double  function,
    #  using the same style for testing as we did.
    #  __
    #   Try to choose a test that might expose errors in your code!
    #  __
    #   As usual, compute the EXPECTED results BY HAND
    #   (not by running your program).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   doubler   function:')
    print('--------------------------------------------------')

    format_string = '    doubler( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1: Tests whether the function RETURNS the correct value.
    # -------------------------------------------------------------------------
    seq_of_lists_1 = ([10, 3, 101], [8, 0], [-20, 5, 1, 2, 3, 4, 5], [])
    seq_of_lists_2 = ([101], [-20, 5, 1, 2, 3, 4, 5], [], [50, 40])
    # After the function call, seq_of_lists should be as follows:
    expected_mutated = ([20, 6, 202], [16, 0], [-40, 10, 2, 4, 6, 8, 10], [])
    expected_returned = ([202], [-40, 10, 2, 4, 6, 8, 10], [], [100, 80])

    print_expected_result_of_test([seq_of_lists_1, seq_of_lists_2],
                                  expected_returned,
                                  test_results, format_string)
    actual = doubler(seq_of_lists_1, seq_of_lists_2)

    print_actual_result_of_test(expected_returned, actual, test_results)
    print('The above is for the RETURNED VALUE from this test.')
    print('The NEXT test will be similar but testing the MUTATED list.')

    # Test 2: (a continuation of Test 1)
    #   Tests whether the function MUTATES the sub-lists correctly.
    print_actual_result_of_test(expected_mutated, seq_of_lists_1, test_results)
    print('The above is for the MUTATED list.')
    # -------------------------------------------------------------------------

    # Test 1:
    arg1 = [10, -3, 20, 4]
    arg2 = [5, 0, 8]
    correct_arg1_after = [20, -6, 40, 8]
    correct_arg2_after = [5, 0, 8]
    expected = [10, 0, 16]

    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)
    print('  Argument 2 is:', arg2)

    answer = doubler(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)
    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)
    print('The returned value is:       ', answer)
    print('The returned value should be:', expected)

    # -------------------------------------------------------------------------
    # TO DO 2 (continued): Add your ADDITIONAL test(s) here:
    # -------------------------------------------------------------------------

    print()
    print('------------------------------------------------------')
    print('Testing the   multiply_by_c   function:')
    print('------------------------------------------------------')

    format_string = '    multiply_by_c( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.



    # -------------------------------------------------------------------------
    # Test 3: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = ([4, 2, 1], [8, 0], [1, 2, 3, 4, 5], [], [101])
    c = 2  # Each number in each sub-list should be multiplied by this
    # After the function call, seq_of_lists should be as follows:
    expected = ([8, 4, 2], [16, 0], [2, 4, 6, 8, 10], [], [202])
    print_expected_result_of_test([c, seq_of_lists], expected,
                                  test_results, format_string)
    actual = multiply_by_c(c,
                           seq_of_lists)
    print_actual_result_of_test(expected, seq_of_lists, test_results)
    print('The above is for  seq_of_lists  (whose lists should be MUTATED.')

    # Test 4: (a continuation of Test 3)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([c, seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print('The above is for the RETURNED VALUE, which should be')
    print('the constant None, NOT the STRING "None".')
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 5: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = [[], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300],
                    [5, 5], [], [-10, 4]]
    c = 100  # Each number in each sub-list should be multiplied by this
    # After the function call, seq_of_lists should be as follows:
    expected = [[], [100], [2000, 200, 3000, 400, 10000, 800, 200, 200, 200],
                [], [30000], [500, 500], [], [-1000, 400]]
    print_expected_result_of_test([c, seq_of_lists], expected,
                                  test_results, format_string)
    actual = multiply_by_c(c,
                           seq_of_lists)
    print_actual_result_of_test(expected, seq_of_lists, test_results)
    print('The above is for  seq_of_lists  (whose lists should be MUTATED.')

    # Test 6: (a continuation of Test 5)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([c, seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print('The above is for the RETURNED VALUE, which should be')
    print('the constant None, NOT the STRING "None".')
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def doubler(seq_of_lists_1, seq_of_lists_2):
    """
    Both arguments are sequences of lists, where each sub-list contains
    only numbers.  This function:
      -- MUTATEs each number in each sub-list of list1 by doubling each number
           in the sub-list
    and
      -- RETURNs a new list that is the same as list2 but with each
           number in the list doubled.

    For example, if the two arguments are:
       [10, -3, 20, 4]  and  [5, 0, 8]
    then this method MUTATEs the first argument to [20, -6, 40, 8]
    and RETURNs the list [10, 0, 16]

    Preconditions:
        :type list1: list of int
        :type list2: list of int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------
    for k in range(len(list1)):
        sublist = list1[k]
        for j in range(len(sublist)):
            sublist[j] = sublist[j] * 2
    result = []
    for k in range(len(list2)):
        for j in range(len(sublist)):
            result.append(list2[k] * 2)
    return result


def run_test_zero_changer():
    """ Tests the    zero_changer    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   zero_changer   function:')
    print('--------------------------------------------------')

    # Test 1:
    test1 = ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
    expected1 = ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    zero_changer(test1)
    print()
    print('Test 1:')
    print('  Expected:', expected1)
    print('  Actual:  ', test1)

    # -------------------------------------------------------------------------
    # TODO: 2. Write at least 2 additional tests for the
    #    zero_changer
    # function.  Try to choose some unexpected things like empty lists
    # or an empty tuple, or a list with no zeros, etc.
    # -------------------------------------------------------------------------


def zero_changer(tuple_of_lists):
    """
    What comes in:  A TUPLE of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., none)
    Side effects:  The argument is MUTATED so that:
      -- the 1st 0 in the given tuple of lists is changed to 1.
      -- the 2nd 0 in the given tuple of lists is changed to 2.
      -- the 3rd 0 in the given tuple of lists is changed to 3.
           etc.
    Example:
      If the given tuple of lists is:
          ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
      then AFTER this function is called with that tuple of lists,
      the tuple of lists has been MUTATED to:
          ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    Note that:
      -- If there are no zeros in the given tuple of lists,
           then this function does nothing.
      -- After this function call, the tuple of lists IN THE CALLER
           should contain no zeros.
    Type hints:
      :type tuple_of_lists: tuple of list[int]
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
