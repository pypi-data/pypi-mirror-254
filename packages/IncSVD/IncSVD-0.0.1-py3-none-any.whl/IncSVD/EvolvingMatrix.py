"""EvolvingMatrix class for updating the truncated singular value decomposition (SVD) of evolving matrices.
"""

import time
import math
import numpy as np
import scipy.sparse
from scipy.sparse import csr_matrix, csc_matrix, vstack, hstack
import numpy as np
from .svd_update import (
    kalantzis1_update,
    zhasimon_update,
)
from tqdm import tqdm

msg_len = 60

class EvolvingMatrix(object):
    """
    Parameters
    ----------
    network : bool
        True - matrix represents a network (i.e., #rows = #cols, updates include row updates and cols updates)
        False - only update rows, i.e., a user-item matrix

    sparse : bool, default=True
        True - matrix is sparse: Use our sparse matrix acceleration method for SVD computation
        False - matrix is dense: Use the original methods (z-s, vecharynski, random)

    k_dim : int
        Rank of truncated SVD to be calculated

    method : string, default='z-s'
        method for SVD update
        choose from ['z-s', 'vecharynski', 'random']

    init : int
        number of rows to perform the initial SVD decomposition

    Attributes
    ----------
    data : ndarray of shape (m_dim, n_dim)
        The entire matrix, including the initially defined parts and subsequent additions
    
    m_dim : int
        Number of rows in data matrix

    n_dim : int
        Number of columns in data matrix
            Does not change in non-Network case
            =m_dim in Network case

    SVDmatrix : ndarray of shape [(init, init) - for network=True] [(init, n_dim) - for network=False]
        The matrix used for the initial calculation of the SVD
    
    svd_mdim : int
        The number of rows in the matrix for which the SVD has been computed
        (for network=True, also represents the number of cols)

    res_m_dim : int
        Number of rows in matrix to be appended
        (for network=True, also represents the number of cols)

    [Only for Network=False] append_matrix : ndarray of shape (res_m_dim, n_dim)
        The matrix to be appended for non-network matrix

    [Only for Network=True] append_rows : ndarray of shape (res_m_dim, n_dim)
        The row matrix to be appended for network matrix

    [Only for Network=True] append_cols : ndarray of shape (m_dim, res_m_dim)
        The row matrix to be appended for network matrix
    
    Uk, sigmak, VHk : ndarrays of shape (init, k), (k,), (n, k) [for network=True, n=init, for network=False, n=n_dim]
        The initial truncated SVD

    ----
    
    update_matrix : ndarray of shape (u, n)
        Matrix to be appended directly

    phi : int
        Current update index

    n_appended : int
        Number of rows appended in last update

    n_appended_total : int
        Number of rows appended in all updates

    runtime : float
        Total runtime for updates

    SVDinitialized : bool
        Flag for whether SVD initialization has been performed. 
        Updates cannot be performed until SVD initialization has been performed.

    step_length : int
        The step length of each update, which can be not fixed
        Can be modified by SetStepLength()



    References
    ----------
    V. Kalantzis, G. Kollias, S. Ubaru, A. N. Nikolakopoulos, L. Horesh, and K. L. Clarkson,
        “Projection techniquesto update the truncated SVD of evolving matrices with applications,”
        inProceedings of the 38th InternationalConference on Machine Learning,
        M. Meila and T. Zhang, Eds.PMLR, 7 2021, pp. 5236-5246.

    Mina Ghashami et al. “Frequent Directions: Simple and Deterministic Matrix Sketching”.
        In: SIAM Journalon Computing45.5 (Jan. 2016), pp. 1762-1792.
    """
    def __init__(self, matrix, network, max_rows=1000000, sparse = True):
        """ Initialize the matrix (not the SVD)

        Parameters
        ----------
        matrix : ndarray of shape (m_dim, n_dim)
            Initial input matrix

        network : bool - whether it's a network
            True - An update consists of a row update and a column update
            False - only update rows

        sparse : bool - whether it's a sparse matrix
            True - use our methods
            False - use the original methods(z-s, vecharynski, random)
        """
        
        self.data = matrix
        (self.m_dim, self.n_dim) = np.shape(self.data)

        self.network = network
        if network == True:
            assert(self.m_dim == self.n_dim
                   ), "Network must have square adjacency matrix."

        if max_rows is not None:
            self.max_rows = max_rows

        self.sparse = sparse

        self.SVDinitialized = False
        self.step_length = None
        self.method_dict = {'z-s': 1, 'vecharynski': 2, 'random' : 3}

        
    def TruncatedSVD(self, k_dim, init, method='z-s'):
        """ Initialize SVD
        Parameters
        ----------
        k_dim: Rank of truncated SVD to be calculated
        init: number of rows to perform the initial SVD decomposition
        method : string, default='z-s'
                 method for SVD update

        """
        
        self.SVDinitialized = True
        self.Uall = np.zeros((self.max_rows, k_dim), dtype=np.float64)
        self.mm = np.zeros((max(self.max_rows, 1000000),), dtype=np.int64)

        self.method = self.method_dict.get(method, 1)

        assert init <= self.m_dim, "init must be smaller than the matrix's size."
        self.init = init
        
        # Split initial SVD matrix and appended matrix
        if self.network == True:
            self.SVDmatrix = self.data[:init, :init]
            self.svd_mdim = init
            self.res_m_dim = self.m_dim - self.svd_mdim
            if init < self.m_dim:
                self.append_rows = self.data[init:, :].tocsr()
                self.append_cols = self.data[:, init:].tocsc()
            else:
                self.append_rows = None
                self.append_cols = None
        else:
            self.SVDmatrix = self.data[:init, :]
            self.svd_mdim = init
            self.res_m_dim = self.m_dim - self.svd_mdim
            if init < self.m_dim:
                self.append_matrix = self.data[init:, :]
            else:
                self.append_matrix = scipy.sparse.csr_matrix((0, self.n_dim))
        
        # Set desired rank of truncated SVD
        assert k_dim < min(self.m_dim, self.n_dim), "k must be smaller than or equal to min(m,n)."
        self.k_dim = k_dim

        # Calculate true truncated SVD of current matrix
        # Get initial truncated SVD
        U_true, sigma_true, VH_true = scipy.sparse.linalg.svds(self.SVDmatrix, self.k_dim)
        self.Uk = U_true[:, :self.k_dim]
        self.Uall[:self.Uk.shape[0]] = self.Uk
        self.cur_row = self.Uk.shape[0]
        self.sigmak = sigma_true[:self.k_dim]
        self.VHk = VH_true[: self.k_dim, :]
        self.Vk = self.VHk.T

        print(f"{'Initial Uk matrix of evolving matrix set to shape of ':<{msg_len}}{np.shape(self.Uk)}.")
        print(f"{'Initial sigmak array of evolving matrix set to shape of ':<{msg_len}}{np.shape(self.sigmak)}.")
        print(f"{'Initial VHk matrix of evolving matrix set to shape of ':<{msg_len}}{np.shape(self.VHk)}.")

        if self.sparse == True: # isvd
            self.Ku = np.eye(k_dim, dtype=np.float64)
            self.Kv = np.eye(k_dim, dtype=np.float64)
        else:
            self.Ku, self.Kv = None, None
        
        # Initialize submatrix to be appended at each update
        self.update_matrix = np.array([])

        # Initialize total runtime
        self.runtime = 0.0

        self.svd_time = 0

        # return
        return self.Uk, self.sigmak, self.VHk
 
    
    def SetStepLength(self, step_length : int):
        """ Set the step length of updates

        Parameters
        ----------
        step_length : int
            the step length of each update
        """

        assert(
            step_length > 0
        ), "Step length must be a positive integer."
        self.step_length = step_length
        print(f"New step length is: {self.step_length}")

    def SetAppendMatrix(self, append_matrix = None, A_csr = None, A_csc = None):
        """ Expand the original matrix

        Parameters
        ----------
       [Only for Network] A_csr: ndarray of shape(newl, n_dim + newl)
       [Only for Network] A_csc: ndarray of shape(m_dim + newl, newl)
       [Only for Non-network] new_matrix: ndarray of shape(newl, n_dim)
        
        """
        
        assert (
            self.SVDinitialized == True
        ), "SVD must be initialized before setting append matrix."

        if self.network == True:
            assert (
                A_csr != None and A_csc != None
            ), "Need rows(csr) and cols(csc) of the append matrix."
            
            assert(
                isinstance(A_csr, csr_matrix) and isinstance(A_csc, csc_matrix)
            ), "A_csr should be csr type and A_csc should be csc type."
            self._set_network_append_matrix(A_csr, A_csc)
        else:
            assert (
                append_matrix != None
            ), "Need append matrix of shape (num_rows_appended, n_dim)."
            self._set_append_matrix(append_matrix)

    def _set_append_matrix(self, append_matrix):
        """Add new part of the appended matrix 

        Parameters
        ----------
        append_matrix : ndarray of shape (s, n_dim)
            Matrix to be appended
        """

        # 1. Ensure that column dimensions are the same
        s_dim, n_dim = append_matrix.shape
        assert (
            n_dim == self.n_dim
        ), "Number of columns must be the same for initial matrix and matrix to be appended."
        
        # 2. Add the new section to data 
        new_data = scipy.sparse.vstack((self.data, append_matrix))
        self.data = new_data
        self.m_dim += s_dim

        # 3. Add the new section to append_matrix
        new_append_matrix = scipy.sparse.vstack((self.append_matrix, append_matrix))
        self.append_matrix = new_append_matrix.tocsr()
        self.res_m_dim += s_dim
        
        print(f"{'Add new part of the append matrix with shape ':<{msg_len}}{append_matrix.shape}.")

    def _set_network_append_matrix(self, A_csr, A_csc):
        """Add new part of the appended matrix 

        Parameters
        ----------
        A_csr : ndarray of shape (s, n_dim + s)
            Row matrix to be appended

        A_csc : ndarray of shape (m_dim + s, s)
            Row matrix to be appended
        """

        # 1. Ensure that column dimensions are the same
        s1_dim, n1_dim = A_csr.shape
        assert (
            n1_dim == self.n_dim + s1_dim
        ), "The shape must be the same for initial matrix and matrix to be appended."

        s2_dim, n2_dim = A_csc.shape
        assert (
            n2_dim == s1_dim and s2_dim == self.m_dim + s1_dim
        ), "The shape must be the same for initial matrix and matrix to be appended."

        # 2. Add the new section to data
        m1 =  A_csc[:self.m_dim, :]
        new_data1 = scipy.sparse.hstack((self.data, A_csc[:self.m_dim, :]))
        new_data2 = scipy.sparse.vstack((new_data1, A_csr))
        self.data = new_data2 
        
        # 3. Add the new section to append matrix
        # 3.1 append matrix is null
        if self.res_m_dim == 0:
            self.append_rows = A_csr
            self.append_cols = A_csc
            self.res_m_dim = s1_dim
        # 3.2 not null
        else:
            new_col_1 = scipy.sparse.hstack((self.append_cols, A_csc[:self.m_dim, :]))
            new_col_2 = scipy.sparse.vstack((new_col_1, A_csr[:, self.svd_mdim:])).tocsc()
            self.append_cols = new_col_2
            new_row_1 = scipy.sparse.vstack((self.append_rows, A_csr[:, :self.m_dim]))
            new_row_2 = scipy.sparse.hstack((new_row_1, A_csc[self.svd_mdim:, :])).tocsr()
            self.append_rows = new_row_2
            self.res_m_dim += s1_dim

        self.m_dim += s1_dim
        self.n_dim += s1_dim
        print(f"{'Add new part of the append matrix with number of nodes = ':<{msg_len}}{s1_dim}.")
        

    def Update(self, num_step=None, step_length=None, timer=False):
        """ Perform updates

        Parameters
        ----------
        num_step: int - number of updates performed
			If the maximum number of updatable steps is exceeded, it is automatically changed to the maximum value

        step_length: int
            can be ignored if already set

        timer: bool - whether to use a timer
        
        """

        assert (
            self.SVDinitialized == True
        ), "SVD must be initialized before performing updates."

        if step_length != None:
            assert(
                step_length > 0
            ), "Step length must be a positive integer."
            self.step_length = step_length
        
        else:
            assert (
                self.step_length != None
            ), "Must set step length before performing updates."
        
        if num_step != None:
            assert(
                num_step > 0
            ), "num_step must be a positive integer."
        
        max_step = math.ceil(self.res_m_dim / self.step_length)
        if num_step == None:
            num_step = max_step
        elif num_step > max_step:
            print(f"{'Exceeding Maximum Steps':<{msg_len}}.")
            num_step = max_step
        
        print(f"{'Start performing updates: num_step = ' + str(num_step) + ', step_length = ' + str(self.step_length):<{msg_len}}.")
        
        pbar = tqdm(range(num_step))
        for ii in pbar:
            
            if self.network == True:          
                self._evolve_network()
            
                self.update_matrix = self.E1
                self._update_svd()

                self.Uk, self.Vk = self.Vk, self.Uk
                if self.Ku is not None:
                    self.Ku, self.Kv = self.Kv, self.Ku

                self.update_matrix = self.E2
                self._update_svd()

                self.Uk, self.Vk = self.Vk, self.Uk
                if self.Ku is not None:
                    self.Ku, self.Kv = self.Kv, self.Ku
        
            else:
                self._evolve()
                self._update_svd()
            
    
    def _update_svd(self):
        if self.sparse == True:
            if self.method == 1:
                self._update_svd_isvd1()
            elif self.method == 2:
                self._update_svd_isvd2()
            else:
                self._update_svd_isvd3()
        else:
            if self.method == 1:
                self._update_svd_zhasimon()
            elif self.method == 2:
                self._update_vecharynski()
            else:
                self._update_random()
    
    
    def _evolve_network(self):
        """Evolve matrix by one update."""
        
        update_length = min(self.step_length, self.res_m_dim)
        self.res_m_dim -= update_length
        
        update_ptr = self.svd_mdim - self.init
        self.E1 = self.append_rows[
            update_ptr : update_ptr + update_length, : self.svd_mdim
        ]
        
        E2 = self.append_cols[
            : self.svd_mdim + update_length, update_ptr : update_ptr + update_length
        ]
        self.E2 = E2.transpose().tocsr()
        
        self.svd_mdim += update_length

    def _evolve(self):
        """Evolve matrix by one update."""
        
        update_length = min(self.step_length, self.res_m_dim)
        self.res_m_dim -= update_length

        update_ptr = self.svd_mdim - self.init
        self.update_matrix = self.append_matrix[
            update_ptr : update_ptr + update_length, :
        ]

        self.svd_mdim += update_length



    def _update_svd_isvd1(self):
        start = time.perf_counter()

        """ write ISVD code here """
        s = self.update_matrix.shape[0]
        k = self.Uk.shape[1]
        uid = np.unique(self.update_matrix.indices)
        B = np.zeros((s, len(uid)), dtype=np.float64)
        E = self.update_matrix
        
        for i in range(len(uid)):
            self.mm[ uid[i] ] = i
        cur = 0
        for i in range(s):
            for j in range( E.indptr[i+1] - E.indptr[i] ):
                B[i, self.mm[ E.indices[cur] ]] = E.data[cur]
                cur += 1
        B = B.T

        C = (self.Kv.T @ self.Vk[uid].T @ B)
        C0 = C.copy()

        R = np.zeros((s, s), dtype=np.float64)

        for i in range(s):
            tmp = np.dot(B[:, i], B[:, i]) - np.dot(C[:, i], C[:, i])
            alpha = 0
            if abs(tmp) > 1e-5:
                alpha = np.sqrt(tmp)
                B[:, i] /= alpha
                C[:, i] /= alpha
            R[i, i] = alpha

            for j in range(i+1, s):
                beta =  np.dot(B[:, i], B[:, j]) - np.dot(C[:, i], C[:, j])
                B[:, j] -= beta * B[:, i]
                C[:, j] -= beta * C[:, i]
                R[i, j] = beta

        time_1 = time.perf_counter()

        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, s), dtype=np.float64)), axis=1)
        Md = np.concatenate((C0.T, R.T), axis=1)
        M = np.concatenate((Mu, Md), axis=0)

        Fk, Tk, Gk = np.linalg.svd(M, full_matrices=False)
        Gk = Gk.T

        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            Gk = Gk[:, :k]
        
        time_2 = time.perf_counter()
        self.svd_time += time_2 - time_1

        self.Ku = self.Ku @ Fk[:k]
        self.Kv = self.Kv @ (Gk[:k] - C @ Gk[k:])



        time_3 = time.perf_counter()

        delta_Uk = Fk[k:] @ np.linalg.inv(self.Ku)
        self.Uk = np.append(self.Uk, delta_Uk, axis=0)
        
        self.sigmak = Tk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

        delta_Vk = B @ Gk[k:] @ np.linalg.inv(self.Kv)
        self.Vk[uid] += delta_Vk
        
        self.runtime += time.perf_counter() - start

    def _update_svd_isvd2(self):
        """Return truncated SVD of updated matrix using the ISVD method."""

        start = time.perf_counter()
        k = self.Uk.shape[1]
        E = self.update_matrix
        s = E.shape[0]
        l = min(10, s)
        uid = np.unique(self.update_matrix.indices)
        B = np.zeros((s, len(uid)), dtype=np.float64)
        for i in range(len(uid)):
            self.mm[ uid[i] ] = i
        cur = 0
        for i in range(s):
            for j in range( E.indptr[i+1] - E.indptr[i] ):
                B[i, self.mm[ E.indices[cur] ]] = E.data[cur]
                cur += 1
        B = B.T

        C = (self.Kv.T @ (self.Vk[uid].T) @ B)
 
        Bp = np.zeros((B.shape[0], l+1), dtype=np.float64)
        Cp = np.zeros((C.shape[0], l+1), dtype=np.float64)

        P = np.zeros((s, l+2), dtype=np.float64)
        P[:, 1] = np.random.randn(s)
        P[:, 1] = P[:, 1] / np.linalg.norm(P[:, 1])
        beta = np.zeros((l+1, ), dtype=np.float64)
        alpha = np.zeros((l+1, ), dtype=np.float64)

        for i in range(1, l+1):
            Bp[:, i] = B @ P[:, i] - beta[i-1] * Bp[:, i-1]
            Cp[:, i] = C @ P[:, i] - beta[i-1] * Cp[:, i-1]
            tmp = np.dot(Bp[:, i], Bp[:, i]) - np.dot(Cp[:, i], Cp[:, i])
            if abs(tmp) < 1e-9:
                alpha[i] = 0
            else:
                alpha[i] = np.sqrt( tmp )
                Bp[:, i] /= alpha[i]
                Cp[:, i] /= alpha[i]

           
            P[:, i+1] = B.T @ Bp[:, i] - C.T @ Cp[:, i] - alpha[i] * P[:, i]
            for j in range(1, i+1):
                P[:, i+1] -= np.dot(P[:, i+1], P[:, j]) * P[:, j]
            beta[i] = np.linalg.norm(P[:, i+1])
            if abs(beta[i]) < 1e-9:
                l = i
                break
            P[:, i+1] /= beta[i]
        
        L = np.zeros((l, l+1), dtype=np.float64)
        for i in range(l):
            L[i, i] = alpha[i]
            L[i, i+1] = beta[i]
        
        Bp = Bp[:, 1:]
        Cp = Cp[:, 1:]
        P = P[:, 1:]

        Bp = Bp[:, :l]
        Cp = Cp[:, :l]
        P = P[:, :l+1]

        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, l), dtype=np.float64)), axis=1)
        Md = np.concatenate((C.T, P @ L.T), axis=1)
        M = np.concatenate((Mu, Md), axis=0)

        # Calculate SVD of M
        time_1 = time.perf_counter()
        Fk, Tk, GHk = np.linalg.svd(M, full_matrices=False)
        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            GHk = GHk[:k]
        Gk = GHk.T
        time_2 = time.perf_counter()
        self.svd_time += time_2 - time_1

        # Calculate updated values for Uk, Sk, Vk`
        
        self.Ku = self.Ku @ Fk[:k]
        self.Kv = self.Kv @ (Gk[:k] - Cp @ Gk[k:])

        delta_Uk = Fk[k:] @ np.linalg.inv(self.Ku)
        self.Uk = np.append(self.Uk, delta_Uk, axis=0)
        
        self.sigmak = Tk

        delta_Vk = Bp @ Gk[k:] @ np.linalg.inv(self.Kv)
        self.Vk[uid] += delta_Vk

        self.runtime += time.perf_counter() - start
        return self.Uk, self.sigmak, self.Vk

    def _update_svd_isvd3(self):
        """Return truncated SVD of updated matrix using the random method."""
        start = time.perf_counter()
        E = self.update_matrix

        s = E.shape[0]
        k = self.Uk.shape[1]
        l = min(10, s)
        if l == 0:
            l = 1
        num_iter = 3

        uid = np.unique(self.update_matrix.indices)
        B = np.zeros((s, len(uid)), dtype=np.float64)
        for i in range(len(uid)):
            self.mm[ uid[i] ] = i
        cur = 0
        for i in range(s):
            for j in range( E.indptr[i+1] - E.indptr[i] ):
                B[i, self.mm[ E.indices[cur] ]] = E.data[cur]
                cur += 1
        B = B.T
        C = (self.Kv.T @ (self.Vk[uid].T) @ B)


        Q = np.zeros((s, l), dtype=np.float64)
        for i in range(l):
            Q[:, i] = np.random.randn(s)
            Q[:, i] = Q[:, i] / np.linalg.norm(Q[:, i])

        for _ in range(num_iter):
            Q, R = np.linalg.qr(Q)
            BP, CP = B @ Q, C @ Q

            R = np.zeros((l, l), dtype=np.float64)
            for i in range(l):
                for j in range(i):
                    beta = np.dot(BP[:, i], BP[:, j]) - np.dot(CP[:, i], CP[:, j])
                    R[j, i] = beta
                    BP[:, i] -= beta * BP[:, j]
                    CP[:, i] -= beta * CP[:, j]
                tmp = np.dot(BP[:, i], BP[:, i]) - np.dot(CP[:, i], CP[:, i])
                if abs(tmp) < 1e-9:
                    R[i, i] = 0
                    continue
                alpha = np.sqrt( tmp )
                R[i, i] = alpha
                BP[:, i] /= alpha
                CP[:, i] /= alpha

            # P, R = np.linalg.qr(P)
            if _ != num_iter-1:
                Q = B.T @ BP - C.T @ CP
        


        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, l), dtype=np.float64)), axis=1)
        Md = np.concatenate((C.T, P), axis=1)

        M = np.concatenate((Mu, Md), axis=0)
        # Calculate SVD of M


        time_1 = time.perf_counter()
        
        Fk, Tk, GHk = np.linalg.svd(M, full_matrices=False)

        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            GHk = GHk[:k]
        Gk = GHk.T


        time_2 = time.perf_counter()
        self.svd_time += time_2 - time_1
        # Calculate updated values for Uk, Sk, Vk


        self.Ku = self.Ku @ Fk[:k]
        self.Kv = self.Kv @ (Gk[:k] - CP @ Gk[k:])

        delta_Uk = Fk[k:] @ np.linalg.inv(self.Ku)
        self.Uk = np.append(self.Uk, delta_Uk, axis=0)
        
        self.sigmak = Tk

        delta_Vk = BP @ Gk[k:] @ np.linalg.inv(self.Kv)
        self.Vk[uid] += delta_Vk

        self.runtime += time.perf_counter() - start
        return self.Uk, self.sigmak, self.Vk



    def _update_svd_zhasimon(self):
        """Return truncated SVD of updated matrix using the Zha-Simon projection method."""
        
        '''=====Step 1====='''
        start_time_step_1 = time.perf_counter()
        E = self.update_matrix
        V = self.Vk

        s = E.shape[0]
        k = self.Uk.shape[1]

        Q, R = np.linalg.qr(E.T - V @ (V.T @ E.T))
        Z = scipy.linalg.block_diag(self.Uk, np.eye(s))
        W = np.concatenate((V, Q), axis=1)
        self.runtime_step1 += time.perf_counter() - start_time_step_1


        '''=====Step 2====='''
        start_time_step_2 = time.perf_counter()
        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, s), dtype=np.float64)), axis=1)
        Md = np.concatenate((E@V, R.T), axis=1)
        M = np.concatenate((Mu, Md), axis=0)
        # print(M)

        # Calculate SVD of M
        # Fk, Tk, GHk = scipy.sparse.linalg.svds(M, k)
        Fk, Tk, GHk = np.linalg.svd(M, full_matrices=False)
        # print(len(Tk))

        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            GHk = GHk[:k]
        self.runtime_step2 += time.perf_counter() - start_time_step_2

        '''=====Step 3====='''
        start_time_step_3 = time.perf_counter()
        # Calculate updated values for Uk, Sk, Vk
        self.sigmak = Tk
        self.Uk = Z @ Fk
        self.Vk = W @ (GHk.T)
        self.runtime_step3 += time.perf_counter() - start_time_step_3


    def _update_vecharynski(self):
        """Return truncated SVD of updated matrix using the Zha-Simon projection method."""

        '''=====Step 1====='''
        start_time_step_1 = time.perf_counter()
        E = self.update_matrix
        V = self.Vk
        s = E.shape[0]
        k = self.Uk.shape[1]
        n = V.shape[0]
        l = min(10, s)

        Q = np.zeros((n, l+1), dtype=np.float64)
        # X = E.T - V @ ((V.T) @ (E.T))

        P = np.zeros((s, l+2), dtype=np.float64)
        P[:, 1] = np.random.randn(s)
        P[:, 1] = P[:, 1] / np.linalg.norm(P[:, 1])
        beta = np.zeros((l+1, ), dtype=np.float64)
        alpha = np.zeros((l+1, ), dtype=np.float64)
        for i in range(1, l+1):
            time_1 = time.perf_counter()
            # Q[:, i] = X @ P[:, i] - beta[i-1] * Q[:, i-1]
            Q[:, i] = E.T @ P[:, i] - V @ ((V.T @ E.T) @ P[:, i]) - beta[i-1] * Q[:, i-1]
            self.runtime_tmp1 += time.perf_counter() - time_1

            alpha[i] = np.linalg.norm(Q[:, i])
            if alpha[i] == 0:
                Q[:, i] = 0
            else:
                Q[:, i] /= alpha[i]
            
            time_2 = time.perf_counter()
            # P[:, i+1] = X.T @ Q[:, i] - alpha[i] * P[:, i]
            P[:, i+1] = E @ Q[:, i] - E @ (V @ (V.T @ Q[:, i])) - alpha[i] * P[:, i]
            self.runtime_tmp2 += time.perf_counter() - time_2
            for j in range(1, i+1):
                P[:, i+1] -= np.dot(P[:, i+1], P[:, j]) * P[:, j]
            
            beta[i] = np.linalg.norm(P[:, i+1])
            if beta[i] == 0:
                P[:, i+1] = 0
                continue
            P[:, i+1] /= beta[i]

        B = np.zeros((l, l+1), dtype=np.float64)
        for i in range(l):
            B[i, i] = alpha[i]
            B[i, i+1] = beta[i]
        
        P = P[:, 1:]
        Q = Q[:, 1:]

        Z = scipy.linalg.block_diag(self.Uk, np.eye(s))
        W = np.concatenate((self.Vk, Q), axis=-1)
        self.runtime_step1 += time.perf_counter() - start_time_step_1

        '''=====Step 2====='''
        start_time_step_2 = time.perf_counter()
        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, l), dtype=np.float64)), axis=1)
        Md = np.concatenate((E@V, P @ B.T), axis=1)
        M = np.concatenate((Mu, Md), axis=0)

        # Calculate SVD of M
        Fk, Tk, GHk = np.linalg.svd(M, full_matrices=False)
        
        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            GHk = GHk[:k]
        self.runtime_step2 += time.perf_counter() - start_time_step_2

        '''=====Step 3====='''
        start_time_step_3 = time.perf_counter()
        # Calculate updated values for Uk, Sk, Vk
        self.Uk = Z @ Fk
        self.sigmak = Tk
        self.Vk = (W @ (GHk.T))  
        self.runtime_step3 += time.perf_counter() - start_time_step_3      


    def _update_random(self):
        """Return truncated SVD of updated matrix using the random method."""

        '''=====Step 1====='''
        start_time_step_1 = time.perf_counter()
        E = self.update_matrix
        V = self.Vk

        s = E.shape[0]
        k = self.Uk.shape[1]
        l = min(10, s)
        num_iter = 3
        # X = E.T - V @ ((V.T) @ (E.T))

        Q = np.zeros((s, l), dtype=np.float64)
        for i in range(l):
            Q[:, i] = np.random.randn(s)
            Q[:, i] = Q[:, i] / np.linalg.norm(Q[:, i])

        for i in range(num_iter):
            Q, R = np.linalg.qr(Q)
            # P = X @ Q
            P = E.T @ Q - V @ (((V.T) @ (E.T)) @ Q)
            P, R = np.linalg.qr(P)
            if i != num_iter-1:
                # Q = X.T @ P
                Q = E @ P - E @ (V @ (V.T @ P))

        Z = scipy.linalg.block_diag(self.Uk, np.eye(s))
        W = np.concatenate((self.Vk, P), axis=-1)
        self.runtime_step1 += time.perf_counter() - start_time_step_1
        
        '''=====Step 2====='''
        start_time_step_2 = time.perf_counter()
        Mu = np.concatenate((np.diag(self.sigmak), np.zeros((k, l), dtype=np.float64)), axis=1)
        Md = np.concatenate((E@V, Q), axis=1)
        M = np.concatenate((Mu, Md), axis=0)
        # Calculate SVD of M
        Fk, Tk, GHk = np.linalg.svd(M, full_matrices=False)
        
        # Truncate if necessary
        if k < len(Tk):
            Fk = Fk[:, :k]
            Tk = Tk[:k]
            GHk = GHk[:k]
        self.runtime_step2 += time.perf_counter() - start_time_step_2

        '''=====Step 3====='''
        start_time_step_3 = time.perf_counter()
        # Calculate updated values for Uk, Sk, Vk
        self.Uk = Z @ Fk
        self.sigmak = Tk
        self.Vk = (W @ (GHk.T))
        self.runtime_step3 += time.perf_counter() - start_time_step_3     