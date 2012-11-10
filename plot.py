#! /usr/bin/env python

#    Copyright (C) 2012  Club Capra - capra.etsmtl.ca
#
#    This file is part of CapraVision.
#    
#    CapraVision is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import sys
import tempfile
import matplotlib.pyplot as plt

def create_graphic(data_file):
    data = np.fromfile(data_file, np.float16)
    data = data.reshape((2, len(data) / 2))
    import logging
    logging.basicConfig(filename='/home/benoit/errorz.txt')
    precisions = data[0, :]
    noises = data[1, :]
    logging.error(precisions)
    logging.error('hello!')
    logging.error(noises)
    plt.clf()
    plt.plot(noises, precisions, '.b')
    plt.xlabel('Noise (%)')
    plt.ylabel('Precision (%)')
    #plt.xlim(0, np.max(precisions))
    #plt.ylim(0, np.max(noises))
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    ntf = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    plt.savefig(ntf.file)
    ntf.flush()
    file_name = ntf.name
    ntf.close()
    return file_name

if __name__ == '__main__':
    data_file = sys.argv[1] 
    image_file = create_graphic(data_file)
    print image_file
    sys.stdout.flush()
    
    