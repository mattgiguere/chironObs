
#!/usr/bin/env python

"""
Created on 2014-07-27T21:32:27
"""

from __future__ import division, print_function
import sys
import argparse

try:
    import numpy as np
except ImportError:
    print('You need numpy installed')
    sys.exit(1)
import pandas as pd
import subprocess
import pymysql

__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'


def addChironObs():
    """PURPOSE: To read in a comma-delimited plan from file and write the
    contents to the CHIRON database at the beginning of the semester."""
    newPlan = pd.read_csv('2014BObservingPlan.txt', sep=',', header=0)
    newPlan = newPlan.where((pd.notnull(newPlan)), None)
    conn = connectChiron()
    pd.io.sql.write_frame(newPlan[newPlan.object_type == 'Science'], 'objects',
                          conn, flavor='mysql', if_exists='append')
    SciencePlan = newPlan[newPlan.object_type == 'Science']
    cur = conn.cursor()
    for i in range(len(newPlan[newPlan.object_type == 'Science'])):
        object_seq = SciencePlan.loc[SciencePlan.index[i], 'object_seq']
        #print(object_seq)
        cmd = ("SELECT object_id FROM objects WHERE plan_id=247 "
               "AND object_seq="+str(object_seq))
        cur.execute(cmd)
        new_obj_id = cur.fetchall()
        newPlan.loc[newPlan.object_seq == object_seq,
                    'object_id_attach'] = new_obj_id[0][0]
    pd.io.sql.write_frame(newPlan[newPlan.object_type == 'Standard'],
                          'objects', conn, flavor='mysql', if_exists='append')


def connectChiron():
    """connect to the database"""
    #retrieve credentials:
    cmd = 'echo $AeroFSdir'
    #read in the AeroFSdir string and
    #chop off the newline character at the end
    cdir = subprocess.check_output(cmd, shell=True)
    cdir = cdir[0:len(cdir)-1]
    credsf = open(cdir+'.credentials/SQL/ceaye', 'r')
    creds = credsf.read().split('\n')
    conn = pymysql.connect(host=creds[0],
                           port=int(creds[1]),
                           user=creds[2],
                           passwd=creds[3],
                           db=creds[4])
    #cur = conn.cursor()
    return conn

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
        print('python filename.py')
        sys.exit(2)

    args = parser.parse_args()

    #addChironObs(int(args.arg1), args.arg2)
    addChironObs()

