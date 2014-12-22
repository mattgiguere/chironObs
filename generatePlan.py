#!/usr/bin/env python

"""
Created on 2014-07-29T12:49:11
"""

from __future__ import division, print_function
import sys
import argparse
import datetime


__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'


def generatePlan():
    """PURPOSE: To generate a comma-delimited observing plan that will then
    be used by addChironObs.py to add it to the database."""

    #the starting object sequence in the plan:
    object_seq = 10

    #the date you would like your observations to start:
    date = datetime.datetime(2014, 8, 1)

    #the comment message to add to each observation:
    obj_comment = 'Please observe on '+date.strftime('%Y-%m-%d')

    #the header row. these are the columns in the object TABLE
    #of the MySQL database that stores all the CHIRON information:
    header = ['object_id', 'plan_id', 'decker_id', 'cycle_id',
              'object_id_attach', 'object_attach_seq', 'object_type',
              'object_name', 'object_seq', 'object_ra', 'object_dec',
              'object_epoch', 'object_vmag', 'object_num_exp',
              'object_iodine_in', 'object_day_ok', 'object_priority',
              'object_exp_time', 'object_snr', 'object_reduce',
              'object_status', 'object_scheduled_date', 'object_comments',
              'object_optimal_start']

    #the list of nightly observations:
    hr472n = ['NULL', 247, 4, 0, 0, 0, 'Science', 'HR 472', object_seq,
              24.4285, -57.2368, 'J2000', 0.5, 3, 'Yes', 'No', 'High',
              28, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']

    tauCeti_Iout = ['NULL', 247, 4, 0, 0, 0, 'Science', '10700',
                    object_seq, 26.017, -15.9375, 'J2000', 3.5, 1, '', 'No',
                    'High', 555, 0, 'Yes', 'Unscheduled', 'None',
                    obj_comment, 'None']
    tauCeti_I2B = ['NULL', 247, 3, 0, 0, -1, 'Standard', '10700',
                   object_seq, 26.017, -15.9375, 'J2000', 3.5, 4, 'Yes', 'No',
                   'High', 383, 0, 'Yes', 'Unscheduled', 'None',
                   obj_comment, 'None']
    tauCeti_I2A = ['NULL', 247, 3, 0, 0, 1, 'Standard', '10700',
                   object_seq, 26.017, -15.9375, 'J2000', 3.5, 3, 'Yes', 'No',
                   'High', 383, 0, 'Yes', 'Unscheduled', 'None',
                   obj_comment, 'None']
    hr472 = ['NULL', 247, 3, 0, 0, 0, 'Science', 'HR 472', object_seq,
             24.4285, -57.2368, 'J2000', 0.5, 3, 'Yes', 'No', 'High',
             15, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']

    epsEri_Iout = ['NULL', 247, 4, 0, 0, 0, 'Science', '22049', object_seq,
                   53.2327, -9.45826, 'J2000', 3.73, 1, '', 'No', 'High',
                   740, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']
    epsEri_I2B = ['NULL', 247, 3, 0, 0, -1, 'Standard', '22049', object_seq,
                  53.2327, -9.45826, 'J2000', 3.73, 1, 'Yes', 'No', 'High',
                  386, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']
    epsEri_I2A = ['NULL', 247, 3, 0, 0, 1, 'Standard', '22049', object_seq,
                  53.2327, -9.45826, 'J2000', 3.73, 1, 'Yes', 'No', 'High',
                  386, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']
    hd20794 = ['NULL', 247, 3, 0, 0, 0, 'Science', '20794', object_seq,
               49.9819, -43.0698, 'J2000', 4.3, 3, 'Yes', 'No', 'High',
               664, 200, 'Yes', 'Unscheduled', 'None', obj_comment, 'None']

    f = open('2014BObservingPlan.txt', 'w')
    f.write(','.join(header)+'\n')

    for i in range(183):
        obj_comment = 'Please observe on '+date.strftime('%Y-%m-%d')
        hr472n[8] = object_seq
        hr472n[-2] = obj_comment
        f.write(','.join(str(x) for x in hr472n)+'\n')

        object_seq += 1
        hr472[8] = object_seq
        hr472[-2] = obj_comment
        f.write(','.join(str(x) for x in hr472)+'\n')

        object_seq += 1
        tauCeti_Iout[8] = object_seq
        tauCeti_Iout[-2] = obj_comment
        f.write(','.join(str(x) for x in tauCeti_Iout)+'\n')
        tauCeti_I2B[8] = object_seq
        tauCeti_I2B[-2] = obj_comment
        f.write(','.join(str(x) for x in tauCeti_I2B)+'\n')
        tauCeti_I2A[8] = object_seq
        tauCeti_I2A[-2] = obj_comment
        f.write(','.join(str(x) for x in tauCeti_I2A)+'\n')

        object_seq += 1
        hr472[8] = object_seq
        f.write(','.join(str(x) for x in hr472)+'\n')

        object_seq += 1
        epsEri_Iout[8] = object_seq
        epsEri_Iout[-2] = obj_comment
        f.write(','.join(str(x) for x in epsEri_Iout)+'\n')
        epsEri_I2B[8] = object_seq
        epsEri_I2B[-2] = obj_comment
        f.write(','.join(str(x) for x in epsEri_I2B)+'\n')
        epsEri_I2A[8] = object_seq
        epsEri_I2A[-2] = obj_comment
        f.write(','.join(str(x) for x in epsEri_I2A)+'\n')

        object_seq += 1
        hr472[8] = object_seq
        f.write(','.join(str(x) for x in hr472)+'\n')

        object_seq += 1
        hd20794[8] = object_seq
        hd20794[-2] = obj_comment
        f.write(','.join(str(x) for x in hd20794)+'\n')
        object_seq += 1
        date += datetime.timedelta(days=1)
    f.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='argparse object.')
    parser.add_argument(
        'arg1',
        help='This argument does something.', nargs='?')
    parser.add_argument(
        'arg2',
        help='This argument does something else. By specifying ' +
             'the "nargs=>" makes this argument not required.',
             nargs='?')
    if len(sys.argv) > 3:
        print('use the command')
        print('python filename.py tablenum columnnum')
        sys.exit(2)

    args = parser.parse_args()

    #generatePlan(int(args.arg1), args.arg2)
    generatePlan()
