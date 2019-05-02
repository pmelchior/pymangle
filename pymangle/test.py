from __future__ import with_statement, print_function
import sys, os
import tempfile
import warnings
import numpy as np

from .mangle import Mangle

import unittest

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRead)
    res=unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()

    if not res :
        sys.exit(1)


class TestRead(unittest.TestCase):

    def testStandardUnpixelized(self):
        """
        a basic mask with standard header, no pixelization
        """

        text="""3 polygons
snapped
polygon 0 ( 4 caps, 1 weight, 0 pixel, 0.101732020850849 str):
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 -0.2568551745226059
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 1.422618261740699
  0.2367814257465403  0.0207156904863277 -0.9713420698132612 1
  0.1515445107781580  0.0132584267126710 -0.9883615104677608 -1
polygon 1 ( 4 caps, 1 weight, 0 pixel, 0.054242425709277 str):
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 -0.2568551745226059
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 1.5
  0.1515445107781580  0.0132584267126710 -0.9883615104677608 1
  0.1084526035253447  0.0094883733383393 -0.9940563382223196 -1
polygon 2 ( 4 caps, 1 weight, 0 pixel, 0.302363552547417 str):
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 -0.2568551745226059
  0.0871557427476579 -0.9961946980917455  0.0000000000000001 1.642787609686539
  0.1084526035253447  0.0094883733383393 -0.9940563382223196 1
 -0.1084526035253447 -0.0094883733383393 -0.9940563382223196 -1\n"""

        fname=tempfile.mktemp(prefix='mangle-StandardUnpixelized-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)

    def testStandardPixelized(self):
        """
        standard header with pixel
        """


        text="""3 polygons
pixelization 9s
snapped
balkanized
polygon 0 ( 4 caps, 1 weight, 87381 pixel, 0.000000000129178 str):
  0.9999999991588143  0.0000410152374105  0.0000003490658505 0.998159921767887
  0.9659041924494473 -0.2588997625991339 -0.0000627271332757 -0.9982831417433783
 -0.0000000000000000  1.0000000000000000  0.0000000000000000 1
 -0.0122715382857199  0.9999247018391445  0.0000000000000000 -1
polygon 1 ( 4 caps, 1 weight, 87381 pixel, 0.000000067701897 str):
 -0.9647577286061684 -0.2584481766449109  0.0494678186661570 -1
  0.2587637821532441 -0.9659406319340194 -0.0000249931148859 -0.9872370563678581
 -0.0122715382857199  0.9999247018391445  0.0000000000000000 -1
  0.0000000000000000  0.0000000000000000  1.0000000000000000 0.00390625
polygon 2 ( 5 caps, 1 weight, 87381 pixel, 0.000000311118396 str):
 -0.9647577286061684 -0.2584481766449109  0.0494678186661570 1
  0.2587637821532441 -0.9659406319340194 -0.0000249931148859 -0.9872370563678581
 -0.9987456407765712  0.0000501504038277  0.0500713742045613 -1
 -0.0122715382857199  0.9999247018391445  0.0000000000000000 -1
  0.0000000000000000  0.0000000000000000  1.0000000000000000 0.00390625\n"""


        fname=tempfile.mktemp(prefix='mangle-Pixelized-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        if os.path.exists(fname):
            os.remove(fname)


    def testNopixel(self):
        """
        standard header with no pixels in the header
        """

        text="""3 polygons
polygon                      0 ( 4 caps,            1.0000000 weight,   0.0074088006084970 str):
 -0.06081623141086969775  -0.00532073080682029988   0.99813479842186692004  -1.00000000000000000000
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000  -0.21198924639327809682
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000   1.90996127087654299359
 -0.06515425057767830486  -0.00570025830607420042   0.99785892323860347908   1.00000000000000000000
polygon                      1 ( 4 caps,            1.0000000 weight,   0.0116826109771030 str):
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000   1.88539361956466899883
 -0.06081623141086969775  -0.00532073080682029988   0.99813479842186692004   1.00000000000000000000
 -0.05387300028307989708  -0.00471327679489840033   0.99853667176641747183  -1.00000000000000000000
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000  -0.21198924639327809682
polygon                      2 ( 4 caps,            1.0000000 weight,   0.0022611252679780 str):
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000   1.50753836296070398149
 -0.05387300028307989708  -0.00471327679489840033   0.99853667176641747183   1.00000000000000000000
 -0.05213680212878300108  -0.00456137913876279982   0.99862953475457394426  -1.00000000000000000000
  0.08715574274765790219  -0.99619469809174554520   0.00000000000000010000  -0.21198924639327809682\n"""

        fname=tempfile.mktemp(prefix='mangle-Nopixel-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)


    def testWeightOnly(self):
        """
        standard header with only weight in addition to caps
        """

        text="""4 polygons
polygon 1 ( 4 caps, 1 weight ):
0.0000000000 0.0000000000 1.0000000000 1.0174524064
0.0000000000 0.0000000000 1.0000000000 -0.8781306566
0.5000000000 0.8660254038 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 2 ( 4 caps, 1 weight ):
0.0000000000 0.0000000000 1.0000000000 1.1218693434
0.0000000000 0.0000000000 1.0000000000 -1.0174524064
-0.4617486132 0.8870108332 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 3 ( 4 caps, 1 weight ):
0.0000000000 0.0000000000 1.0000000000 1.0348994967
0.0000000000 0.0000000000 1.0000000000 -0.9128442573
-0.7933533403 -0.6087614290 0.0000000000 1.0000000000
0.7071067812 -0.7071067812 0.0000000000 -1.0000000000
polygon 4 ( 4 caps, 1 weight ):
0.0000000000 0.0000000000 1.0000000000 0.3244097924
0.0000000000 0.0000000000 1.0000000000 -0.3053416295
0.3420201433 -0.9396926208 0.0000000000 1.0000000000
0.9396926208 -0.3420201433 0.0000000000 -1.0000000000\n"""

        fname=tempfile.mktemp(prefix='mangle-Weight-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)


    def testMinimalNonStandard(self):
        """
        absolutely minimal header, non standard
        """

        text="""4 polygons
polygon 1 4
0.0000000000 0.0000000000 1.0000000000 1.0174524064
0.0000000000 0.0000000000 1.0000000000 -0.8781306566
0.5000000000 0.8660254038 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 2 4
0.0000000000 0.0000000000 1.0000000000 1.1218693434
0.0000000000 0.0000000000 1.0000000000 -1.0174524064
-0.4617486132 0.8870108332 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 3 4
0.0000000000 0.0000000000 1.0000000000 1.0348994967
0.0000000000 0.0000000000 1.0000000000 -0.9128442573
-0.7933533403 -0.6087614290 0.0000000000 1.0000000000
0.7071067812 -0.7071067812 0.0000000000 -1.0000000000
polygon 4 4
0.0000000000 0.0000000000 1.0000000000 0.3244097924
0.0000000000 0.0000000000 1.0000000000 -0.3053416295
0.3420201433 -0.9396926208 0.0000000000 1.0000000000
0.9396926208 -0.3420201433 0.0000000000 -1.0000000000\n"""

        fname=tempfile.mktemp(prefix='mangle-MinimalNonStandard-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)


    def testMinimalNonStandardNopolycount(self):
        """
        absolutely minimal header, non standard, without even
        the polygon count
        """

        text="""polygon 1 4
0.0000000000 0.0000000000 1.0000000000 1.0174524064
0.0000000000 0.0000000000 1.0000000000 -0.8781306566
0.5000000000 0.8660254038 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 2 4
0.0000000000 0.0000000000 1.0000000000 1.1218693434
0.0000000000 0.0000000000 1.0000000000 -1.0174524064
-0.4617486132 0.8870108332 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 3 4
0.0000000000 0.0000000000 1.0000000000 1.0348994967
0.0000000000 0.0000000000 1.0000000000 -0.9128442573
-0.7933533403 -0.6087614290 0.0000000000 1.0000000000
0.7071067812 -0.7071067812 0.0000000000 -1.0000000000
polygon 4 4
0.0000000000 0.0000000000 1.0000000000 0.3244097924
0.0000000000 0.0000000000 1.0000000000 -0.3053416295
0.3420201433 -0.9396926208 0.0000000000 1.0000000000
0.9396926208 -0.3420201433 0.0000000000 -1.0000000000\n"""

        fname=tempfile.mktemp(prefix='mangle-MinimalNonStandard-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)


    def testExtraLines(self):
        """
        extra line at the end
        """

        text="""polygon 1 4
0.0000000000 0.0000000000 1.0000000000 1.0174524064
0.0000000000 0.0000000000 1.0000000000 -0.8781306566
0.5000000000 0.8660254038 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 2 4
0.0000000000 0.0000000000 1.0000000000 1.1218693434
0.0000000000 0.0000000000 1.0000000000 -1.0174524064
-0.4617486132 0.8870108332 0.0000000000 1.0000000000
-0.6427876097 0.7660444431 0.0000000000 -1.0000000000
polygon 3 4
0.0000000000 0.0000000000 1.0000000000 1.0348994967
0.0000000000 0.0000000000 1.0000000000 -0.9128442573
-0.7933533403 -0.6087614290 0.0000000000 1.0000000000
0.7071067812 -0.7071067812 0.0000000000 -1.0000000000
polygon 4 4
0.0000000000 0.0000000000 1.0000000000 0.3244097924
0.0000000000 0.0000000000 1.0000000000 -0.3053416295
0.3420201433 -0.9396926208 0.0000000000 1.0000000000
0.9396926208 -0.3420201433 0.0000000000 -1.0000000000\n
        \n"""

        fname=tempfile.mktemp(prefix='mangle-MinimalNonStandard-',suffix='.ply')
        with open(fname,'w') as fobj:
            fobj.write(text)

        m = Mangle(fname)
        ra,dec = m.genrand(3)
        if os.path.exists(fname):
            os.remove(fname)



if __name__ == '__main__':
    test()
