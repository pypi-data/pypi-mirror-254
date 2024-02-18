#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:47:48 2023

@author: samgale
"""

import glob
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
from DynamicRoutingAnalysisUtils import getSessionData
from RLmodelHPC import calcLogisticProb, runModel


# plot relationship bewtween tau and q values
q = np.arange(0,1.01,0.01)
beta = np.arange(51)
bias = (0,0.25)
xticks = np.arange(0,q.size+1,int(q.size/4))
yticks = np.arange(0,50,10)
for bi in bias:
    p = np.zeros((beta.size,q.size))
    for i,bt in enumerate(beta):
        p[i] = calcLogisticProb(q,bt,bi)
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    im = ax.imshow(p,clim=(0,1),cmap='magma',origin='lower',aspect='auto')
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.round(q[xticks],1))
    ax.set_yticks(yticks)
    ax.set_yticklabels(beta[yticks])
    ax.set_xlabel('Q')
    ax.set_ylabel(r'$\beta$')
    ax.set_title('lick probability, bias='+str(bi))
    plt.colorbar(im)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for bt,clr in zip((5,10,20),'rgb'):
    for bi,ls in zip(bias,('-','--')):
        ax.plot(q,calcLogisticProb(q,bt,bi),color=clr,ls=ls,label=r'$\beta$='+str(bt)+', bias='+str(bi))
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
ax.set_xticks(np.arange(-1,1.1,0.5))
ax.set_yticks(np.arange(0,1.1,0.5))
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_xlabel('Q',fontsize=14)
ax.set_ylabel('lick probability',fontsize=14)
ax.legend()
plt.tight_layout()


# get fit params from HPC output
trainingPhaseNames = ('initial training','after learning')#,'nogo','noAR','rewardOnly','no reward')
trainingPhases = []
trainingPhaseColors = 'mgrbck'
modelTypeNames = ('contextQ',)#'weightContext','weightAction','attendReward')
modelTypes = []
modelTypeParams = {}
paramNames = ('betaAction','biasAction','biasAttention','visConf','audConf','alphaContext','alphaAction','decayContext','alphaHabit')
paramBounds = ([0,40],[-1,1],[-1,1],[0.5,1],[0.5,1],[0,1],[0,1],[1,600],[0,1])
fixedParamNames = ('Full model','biasAction','biasAttention','visConf','audConf','alphaContext','alphaAction','alphaContext,\nalphaAction','alphaContext,\nalphaHabit','decayContext','alphaHabit','decayContext,\nalphaHabit')
fixedParamValues = (None,0,0,1,1,0,0,0,0,0,0,0)
nModelParams = (9,8,8,8,8,7,8,6,6,8,8,7)
modelData = {}
filePaths = glob.glob(os.path.join(r"\\allen\programs\mindscope\workgroups\dynamicrouting\Sam\RLmodel",'*.npz'))
for f in filePaths:
    mouseId,sessionDate,sessionTime,trainingPhase,modelType = os.path.splitext(os.path.basename(f))[0].split('_')
    session = sessionDate+'_'+sessionTime
    if trainingPhase not in trainingPhases:
        trainingPhases.append(trainingPhase)
        modelData[trainingPhase] = {}
    if modelType not in modelTypes:
        modelTypes.append(modelType)
    with np.load(f) as data:
        params = data['params']
        logLoss = data['logLoss']
        termMessage = data['terminationMessage']
        if modelType not in modelTypeParams:
            modelTypeParams[modelType] = {key: bool(val) for key,val in data.items() if key not in ('params','logLoss','terminationMessage')}
    d = modelData[trainingPhase]
    p = {'params': params, 'logLoss': logLoss, 'terminationMessage': termMessage}
    if mouseId not in d:
        d[mouseId] = {session: {modelType: p}}
    elif session not in d[mouseId]:
        d[mouseId][session] = {modelType: p}
    elif modelType not in d[mouseId][session]:
        d[mouseId][session][modelType] = p
trainingPhases = [name for name in trainingPhaseNames if name in trainingPhases]
modelTypes = [name for name in modelTypeNames if name in modelTypes]


# print fit termination message
for trainingPhase in trainingPhases:
    for mouse in modelData[trainingPhase]:
        for session in modelData[trainingPhase][mouse]:
            for modelType in modelTypes:
                print(modelData[trainingPhase][mouse][session][modelType]['terminationMessage'])


# get experiment data and model variables
sessionData = {phase: {} for phase in trainingPhases}
useHistory = True
nReps = 1      
for trainingPhase in trainingPhases:
    print(trainingPhase)
    d = modelData[trainingPhase]
    if len(d) > 0:
        for mouse in d:
            for session in d[mouse]:
                obj = getSessionData(mouse,session)
                if mouse not in sessionData[trainingPhase]:
                    sessionData[trainingPhase][mouse] = {session: obj}
                elif session not in sessionData[trainingPhase][mouse]:
                    sessionData[trainingPhase][mouse][session] = obj
                for modelType in modelTypes:
                    s = d[mouse][session][modelType]
                    s['pContext'] = []
                    s['qContext'] = []
                    s['qStim'] = []
                    s['wHabit'] = []
                    s['expectedValue'] = []
                    s['qTotal'] = []
                    s['prediction'] = []
                    for params in s['params']:
                        pContext,qContext,qStim,wHabit,expectedValue,qTotal,pAction,action = [val.mean(axis=0) for val in runModel(obj,*params,useHistory=useHistory,nReps=nReps,**modelTypeParams[modelType])]
                        s['pContext'].append(pContext)
                        s['qContext'].append(qContext)
                        s['qStim'].append(qStim)
                        s['wHabit'].append(wHabit)
                        s['expectedValue'].append(expectedValue)
                        s['qTotal'].append(qTotal)
                        s['prediction'].append(pAction)
                        

# plot logloss
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
xticks = np.arange(len(modelTypes)+1)
xticklabels = ['standardQ']+modelTypes
for trainingPhase,clr in zip(trainingPhases,trainingPhaseColors):
    d = modelData[trainingPhase]
    if len(d) > 0:
        for x,modelType in zip(xticks,xticklabels):
            if modelType=='standardQ':
                val = np.array([np.mean([session['contextQ']['logLoss'][fixedParamNames.index('alphaContext')] for session in mouse.values()],axis=0) for mouse in d.values()])
            else:
                val = np.array([np.mean([session[modelType]['logLoss'][fixedParamNames.index('Full model')] for session in mouse.values()],axis=0) for mouse in d.values()])
            m = val.mean()
            s = val.std()/(len(val)**0.5)
            ax.plot(x,m,'o',mec=clr,mfc='none',ms=10,mew=2,label=trainingPhase)
            ax.plot([x,x],[m-s,m+s],color=clr,lw=2)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlim([-0.25,xticks[-1]+0.25])
ax.set_ylabel('NLL')
plt.tight_layout()

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
xticks = np.arange(len(modelTypes))
xticklabels = modelTypes
for trainingPhase,clr in zip(trainingPhases,trainingPhaseColors):
    if clr not in 'gm':
        continue
    d = modelData[trainingPhase]
    standardQ = np.array([np.mean([session['contextQ']['logLoss'][fixedParamNames.index('alphaContext')] for session in mouse.values()],axis=0) for mouse in d.values()])
    if len(d) > 0:
        for x,modelType in zip(xticks,xticklabels):
            val = np.array([np.mean([session[modelType]['logLoss'][fixedParamNames.index('Full model')] for session in mouse.values()],axis=0) for mouse in d.values()])
            val -= standardQ
            m = val.mean()
            s = val.std()/(len(val)**0.5)
            lbl = trainingPhase if x==0 else None
            ax.plot(x,m,'o',mec=clr,mfc='none',ms=10,mew=2,label=lbl)
            ax.plot([x,x],[m-s,m+s],color=clr,lw=2)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlim([-0.25,xticks[-1]+0.25])
ax.set_ylabel('NLL relative to Q learning')
ax.legend()
plt.tight_layout()

for modelType in modelTypes:
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    xticks = np.arange(len(fixedParamNames))
    xlim = [-0.25,xticks[-1]+0.25]
    ax.plot(xlim,[0,0],'--',color='0.5')
    for trainingPhase,clr in zip(trainingPhases,trainingPhaseColors):
        d = modelData[trainingPhase]
        if len(d) > 0:
            val = np.array([np.mean([session[modelType]['logLoss'] for session in mouse.values()],axis=0) for mouse in d.values()])
            val -= val[:,fixedParamNames.index('Full model')][:,None]
            mean = val.mean(axis=0)
            sem = val.std(axis=0)/(len(val)**0.5)
            ax.plot(xticks,mean,'o',mec=clr,mfc='none',ms=10,mew=2,label=trainingPhase)
            for x,m,s in zip(xticks,mean,sem):
                ax.plot([x,x],[m-s,m+s],color=clr,lw=2)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    ax.set_xticks(xticks)
    ax.set_xticklabels([fixedParamNames[0]]+[name+'='+str(val) for name,val in zip(fixedParamNames[1:],fixedParamValues[1:])])
    ax.set_xlim(xlim)
    ax.set_ylabel(r'$\Delta$ NLL')
    ax.legend(loc='upper left')
    plt.tight_layout()

for modelType in modelTypes:
    fig = plt.figure(figsize=(5,10))
    for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
        ax = fig.add_subplot(len(fixedParamNames),1,i+1)
        ax.plot([0,0],[0,1],'--',color='0.5')
        for trainingPhase,clr in zip(trainingPhases,trainingPhaseColors):
            d = modelData[trainingPhase]
            if len(d) > 0:
                logLoss = np.array([np.mean([session[modelType]['logLoss'] for session in mouse.values()],axis=0) for mouse in d.values()])          
                logLoss = logLoss[:,i] - logLoss[:,fixedParamNames.index('Full model')] if fixedParam != 'Full model' else logLoss[:,i]
                dsort = np.sort(logLoss)
                cumProb = np.array([np.sum(dsort<=i)/dsort.size for i in dsort])
                ax.plot(dsort,cumProb,color=clr,label=trainingPhase)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xlim(([0,1.2] if fixedParam == 'Full model' else [-0.05,0.17]))
        ax.set_ylim([0,1.01])
        ax.set_xlabel(('NLL' if fixedParam == 'Full model' else r'$\Delta$ NLL'))
        ax.set_title((fixedParam if fixedParam == 'Full model' else fixedParam+'='+str(fixedVal)))
        if i==0:
            ax.legend(bbox_to_anchor=(1,1))
    plt.tight_layout()
                
                
# plot param values
for modelType in modelTypes:
    fig = plt.figure(figsize=(11,11))
    gs = matplotlib.gridspec.GridSpec(len(fixedParamNames),len(paramNames))
    for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
        for j,(param,xlim) in enumerate(zip(paramNames,paramBounds)):
            ax = fig.add_subplot(gs[i,j])
            for trainingPhase,clr in zip(trainingPhases,trainingPhaseColors):
                d = modelData[trainingPhase]
                if len(d) > 0:
                    paramVals = np.array([np.mean([session[modelType]['params'][i,j] for session in mouse.values()]) for mouse in d.values()])
                    dsort = np.sort(paramVals)
                    cumProb = np.array([np.sum(dsort<=s)/dsort.size for s in dsort])
                    ax.plot(dsort,cumProb,color=clr,label=trainingPhase)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False)
            ax.set_xlim([xlim[0]-0.02,xlim[1]+0.02])
            ax.set_ylim([0,1.01])
            if j>0:
                ax.set_yticklabels([])
            if i<len(fixedParamNames)-1:
                ax.set_xticklabels([])
            else:
                ax.set_xlabel(param)
            if j==0 and i==len(fixedParamNames)//2:
                ax.set_ylabel('Cum. Prob.')
            if j==len(paramNames)//2:
                ax.set_title((fixedParam if fixedParam == 'Full model' else fixedParam+'='+str(fixedVal)))
            if i==0 and j==len(paramNames)-1:
                ax.legend(bbox_to_anchor=(1,1))
    plt.tight_layout()


# compare model and mice
modelType = 'contextQ'
var = 'qTotal'
stimNames = ('vis1','vis2','sound1','sound2')
preTrials = 5
postTrials = 15
x = np.arange(-preTrials,postTrials+1)
for trainingPhase in trainingPhases:
    fig = plt.figure(figsize=(12,10))
    nRows = int(np.ceil((len(fixedParamNames)+1)/2))
    gs = matplotlib.gridspec.GridSpec(nRows,4)
    for i,(fixedParam,fixedVal) in enumerate(zip(('mice',) + fixedParamNames,(None,)+fixedParamValues)):
        if fixedParam == 'mice':
            d = sessionData[trainingPhase]
        else:
            d = modelData[trainingPhase]
        if len(d) == 0:
            continue
        for j,(rewardStim,blockLabel) in enumerate(zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks'))):
            if i>=nRows:
                row = i-nRows
                col = j+2
            else:
                row,col = i,j
            ax = fig.add_subplot(gs[row,col])
            for stim,clr,ls in zip(stimNames,'ggmm',('-','--','-','--')):
                y = []
                for mouse in d:
                    y.append([])
                    for session in d[mouse]:
                        obj = sessionData[trainingPhase][mouse][session]
                        if fixedParam == 'mice':
                            resp = obj.trialResponse
                        else:
                            resp = d[mouse][session][modelType][var][fixedParamNames.index(fixedParam)]
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if rewStim==rewardStim and blockInd > 0:
                                trials = (obj.trialStim==stim) & ~obj.autoRewardScheduled
                                y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                pre = resp[(obj.trialBlock==blockInd) & trials]
                                k = min(preTrials,pre.size)
                                y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                post = resp[(obj.trialBlock==blockInd+1) & trials]
                                k = min(postTrials,post.size)
                                y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                    y[-1] = np.nanmean(y[-1],axis=0)
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x,m,color=clr,ls=ls,label=stim)
                ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False)
            ax.set_xticks(np.arange(-5,20,5))
            ax.set_yticks([0,0.5,1])
            ax.set_xlim([-preTrials-0.5,postTrials+0.5])
            ax.set_ylim([0,1.01])
            if i==len(fixedParamNames):
                ax.set_xlabel('Trials after block switch')
            if j==0:
                ax.set_ylabel(('Response\nrate' if fixedParam=='mice' else var))
            if fixedParam=='mice':
                title = 'mice, '+blockLabel+' (n='+str(len(y))+')'
            elif fixedParam=='Full model':
                title = fixedParam
            else:
                title = fixedParam+'='+str(fixedVal)
            ax.set_title(title)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1))
    plt.tight_layout()
            
preTrials = 0
postTrials = 15
x = np.arange(-preTrials,postTrials+1)
for var,yticks,ylim,ylbl in zip(('prediction','expectedValue'),([0,0.5,1],[-1,0,1]),([0,1.01],[-1.01,1.01]),('Response\nrate','Expected\nvalue')):
    if var=='expectedValue':
        continue
    for trainingPhase in trainingPhases:
        fig = plt.figure(figsize=(8,10))
        gs = matplotlib.gridspec.GridSpec(len(fixedParamNames)+1,2)
        for i,(fixedParam,fixedVal) in enumerate(zip(('mice',) + fixedParamNames,(None,)+fixedParamValues)):
            if fixedParam == 'mice':
                d = sessionData[trainingPhase]
            else:
                d = modelData[trainingPhase]
            if len(d) == 0:
                continue
            for j,(rewardStim,blockLabel) in enumerate(zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks'))):
                ax = fig.add_subplot(gs[i,j])
                for stim,clr,ls in zip(stimNames,'ggmm',('-','--','-','--')):
                    y = []
                    for mouse in d:
                        y.append([])
                        for session in d[mouse]:
                            obj = sessionData[trainingPhase][mouse][session]
                            if fixedParam == 'mice':
                                resp = obj.trialResponse
                            else:
                                resp = d[mouse][session][modelType][var][fixedParamNames.index(fixedParam)]
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if rewStim==rewardStim and blockInd == 0:
                                    trials = (obj.trialStim==stim) & ~obj.autoRewardScheduled
                                    y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                    pre = resp[(obj.trialBlock==blockInd) & trials]
                                    k = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                    post = resp[(obj.trialBlock==blockInd+1) & trials]
                                    k = min(postTrials,post.size)
                                    y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                        y[-1] = np.nanmean(y[-1],axis=0)
                    m = np.nanmean(y,axis=0)
                    s = np.nanstd(y,axis=0)/(len(y)**0.5)
                    ax.plot(x,m,color=clr,ls=ls,label=stim)
                    ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False)
                ax.set_xticks(np.arange(-5,20,5))
                ax.set_yticks(([0,0.5,1] if fixedParam=='mice' else yticks))
                ax.set_xlim([-preTrials-0.5,postTrials+0.5])
                ax.set_ylim(([0,1.01] if fixedParam=='mice' else ylim))
                if i==len(fixedParamNames):
                    ax.set_xlabel('Trials after block switch')
                if j==0:
                    ax.set_ylabel(('Response\nrate' if fixedParam=='mice' else ylbl))
                if fixedParam=='mice':
                    title = 'mice, '+blockLabel+' (n='+str(len(y))+')'
                elif fixedParam=='Full model':
                    title = fixedParam
                else:
                    title = fixedParam+'='+str(fixedVal)
                ax.set_title(title)
                if i==0 and j==1:
                    ax.legend(bbox_to_anchor=(1,1))
        plt.tight_layout()
        

# plot pContext and wHabit
modelType = 'contextQ'
preTrials = 20
postTrials = 60
x = np.arange(-preTrials,postTrials+1)
for var,ylbl in zip(('pContext','wHabit'),('Context belief','Habit weight')):
    for trainingPhase in trainingPhases:
        d = modelData[trainingPhase]
        if len(d) == 0:
            continue
        fig = plt.figure(figsize=(10,10))
        gs = matplotlib.gridspec.GridSpec(len(fixedParamNames),2)
        for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
            for j,(rewardStim,blockLabel) in enumerate(zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks'))):
                ax = fig.add_subplot(gs[i,j])
                contexts,clrs = (('visual','auditory'),'gm') if var=='pContext' else ((None,),'k')
                for contextInd,(context,clr) in enumerate(zip(contexts,clrs)):
                    y = []
                    for mouse in d:
                        y.append([])
                        for session in d[mouse]:
                            obj = sessionData[trainingPhase][mouse][session]
                            v = d[mouse][session][modelType][var][fixedParamNames.index(fixedParam)]
                            if var=='pContext':
                                v = v[:,contextInd]
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if rewStim==rewardStim and blockInd > 0:
                                    y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                    pre = v[(obj.trialBlock==blockInd)]
                                    k = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                    post = v[(obj.trialBlock==blockInd+1)]
                                    k = min(postTrials,post.size)
                                    y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                        y[-1] = np.nanmean(y[-1],axis=0)
                    m = np.nanmean(y,axis=0)
                    s = np.nanstd(y,axis=0)/(len(y)**0.5)
                    ax.plot(x,m,color=clr,label=context)
                    ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False)
                ax.set_xticks(np.arange(-20,60,20))
                ax.set_yticks([0,0.5,1])
                ax.set_xlim([-preTrials-0.5,postTrials+0.5])
                ax.set_ylim([0,1.01])
                if i==len(fixedParamNames)-1:
                    ax.set_xlabel('Trials after block switch')
                if j==0:
                    ax.set_ylabel(ylbl)
                if fixedParam=='Full model':
                    title = fixedParam+', '+blockLabel
                else:
                    title = fixedParam+'='+str(fixedVal)
                ax.set_title(title)
                if var=='pContext' and i==0 and j==1:
                    ax.legend(bbox_to_anchor=(1,1))
        plt.tight_layout()

preTrials = 0
postTrials = 60
x = np.arange(-preTrials,postTrials+1)
for var,ylbl in zip(('pContext','wHabit'),('Context belief','Habit weight')):
    for trainingPhase in trainingPhases:
        d = modelData[trainingPhase]
        if len(d) == 0:
            continue
        fig = plt.figure(figsize=(10,10))
        gs = matplotlib.gridspec.GridSpec(len(fixedParamNames),2)
        for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
            for j,(rewardStim,blockLabel) in enumerate(zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks'))):
                ax = fig.add_subplot(gs[i,j])
                contexts,clrs = (('visual','auditory'),'gm') if var=='pContext' else ((None,),'k')
                for contextInd,(context,clr) in enumerate(zip(contexts,clrs)):
                    y = []
                    for mouse in d:
                        y.append([])
                        for session in d[mouse]:
                            obj = sessionData[trainingPhase][mouse][session]
                            v = d[mouse][session][modelType][var][fixedParamNames.index(fixedParam)]
                            if var=='pContext':
                                v = v[:,contextInd]
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if rewStim==rewardStim and blockInd == 0:
                                    y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                    pre = v[(obj.trialBlock==blockInd)]
                                    k = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                    post = v[(obj.trialBlock==blockInd+1)]
                                    k = min(postTrials,post.size)
                                    y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                        y[-1] = np.nanmean(y[-1],axis=0)
                    m = np.nanmean(y,axis=0)
                    s = np.nanstd(y,axis=0)/(len(y)**0.5)
                    ax.plot(x,m,color=clr,label=context)
                    ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False)
                ax.set_xticks(np.arange(-20,60,20))
                ax.set_yticks([0,0.5,1])
                ax.set_xlim([-preTrials-0.5,postTrials+0.5])
                ax.set_ylim([0,1.01])
                if i==len(fixedParamNames)-1:
                    ax.set_xlabel('Trials after block switch')
                if j==0:
                    ax.set_ylabel(ylbl)
                if fixedParam=='Full model':
                    title = fixedParam+', '+blockLabel
                else:
                    title = fixedParam+'='+str(fixedVal)
                ax.set_title(title)
                if var=='pContext' and i==0 and j==1:
                    ax.legend(bbox_to_anchor=(1,1))
        plt.tight_layout()
        
        
# plot q values
modelType = 'contextQ'
preTrials = 20
postTrials = 60
for trainingPhase in trainingPhases:
    d = modelData[trainingPhase]
    if len(d) == 0:
        continue
    for qval in ('qContext','qStim'):
        fig = plt.figure(figsize=(10,10))
        gs = matplotlib.gridspec.GridSpec(len(fixedParamNames),2)
        for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
            for j,(rewardStim,blockLabel) in enumerate(zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks'))):
                ax = fig.add_subplot(gs[i,j])
                y = []
                for mouse in d:
                    y.append([])
                    for session in d[mouse]:
                        obj = sessionData[trainingPhase][mouse][session]
                        q = d[mouse][session][modelType][qval][fixedParamNames.index(fixedParam)]
                        if qval=='qContext':
                            q = q.reshape(obj.nTrials,8)
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if rewStim==rewardStim and blockInd > 0:
                                y[-1].append(np.full((q.shape[1],preTrials+postTrials),np.nan))
                                pre = q[(obj.trialBlock==blockInd)]
                                k = min(preTrials,len(pre))
                                y[-1][-1][:,preTrials-k:preTrials] = pre[-k:].T
                                post = q[(obj.trialBlock==blockInd+1)]
                                k = min(postTrials,len(post))
                                y[-1][-1][:,preTrials:preTrials+k] = post[:k].T
                    y[-1] = np.nanmean(y[-1],axis=0)
                m = np.nanmean(y,axis=0)
                im = ax.imshow(m,clim=(0,1),cmap='gray')
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False)
                ax.set_xticks(np.arange(0,preTrials+postTrials,20))
                ax.set_xticklabels(np.arange(-20,postTrials,20))
                # ax.set_yticks([0,0.5,1])
                ax.set_xlim([-0.5,preTrials+postTrials+0.5])
                # ax.set_ylim([0,1.01])
                if i==len(fixedParamNames)-1:
                    ax.set_xlabel('Trials after block switch')
                if j==0:
                    ax.set_ylabel('state')
                if fixedParam=='Full model':
                    title = fixedParam+', '+blockLabel
                else:
                    title = fixedParam+'='+str(fixedVal)
                ax.set_title(title)
                if i==0 and j==1:
                    cb = plt.colorbar(im,ax=ax,fraction=0.05,pad=0.04,shrink=0.5)
                    cb.ax.tick_params(length=0)
                    cb.set_ticks([0,0.5,1])
        plt.tight_layout()


# no reward blocks, target stimuli only
for modelType in modelTypes:
    fig = plt.figure(figsize=(8,10))
    gs = matplotlib.gridspec.GridSpec(len(fixedParamNames)+1,2)
    preTrials = 15
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)  
    for i,(fixedParam,fixedVal) in enumerate(zip(('mice',) + fixedParamNames,(None,)+fixedParamValues)):
        if fixedParam == 'mice':
            d = sessionData['no reward']
        else:
            d = modelData['no reward']
        if len(d) == 0:
            continue
        for j,(blockRewarded,title) in enumerate(zip((True,False),('switch to rewarded block','switch to unrewarded block'))):
            ax = fig.add_subplot(gs[i,j])
            ax.plot([0,0],[0,1],'--',color='0.5')
            for stimLbl,clr in zip(('previously rewarded target stim','other target stim'),'mg'):
                y = []
                for mouse in d:
                    y.append([])
                    for session in d[mouse]:
                        obj = sessionData['no reward'][mouse][session]
                        if fixedParam == 'mice':
                            resp = obj.trialResponse
                        else:
                            resp = d[mouse][session][modelType]['prediction'][fixedParamNames.index(fixedParam)]
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0 and ((blockRewarded and rewStim != 'none') or (not blockRewarded and rewStim == 'none')):
                                if blockRewarded:
                                    stim = np.setdiff1d(('vis1','sound1'),rewStim) if 'previously' in stimLbl else rewStim
                                else:
                                    prevRewStim = obj.blockStimRewarded[blockInd-1]
                                    stim = np.setdiff1d(('vis1','sound1'),prevRewStim) if 'other' in stimLbl else prevRewStim
                                trials = (obj.trialStim==stim)
                                y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                pre = resp[(obj.trialBlock==blockInd) & trials]
                                k = min(preTrials,pre.size)
                                y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                post = resp[(obj.trialBlock==blockInd+1) & trials]
                                k = min(postTrials,post.size)
                                y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                    y[-1] = np.nanmean(y[-1],axis=0)
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x,m,color=clr,label=stimLbl)
                ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xticks(np.arange(-20,21,5))
            ax.set_yticks([0,0.5,1])
            ax.set_xlim([-preTrials-0.5,postTrials+0.5])
            ax.set_ylim([0,1.01])
            ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
            ax.set_ylabel('Response rate',fontsize=12)
            # ax.legend(bbox_to_anchor=(1,1),loc='upper left')
            # ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=12)
    plt.tight_layout()

for modelType in modelTypes:
    for var,ylbl in zip(('pContext','wHabit'),('Context belief','Habit weight')):
        fig = plt.figure(figsize=(10,10))
        gs = matplotlib.gridspec.GridSpec(len(fixedParamNames)+1,2)
        preTrials = 20
        postTrials = 60
        x = np.arange(-preTrials,postTrials+1)  
        for i,(fixedParam,fixedVal) in enumerate(zip(fixedParamNames,fixedParamValues)):
            d = modelData['no reward']
            if len(d) == 0:
                continue
            for j,(blockRewarded,blockLabel) in enumerate(zip((True,False),('switch to rewarded block','switch to unrewarded block'))):
                ax = fig.add_subplot(gs[i,j])
                ax.plot([0,0],[0,1],'--',color='0.5')
                contexts,clrs = (('visual','auditory'),'gm') if var=='pContext' else ((None,),'k')
                for contextInd,(context,clr) in enumerate(zip(contexts,clrs)):
                    y = []
                    for mouse in d:
                        y.append([])
                        for session in d[mouse]:
                            obj = sessionData['no reward'][mouse][session]
                            v = d[mouse][session][modelType][var][fixedParamNames.index(fixedParam)]
                            if var=='pContext':
                                v = v[:,contextInd]
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if blockInd > 0 and ((blockRewarded and rewStim != 'none') or (not blockRewarded and rewStim == 'none')):
                                    y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                    pre = v[obj.trialBlock==blockInd]
                                    k = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-k:preTrials] = pre[-k:]
                                    post = v[obj.trialBlock==blockInd+1]
                                    k = min(postTrials,post.size)
                                    y[-1][-1][preTrials+1:preTrials+1+k] = post[:k]
                        y[-1] = np.nanmean(y[-1],axis=0)
                    m = np.nanmean(y,axis=0)
                    s = np.nanstd(y,axis=0)/(len(y)**0.5)
                    ax.plot(x,m,color=clr,label=context)
                    ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False,labelsize=10)
                ax.set_xticks(np.arange(-20,60,20))
                ax.set_yticks([0,0.5,1])
                ax.set_xlim([-preTrials-0.5,postTrials+0.5])
                ax.set_ylim([0,1.01])
                if i==len(fixedParamNames)-1:
                    ax.set_xlabel('Trials after block switch')
                if j==0:
                    ax.set_ylabel(ylbl)
                if fixedParam=='Full model':
                    title = fixedParam+', '+blockLabel
                else:
                    title = fixedParam+'='+str(fixedVal)
                ax.set_title(title)
                if var=='pContext' and i==0 and j==1:
                    ax.legend(bbox_to_anchor=(1,1))
        plt.tight_layout()



