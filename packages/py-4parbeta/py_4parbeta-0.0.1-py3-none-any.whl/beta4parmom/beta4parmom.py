import statistics
import math
from scipy.optimize import minimize
import pandas as pd

def inieq(par, dat):
    th1, th2 = par
    datpd = pd.DataFrame(dat)
    if (datpd.isnull().any().any()):
        print("The data contains NANs")
    else:
        Xbar = statistics.mean(dat)
        S2 = statistics.variance(dat)
        m3 = statistics.mean((dat - Xbar) ** 3)
        m4 = statistics.mean((dat - Xbar) ** 4)
        term11 = (th1*th2)/S2
        term12 = (2*S2*(th2-th1)/m3) - 1
        term1 = term11-term12
        comt = 2*S2*(th2-th1)
        deno = comt * (comt + m3)
        nu1 = 3 * (S2 ** 2) * ((comt - m3) * (comt - (8*m3)))
        nu2 = 6 * S2 * (m3 ** 2) * ((th2 + th1) ** 2)
        term2 = m4 - ((nu1 + nu2)/deno)
        ret = (term1 ** 2) + (term2 ** 2)
        return ret


def r4parbeta_mom(dat):
    datpd = pd.DataFrame(dat)
    if(datpd.isnull().any().any()):
        print("The data contains NANs")
    else:
        Xbar = statistics.mean(dat)
        S2 = statistics.variance(dat)
        X1 = min(dat)
        Xn = max(dat)
        U1 = Xbar - X1
        U2 = Xn - Xbar
        mom = [0] * 4
        bnds = ((0, None), (0, None))
        est = minimize(fun=inieq, x0=np.array([U1, U2]).flatten(), args=dat, method='L-BFGS-B', bounds=bnds).x
        mom[0] = Xbar - est[0]
        mom[1] = Xbar + est[1]
        mom[2] = ((est[0])/(est[0]+est[1])) * (((est[0]*est[1])/S2)-1)
        mom[3] = mom[2] * ((est[0])/(est[1]))
    return mom
