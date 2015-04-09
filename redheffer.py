#Based on math research under the supervision of Dr. Zhongshan Li at Georgia State University
#
#Python Model of a Redheffer Matrix
#



import numpy as np
import scipy as sp
from math import floor
import networkx as nx
import matplotlib.pyplot as plt
from numberTheory import mu, sumOfMu, mertens

__Author__ = 'Kevin Slote'


def graph_from_matrix(matrix, tex):
    G=nx.from_numpy_matrix(matrix, create_using=nx.MultiDiGraph())
    plt.title(r'{0}'.format(tex))
    nx.draw(G)
    plt.savefig("path_graph1.png")
    plt.show()


def redheffer_matrix(n):
    a = np.zeros((n+1,n+1))
    for i in xrange(1, n+1):
        a[i,1] = 1
        for j in xrange(1,n+1):
            if j%i == 0:
                 #print i,j
                 a[i,j] = 1
    sp.delete(a, 0, 0 )

    a = np.delete(a, (0), axis=0)
    a = np.delete(a, (0), axis=1)    
    return a

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

if __name__ == '__main__':
    for n in xrange(1, 50):
        a = redheffer_matrix(n)
        print a
        latex = "For $n={0}$,  $M(n)={1}$, $Det(R_n)= {2}$".format(n, mertens(n), np.linalg.det(a))
        #raw_input('...any key..')
        graph_from_matrix(a, latex)
