'''------------------------------------
CONSTANTS FOR THE ENTIRE PROJECT
------------------------------------'''

'''------------------------------------
CONSTANTS FOR SPLITTING
------------------------------------'''
# threshold to detect a bark
# this value is because of the output of normalization

VALUE = 100000000
VALUE2 =    0.320 #320

#TODO add value

MULTIPLIER = 1

MIN_VAL_FOR_SPLITTING = VALUE2 * MULTIPLIER
MIN_VAL = VALUE * MULTIPLIER

# amount of time to skip after detecting a bark (in seconds)
SECONDS = 0.25

# seconds until program will record for another bark sequence
SECONDS_UNTIL_NEXT_BARK_SEQUENCE = .5

'''------------------------------------
CONSTANTS FOR NORMALIZATION
------------------------------------'''
TARGET_DBFS = -17.5

'''------------------------------------
CONSTANTS FOR FEATURE EXTRACTION
------------------------------------'''
# in decimal format
PERCENT_OF_MAX = .5

'''------------------------------------
CONSTANTS FOR SVM PORTION
------------------------------------'''
# ONLY CHANGE TRAIN_PERCENT
TRAIN_PERCENT = .80
