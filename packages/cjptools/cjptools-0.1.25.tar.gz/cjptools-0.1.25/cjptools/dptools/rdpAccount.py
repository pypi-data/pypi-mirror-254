
from opacus.accountants.analysis import rdp as privacy_analysis
import json
import math
import numpy as np
import os
DEFAULT_ALPHAS = [1 + x / 10.0 for x in range(1, 201)] + list(range(22, 500))
dataPath=os.path.abspath(os.path.dirname(__file__))
callBak={};
backupFiles=['getMinSigma4nonUniPrivacy_callBak.npy']
for backupFile in backupFiles:
    dt = np.load(dataPath+os.sep+backupFile, allow_pickle=True).item()
    callBak=dict(callBak, **dt)
    # print(callBak)

def loadBakedObj(key):
    str=json.dumps(key);
    if str in callBak:
        return callBak[str]
    return None

def bakObj(key,val):
    str=json.dumps(key);
    if str not in callBak:
        callBak[str]=val;

def getPrivacySpentWithFixedNoise(
        sample_rate, num_steps, delta: float,sigma=1.0, alphas = None
):
    if alphas is None:
        alphas = DEFAULT_ALPHAS
    noise_multiplier=sigma;
    rdp = privacy_analysis.compute_rdp(
                q=sample_rate,
                noise_multiplier=noise_multiplier,
                steps=num_steps,
                orders=alphas,
            )
    eps, best_alpha = privacy_analysis.get_privacy_spent(
        orders=alphas, rdp=rdp, delta=delta
    )
    return float(eps), float(best_alpha)

def epochAllowed(sample_rate, stepsHasRunned,requiredSteps, maxEps, delta: float,sigma=1.0, alphas = None):
    epsUsed, best_alpha = getPrivacySpentWithFixedNoise(sample_rate, stepsHasRunned+requiredSteps, delta, sigma=sigma, alphas = alphas);
    if maxEps<epsUsed:
        minStep=0
        maxStep=requiredSteps-1;
        while minStep<maxStep:
            midStep=(minStep+maxStep+1)//2
            epsUsed, best_alpha = getPrivacySpentWithFixedNoise(sample_rate, stepsHasRunned+midStep, delta, sigma=sigma, alphas = alphas);
            if maxEps<epsUsed:
                maxStep=midStep-1;
            else:
                minStep=midStep;
        return minStep
    else:
        return requiredSteps;
    # while requiredSteps>0 and maxEps<epsUsed:
    #     requiredSteps-=1;
    #     epsUsed, best_alpha = getPrivacySpentWithFixedNoise(sample_rate, stepsHasRunned+requiredSteps, delta, sigma=sigma, alphas = alphas);

def getClientT(sample_rate, maxEps, delta: float,sigma=1.0, alphas = None):
    keyArr=['getMinSigma',sample_rate, maxEps, delta, sigma, alphas];
    obj=loadBakedObj(keyArr);
    if obj is not None:
        return obj
    minStep=0;
    maxStep=1;
    while getPrivacySpentWithFixedNoise(sample_rate, maxStep, delta, sigma=sigma, alphas = alphas)[0]<=maxEps:
        minStep=maxStep;
        maxStep*=2;
    maxStep = maxStep - 1;
    while minStep<maxStep:
        midStep=(minStep+maxStep+1)//2
        epsUsed, best_alpha = getPrivacySpentWithFixedNoise(sample_rate, midStep, delta, sigma=sigma, alphas = alphas);
        if maxEps<epsUsed:
            maxStep=midStep-1;
        else:
            minStep=midStep;
    bakObj(keyArr,minStep)
    return minStep

def getMinSigma(sample_rate, num_steps, delta: float,requireEps, alphas = None):
    # if requireEps==1.0 and sample_rate==0.01 and num_steps==4096:
    #     return 2.1870198771357536
    keyArr=['getMinSigma',sample_rate, num_steps, delta,requireEps, alphas];
    obj=loadBakedObj(keyArr);
    if obj is not None:
        return obj
    minSigma=0;
    maxSigma = 1;
    while getPrivacySpentWithFixedNoise(sample_rate, num_steps, delta, sigma=maxSigma, alphas = alphas)[0]>requireEps:
        minSigma=maxSigma;
        maxSigma*=2;
    while maxSigma-minSigma>1e-8:
        midSigma=(maxSigma+minSigma)/2;
        eps, best_alpha = getPrivacySpentWithFixedNoise(sample_rate, num_steps, delta, sigma=midSigma, alphas = alphas)
        if eps<=requireEps:
            maxSigma=midSigma;
        else:
            minSigma=midSigma;
    bakObj(keyArr,maxSigma)
    return maxSigma;

from cjptools import tic,toc
# 迭代过程噪声呈现指数分布的情况
def get_nonUni_privacy_spent(
        sample_rate, num_steps, delta: float,sigmaIni=1.0, gamma=0, num_steps_per_group=1,alphas = None
):
    '''
    第t(t从0开始)次迭代的sigma值为sigmaIni*exp(gamma*t/(num_steps-1))
    '''
    if alphas is None:
        alphas = DEFAULT_ALPHAS
    if gamma==0:
        noise_multiplier = sigmaIni;
        rdpAll = privacy_analysis.compute_rdp(
            q=sample_rate,
            noise_multiplier=noise_multiplier,
            steps=num_steps,
            orders=alphas,
        )
    else:
        t=0;
        while t<num_steps:
            # tic()
            if t==0:
                noise_multiplier = sigmaIni;
            else:
                noise_multiplier=sigmaIni*math.exp(gamma*t/(num_steps-1));

            rdp = privacy_analysis.compute_rdp(
                        q=sample_rate,
                        noise_multiplier=noise_multiplier,
                        steps=min(num_steps_per_group,num_steps-t),
                        orders=alphas,
                    )
            if t==0:
                rdpAll=rdp;
            else:
                rdpAll+=rdp
            # print(toc(),t,noise_multiplier)
            t+=num_steps_per_group
    eps, best_alpha = privacy_analysis.get_privacy_spent(
        orders=alphas, rdp=rdpAll, delta=delta
    )
    return float(eps), float(best_alpha)


def getMinSigma4nonUniPrivacy(sample_rate, num_steps, delta: float,requireEps: float, gamma=0, num_steps_per_group=1, alphas = None):
    sample_rate=float(sample_rate)
    num_steps = int(num_steps)
    delta = float(delta)
    requireEps = float(requireEps)
    gamma = float(gamma)
    num_steps_per_group = int(num_steps_per_group)

    keyArr=['getMinSigma4nonUniPrivacy',sample_rate, num_steps, delta,requireEps, gamma, alphas];
    obj=loadBakedObj(keyArr);
    if obj is not None:
        return obj
    minSigma=0;
    maxSigma = 1;
    while get_nonUni_privacy_spent(sample_rate, num_steps, delta, sigmaIni=maxSigma,gamma=gamma,num_steps_per_group=num_steps_per_group, alphas=alphas)[0]>requireEps:
        minSigma=maxSigma;
        maxSigma*=2;
    while maxSigma-minSigma>1e-6:
        midSigma=(maxSigma+minSigma)/2;
        eps, best_alpha = get_nonUni_privacy_spent(sample_rate, num_steps, delta, sigmaIni=midSigma, gamma=gamma,num_steps_per_group=num_steps_per_group, alphas = alphas)
        if eps<=requireEps:
            maxSigma=midSigma;
        else:
            minSigma=midSigma;
    bakObj(keyArr,maxSigma)
    return maxSigma;

