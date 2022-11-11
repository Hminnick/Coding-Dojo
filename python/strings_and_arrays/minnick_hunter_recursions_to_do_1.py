def rSigma(num):
    if num > 0:
        return num + rSigma(num-1);
    return 0

def rFact(num):
    if num > 1:
        return num * rFact(num-1);
    return 1