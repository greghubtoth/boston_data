from numpy import poly1d, mean, std

# I have the format y = p(x) for a general polynomial
# that estimates the curve of the distribution
# for the housing price.

# I got NOX, RM, CRIM, LSTAT and PTRATIO that I will average over
# to produce an outcome

def lstat_approx(x):
    p = poly1d([-1.71414154e-02,  8.75430224e-01, -1.42796917e+01,  9.19755840e+01]) # see documentation on procurement
    y = p(x)

    return y

def nox_approx(x):
    p = poly1d([-425.3024246 ,  378.13603059,  -50.64560988])
    y = p(x)
    return y

def crim_approx(x):
    p = poly1d([ 8.88633374e-03, -9.33071702e-01,  2.84849955e+01])
    y = 1.65*p(x)
    return y

def rm_approx(x):
    p = poly1d([ 17.37065737, -87.35220131])
    y = p(x)
    return y

def ptratio_approx(x):
    p = poly1d([  0.26609764, -11.97890043, 153.01549492])
    y = p(x)
    return y


def wing_it(a,b,c,d,e):
    prices = [a, b, c, d, e]
    ave_prices = mean(prices)

    uncertainty = std(prices)

    return ave_prices, uncertainty