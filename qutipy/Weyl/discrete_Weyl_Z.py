'''
This code is part of QuTIpy.

(c) Copyright Sumeet Khatri, 2021

This code is licensed under the Apache License, Version 2.0. You may
obtain a copy of this license in the LICENSE.txt file in the root directory
of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.

Any modifications or derivative works of this code must retain this
copyright notice, and modified files need to carry a notice indicating
that they have been altered from the originals.
'''


import numpy as np

from qutipy.general_functions import ket,dag


def discrete_Weyl_Z(d):

    '''
    Generates the Z phase operators.
    '''

    w=np.exp(2*np.pi*1j/d)

    Z=ket(d,0)@dag(ket(d,0))

    for i in range(1,d):
        Z=Z+w**i*ket(d,i)@dag(ket(d,i))

    return Z