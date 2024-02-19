import numpy as np
import pandas as pd
from scipy.stats import beta
from scipy.optimize import minimize
import math
import statistics

def loggam(a):
    if(a > 0):
        if(type(a) == type(3.5)):
            gif = int(math.floor(a))
            fra = a - gif
            logt = math.log(math.gamma(fra)) + math.log(fra)
            sum = 0
            for i in range(int(gif - 1)):
                sum = sum + math.log(i + 1 + fra)
                ret = sum + logt
        else:
            ret = 0
            for i in range(int(a - 1)):
                ret = ret + math.log(i + 1)
    else:
        ret = math.nan
    return ret


def betaloglik(par, dt):
    al1, al2 = par
    th1mle = min(dt)
    dt1new = np.delete(dt, np.where(dt == th1mle))
    th2mle = max(dt1new)
    dtnew = np.delete(dt1new, np.where(dt1new == th2mle))
    dat = [0] * len(dtnew)
    sum1 = sum2 = 0
    for i in range(int(len(dtnew))):
        dat[i] = (dtnew[i] - th1mle) / (th2mle - th1mle)
        sum1 = sum1 + math.log(dat[i])
        sum2 = sum2 + math.log(1 - dat[i])
    ret = -((len(dtnew) - 1) * (loggam(al1 + al2) - loggam(al1) - loggam(al2))) - ((al1-1) * sum1) - ((al2-1) * sum2) - beta.logsf(max(dat), al1, al2) - beta.logcdf(min(dat), al1, al2)
    return ret

def momsta(dt):
    th1mle = min(dt)
    dt1new = np.delete(dt, np.where(dt == th1mle))
    th2mle = max(dt1new)
    dtnew = np.delete(dt1new, np.where(dt1new == th2mle))
    newdat = [0] * len(dtnew)
    for i in range(int(len(dtnew))):
        newdat[i] = (dtnew[i] - th1mle) / (th2mle - th1mle)
    mu = statistics.mean(newdat)
    var = statistics.variance(newdat)
    al1est = mu * ((mu*(1-mu)/var) - 1)
    al2est = (1-mu) * ((mu*(1-mu)/var) - 1)
    if al1est < 0 or al2est < 0:
        alpha1mom = math.nan
        alpha2mom = math.nan
    else:
         alpha1mom = al1est
         alpha2mom = al2est
    momest = [alpha1mom, alpha2mom]
    return momest


def r4parbeta_mle(dat):
    datpd = pd.DataFrame(dat)
    if (datpd.isnull().any().any()):
        print("The data contains NANs")
    else:
        momest = momsta(dat)
        pytmom = beta.fit(dat, method="MM")
        bnds = ((0, None), (0, None))
        if(momest[1] > 0):
            est = minimize(fun=betaloglik, x0=np.array([momest[0], momest[1]]).flatten(), args=dat, method='L-BFGS-B', bounds=bnds).x
            theta1mle = min(dat)
            theta2mle = max(dat)
            alpha1mle = est[0]
            alpha2mle = est[1]
            mle = [theta1mle, theta2mle, alpha1mle, alpha2mle]
        else:
            est1 = minimize(fun=betaloglik, x0=np.array([pytmom[0], pytmom[1]]).flatten(), args=dat, method='L-BFGS-B', bounds=bnds).x
            theta1mle = min(dat)
            theta2mle = max(dat)
            alpha1mle = est1[0]
            alpha2mle = est1[1]
            mle = [theta1mle, theta2mle, alpha1mle, alpha2mle]
    return mle
