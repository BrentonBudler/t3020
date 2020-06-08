

import urllib
import urllib.request
import ssl
import sys


#e.g. run as
# python3 datamunger.py https://raw.githubusercontent.com/shaze/t3020/master/data.csv
# fetches the data from the repo
# or
# python3 datamunger.py see.csv
# gets data from same directory

origin=sys.argv[1]

def calc_total(curr):
    computed=0
    for c in curr[1:9]: #E1
        computed=computed+c
    return computed


def check_monotonic(n,prev,curr):
   # Now check monotonicity and update  prev so next time round we compare
   # against this row
    for i in range(9):
        if curr[i] <  prev[i]:  #E2
            print("Monotonic error at column %d comparing lines %d and %d  "%(i,n-1,n),
                     "values %d and %d"%(curr[i],prev[i]))
        prev[i]=curr[i]  


def check_row(n, prev, curr_str):
    data = curr_str
    curr = []
    for d in data: #E3
        try:
            v = int(d)
            curr.append(v)
        except ValueError:  # missing data so can't convert
            return False
    computed = calc_total(curr)
    if computed != curr[0]:
        print("Sum error at line ",n, curr_str,
              "computed %d and expected %d"%(computed, curr[0]))
    check_monotonic(n,prev, curr)
    return True # if there all data was there


def main():
    if "http" in origin:
        ctx = ssl._create_unverified_context()
        inp = urllib.request.urlopen(origin, context=ctx)
        def get_text(x):  # for URL we need to convert from byte to string
            return x.decode('utf-8')
    else:
        inp = open(origin)
        def get_text(x): # does nothing in case of local files
            return x
    inp.readline() # skip the header
    prev = [0,0,0,0,0,0,0,0,0,0]
    missing=0
    n=1
    for  line in inp:
        n=n+1
        str_vals  = get_text(line).strip().split(",")
        ok = check_row(n,prev,str_vals)
        if not ok:
            missing = missing+1
    print("There were ",missing," missing lines")

if __name__=="__main__":
    main()
