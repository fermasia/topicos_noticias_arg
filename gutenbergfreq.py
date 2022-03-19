#!/usr/bin/env python
# coding: utf-8

import collections
import glob
import os
import re
import string


if __name__ == '__main__':
    
    # pattern = re.compile('[\W_]+')
    # for path in glob.glob('/media/mtc/Data/tmp/gberg-*'):
    #     counter = collections.Counter()
    #     outfile = '%s.freq' % path
    #     print(path, outfile)
    #     if os.path.exists(outfile):
    #         continue
    #     with open(path) as handle:
    #         for line in handle:
    #             line = line.lower()
    #             for token in line.split():
    #                 token = pattern.sub('', token)
    #                 if token:
    #                     counter[token] += 1
    #     with open('%s.freq' % path, 'w') as output:
    #         for key, value in counter.iteritems():
    #             output.write('%s\t%s\n' % (key, value))

    counter = collections.Counter()
    for i, path in enumerate(glob.glob('/media/mtc/Data/tmp/gberg-*freq')):
        with open(path) as handle:
            print(path, len(counter), i)
            for line in handle:
                token, frequency = line.strip().split()
                frequency = int(frequency)
                if len(token) > 30:
                    continue
                else:
                    counter[token] += frequency

    with open('./gutenberg.freq', 'w') as output:
        for key, value in counter.iteritems():
            output.write('%s\t%s\n' % (key, value))
