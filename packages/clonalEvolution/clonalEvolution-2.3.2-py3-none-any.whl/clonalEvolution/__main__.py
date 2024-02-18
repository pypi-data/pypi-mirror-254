import sys
import os
import copy
from pathlib import Path
import numpy as np
import pandas as pd
import scipy as sc
from multiprocessing import Process

import clonalEvolution.clonal_evolution_init as CEML
import clonalEvolution.external_plots as external_plots
from clonalEvolution.mainView import run

# import clonal_evolution_init as CEML
# import external_plots as external_plots
# from mainView import run

disclaimer = '''Cellular/Microbial Clonal Evolution simulations basing on Gillespie algorithm. Copyright (C) 2022 by Jarosław Gil. 
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.'''

class WrongParameter(Exception):
    pass

def loadPaths(fname):        
    # self.showDialog("Select file same as resume simulation", "Info")
    xname = fname.split('/')
    
    ##TODO interpret only last number!!!
    
    path = ""
    name = ""
    _last_cycle = 0
    for i in xname:
        if xname.index(i) == len(xname)-1:
            t = i.split('_')
            t = t[len(t)-1]
            _last_cycle = int(''.join(x for x in t if x.isdigit()))
            if i.endswith('.csv'):
                name = i.rstrip('_' + str(_last_cycle) + '.csv')
            elif i.endswith('.txt'):
                name = i.rstrip('_' + str(_last_cycle) + '.txt')
        else:
            path = path + i + '/'
    
    if name.endswith("_binned"):
        name = name.rstrip("_binned")
    else:
        name = name.rstrip("_single")
 
    return [name, path, _last_cycle]

def saveParams(dfp, output):           
    filepath = Path(output + '/params'  + ".csv")  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    dfp.to_csv(filepath)  

def _help():
    print("Usage: if parameter is not set, default value will be used")
    print("To run grafical version of software simply type clonalEvolution without parameters")
    print("opt \t | description \t \t \t | default value")
    print("-----------------------------------------------------")
    print("-p \t | initial population size \t | 1000")
    print("-c \t | population capacity \t \t | 1000")
    print("-s \t | simulation steps (not used) \t | 100")
    print("-t \t | tau step \t \t \t | 0.005")
    print("-ct \t | cycle time \t \t \t | 1")
    print("-mp \t | mutation probabilities \t | 0.0001,0.1")
    print("-me \t | mutation effects \t \t | 0.1,0.001")
    print("-th \t | used threads \t \t | 1")
    print("-----------------------------------------------------")
    print("mutation effects and probabilities values (driver,passanger) should be separeted only by ,")
    print("more than two calues of mutation effects and probabilities are ignored")
    print("default value is set when wrong or no parameter value is provided")
    print()
    print("Additional parameters:")
    print("opt \t \t | description")
    print("-----------------------------------------------------")
    print("-out \t \t | save files localization (obligatory)")
    print("-fname \t \t | output file name (obligatory)")
    print("-par \t \t | load simulation parameters - path and file name")
    print("-save \t \t | ack to save simulation data (default: False)")
    print("-save_p \t | save params to file")
    print("-crit \t \t | print critical population value")
    print("-binned \t | type for binned version (medium priority)")
    print("-matrix \t | type for matrix version (big priority)")
    print("-plot \t \t | type for matrix version (big priority)")
    print("-----------------------------------------------------")
    print()
    print("To resume simulation provide:")
    print("-resume (-binned/matrix {optional}) -par parameters_file -file file_to_resume (-save {optional})")
    print("In path use / symbol not \\ !")
    print()
    print(disclaimer)

def checkParams(p):
    try:
        pop = int(np.where(p == '-p')[0][0])
        pop = pop + 1
        pop = int(p[pop])
    except:
        pop = 1000
        
    try:
        cap = int(np.where(p == '-c')[0][0])
        cap = cap + 1
        cap = int(p[cap])
    except:
        cap = 1000
    
    try:
        steps = int(np.where(p == '-s')[0][0])
        steps = steps + 1
        steps = int(p[steps])
    except:
        steps = 100
    
    try:
        tau = int(np.where(p == '-t')[0][0])
        tau = tau + 1
        tau = float(p[tau])
    except:
        tau = 0.005
        
    try:
        skip = int(np.where(p == '-ct')[0][0])
        skip = skip + 1
        skip = int(p[skip])
    except:
        skip = 1
        
    try:
        mut_prob = int(np.where(p == '-mp')[0][0])
        mut_prob = mut_prob + 1
        mut_prob = p[mut_prob].split(',')
        mut_prob = [float(x) for x in mut_prob]
    except:
        mut_prob = [0.0001, 0.1]
    
    try:
        mut_effect = int(np.where(p == '-me')[0][0])
        mut_effect = mut_effect + 1
        mut_effect = p[mut_effect].split(',')
        mut_effect = [float(x) for x in mut_effect]
        mut_effect[1] = -mut_effect[1]
    except:
        mut_effect = [0.1, -0.001]
        
    try:
        threads = int(np.where(p == '-th')[0][0])
        threads = threads + 1
        threads = int(p[threads])
    except:
        threads = 1
        
    dfp = pd.DataFrame({
                'pop': pop,
                'cap': cap,
                'steps': steps,
                'tau': tau,
                'skip': skip,
                'mut_prob': [mut_prob],
                'mut_effect': [mut_effect],
                'threads': threads
            }, index=[0])
    print(dfp)
    return dfp

def loadParams(_in):
    dfp = pd.read_csv(_in)
    dfp = pd.DataFrame({
        'pop': int(dfp['pop'][0]),
        'cap': int(dfp['cap'][0]),
        'steps': int(dfp['steps'][0]),
        'tau': float(dfp['tau'][0]),
        'skip': float(dfp['skip'][0]),
        'mut_prob': [[float(x.strip('[]')) for x in (dfp['mut_prob'][0].split(','))]],
        'mut_effect': [[float(x.strip('[]')) for x in (dfp['mut_effect'][0].split(','))]],
        'threads': int(dfp['threads'][0])
        }, index = [0])
    return dfp

def main():
    if len(sys.argv) == 1:
        run()
    else:
        p = np.array(sys.argv)
        if len(p[p=='-h']) > 0:
            _help()
        elif len(p[p=='-plot']) > 0:
            print('plot')
        elif len(p[p=='-resume']) > 0:
            _in = ""
            _file = ""
            try:
                _in = int(np.where(p == '-par')[0][0])
                _in = _in + 1
                _in = p[_in]
                _file = int(np.where(p == '-file')[0][0])
                _file = _file + 1
                _file = p[_file]
            except:
                print('Enter parameters path and file correctly')
                return
            dfp = loadParams(_in)
            
            plots = 0
            if len(p[p=='-save'])>0:
                plots = 16
            
            [name, output, cycle] = loadPaths(_file)
            
            print(name)
            print(output)
            print(cycle)
            
            os.chdir(output)
            
            if len(p[p=='-matrix'])>0:
                df = pd.read_csv(_file)
                df = df.drop('Unnamed: 0', axis=1)
                mm = []
                for row in df.iterrows():
                    mm.append(sc.sparse.load_npz(row[1]['Mutation matrix']))
                df['Mutation matrix'] = mm
                for i in range(len(df)):
                    try:
                        df.at[i,'Driver mutation list'] = [int(x.strip('[]')) for x in df.loc[i,'Driver mutation list'].split(',')]
                    except ValueError:
                        df.at[i,'Driver mutation list'] = []
                        
                    try:
                        df.at[i,'Uniqal passenger mutation list'] = [int(x.strip('[]')) for x in df.loc[i,'Uniqal passenger mutation list'].split(',')]
                    except ValueError:
                        df.at[i,'Uniqal passenger mutation list'] = []
                        
                    try:
                        df.at[i,'Clone fitness'] = np.array([float(x.strip('[]')) for x in df.loc[i,'Clone fitness'].split(',')])
                    except ValueError:
                        df.at[i,'Clone fitness'] = np.array([])
                        
                iPop = df.to_numpy().tolist()
                
                CEML.clonalEvolutionMainLoop(iPop, 
                                        copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                                        name, "", output, plots, t_iter=cycle+1, select=2)
            elif len(p[p=='-binned'])>0:
                df = external_plots.loadFile(_file)
                iClone = df['Clone number'].tolist()
                iCells = df['Cells number'].tolist()
                iFit = df['Mean fitness'].tolist()
                iMut = df['Mean mutation number'].tolist()
                iDriv = df['Driver mutation list'].tolist()
                iPass = df['Passener mutation list'].tolist()
                iParent = df['Previous clone number'].tolist()
                
                del df                  
                
                CEML.clonalEvolutionMainLoop(np.array([copy.deepcopy(iClone),
                                                  copy.deepcopy(iCells),
                                                  copy.deepcopy(iFit),
                                                  copy.deepcopy(iMut),
                                                  copy.deepcopy(iDriv),
                                                  copy.deepcopy(iPass),
                                                  copy.deepcopy(iParent)]).T.tolist(), 
                                        copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                                        name, "", output, plots, t_iter=cycle+1, select=1)
            else:
                df = pd.read_csv(_file)
                iMuts = df['Mutations'].tolist()
                iClones = df['Clone'].tolist()
                iProp = df['Fitness'].tolist()
                iMutations = df['Mutations_ID'].tolist()
                iEffect = df['Mutations_effect'].tolist()
                iParent = df['Parent clone'].tolist()
                
                del df
                
                iMutations = [x.split(',') for x in iMutations]
                for x in range(len(iMutations)):
                    for i in range(len(iMutations[x])):
                        iMutations[x][i] = float(iMutations[x][i].strip('[]'))
                    
                iEffect = [x.split(',') for x in iEffect]
                for x in range(len(iEffect)):
                    for i in range(len(iEffect[x])):
                        iEffect[x][i] = float(iEffect[x][i].strip('[]'))
                        
                CEML.clonalEvolutionMainLoop(np.array([copy.deepcopy(iMuts),
                                                       copy.deepcopy(iProp), 
                                                       copy.deepcopy(iClones), 
                                                       copy.deepcopy(iMutations), 
                                                       copy.deepcopy(iEffect),
                                                       copy.deepcopy(iClones)]).T.tolist(), 
                                             copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                                             name, "", output, plots, t_iter=cycle+1, select=0)       
        else:
            dfp = []
            if p[p=='-par']:
                _in = ""
                try:
                    _in = int(np.where(p == '-par')[0][0])
                    _in = _in + 1
                    _in = p[_in]
                except:
                    print('Enter save path')
                    return
                dfp = loadParams(_in)
            else:
                dfp = checkParams(p)
                
            output = ""
            name = ""
            plots = 0
            try:
                output = int(np.where(p == '-out')[0][0])
                output = output + 1
                output = p[output]
                
                name = int(np.where(p == '-fname')[0][0])
                name = name + 1
                name = p[name]
            except:
                print('Enter save path and name')
                return
            
            if len(p[p=="-save_p"]) > 0:
                saveParams(dfp, output)
            if len(p[p=="-crit"]) > 0:
                a = dfp['mut_prob'][0]
                b = dfp['mut_effect'][0]
                print(round((a[1]/a[0])*(b[1]/b[0]**2),0))
            if len(p[p=="-save"]) > 0:
                    plots = 16   
                    
            if len(p[p=='-matrix'])>0:
                iPop = [[0, dfp['pop'][0], [], [0], sc.sparse.csr_matrix(np.array([[0] for x in range(dfp['pop'][0])])), np.ones(dfp['pop'][0]), 0]]
                CEML.clonalEvolutionMainLoop(iPop,
                                             copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                                             name, "", output, plots, select=2)
            elif len(p[p=="-binned"]) > 0:
                iPop = [[0, dfp['pop'][0], 1, 0, [], [], 0]]
                CEML.clonalEvolutionMainLoop(iPop, 
                      copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                      name, "", output, plots, select=1)
            else:                                
                iMuts = np.zeros(dfp['pop'][0], dtype=np.int64).tolist()
                iProp = np.ones(dfp['pop'][0]).tolist()
                iClones = np.zeros(dfp['pop'][0], dtype=np.int64).tolist()
                iMutations = [[] for x in range(len(iMuts))]
                iEffect =[[] for x in range(len(iMuts))]
                
                CEML.clonalEvolutionMainLoop(np.array([copy.deepcopy(iMuts),
                                                       copy.deepcopy(iProp), 
                                                       copy.deepcopy(iClones), 
                                                       copy.deepcopy(iMutations), 
                                                       copy.deepcopy(iEffect),
                                                       copy.deepcopy(iClones)]).T.tolist(), 
                                             copy.deepcopy([dfp['pop'][0], dfp['cap'][0], dfp['steps'][0], dfp['tau'][0], dfp['skip'][0], dfp['mut_prob'][0], dfp['mut_effect'][0], dfp['threads'][0]]), 
                                             name, "", output, plots, select=0)              

def adminMode():
    p = np.array(sys.argv)
    # N = p[int(np.where(p == '-N')[0][0]) + 1]        
    # N = np.array(list(map(lambda x: int(x), N.split(','))))   
    # N = 10**np.array(range(N[0],N[1]+1,N[2]))     

    # s = p[int(np.where(p == '-S')[0][0]) + 1]        
    # sx = np.array(list(map(lambda x: float(x), s.split(','))))   
    # s = np.arange(0,sx[1],sx[2])  
    # s[0] = sx[0]
    # if(sx[0] != sx[1]):
    #     s = np.append(s,sx[1])                 
        
    # f = p[int(np.where(p == '-F')[0][0]) + 1]        
    # fx = np.array(list(map(lambda x: float(x), f.split(','))))   
    # f = np.arange(0,fx[1],fx[2])  
    # f[0] = fx[0]
    # if(fx[0] != fx[1]):
    #     f = np.append(f,fx[1])          

    # ps = p[int(np.where(p == '-PS')[0][0]) + 1]        
    # psx = np.array(list(map(lambda x: float(x), ps.split(','))))   
    # ps = np.arange(0,psx[1],psx[2])  
    # ps[0] = psx[0]
    # if(psx[0] != psx[1]):
    #     ps = np.append(ps,psx[1])                 
        
    # pf = p[int(np.where(p == '-PF')[0][0]) + 1]        
    # pfx = np.array(list(map(lambda x: float(x), pf.split(','))))   
    # pf = np.arange(0,pfx[1],pfx[2])  
    # pf[0] = pfx[0]
    # if(pfx[0] != pfx[1]):
    #     pf = np.append(pf,pfx[1])   
    
    N = np.array([10000])
    f = np.array([0.02, 0.02])
    s = np.array([0, -0.001])
    pf = np.array([0.0005, 0.0005])
    ps = np.array([0.01, 0.01])
    
    if len(pf) == len(ps) and len(ps) == len(f) and len(f) == len(s):
        effects = np.array([s,f,ps,pf])
        tau,step,ct,multiply,kind,path,save,save_p,end = [0.005,10000,50,10,0,'',0,0,10]

        try:
            tau = float(p[int(np.where(p == '-t')[0][0]) + 1])
        except:
            WrongParameter()
        try:
            step = float(p[int(np.where(p == '-s')[0][0]) + 1])
        except:
            WrongParameter()
        try:
            ct = float(p[int(np.where(p == '-ct')[0][0]) + 1])  
        except:
            WrongParameter() 
        try:
            multiply = int(p[int(np.where(p == '-x')[0][0]) + 1])  
        except:
            WrongParameter()             
        try:
            end = int(p[int(np.where(p == '-end')[0][0]) + 1])
        except:
            WrongParameter()
        
        kind = 0 + 1*bool(len(p[p=='-binned'])) + 2*bool(len(p[p=='-matrix']))
        path = ''
        save = 16*bool(len(p[p=='-save']))
        save_p = bool(len(p[p=='-save_params']))
        if save or save_p:
            try:
                path = p[int(np.where(p == '-path')[0][0]) + 1]
            except:
                print('path is obligatory when saving!')
                return
        
        percent_max = len(N) * len(s)
        percent = 0
        processes = []
        for w in range(2):
            for i in N:   
                for mul in range(multiply):                         
                    pop = i
                    cap = i
                    for sx,fx,psx,pfx in effects.T:
                        percent = percent + 1
                        name = 'single' * (kind == 0) + 'binned' * (kind == 1) + 'matrix' * (kind == 2)
                        pathout = path + '/' + str(w*25 + mul) + '_' + name + '_' + str(i) + '/probability_' + str(psx) + '_' + str(pfx) + '/effect_'  + str(sx) + '_' + str(fx) + '/'
                        params = copy.deepcopy([pop, cap, step, tau, ct, [pfx, psx], [fx, sx], 8])   
                        
                        if save_p:
                            dfp = pd.DataFrame({
                                    'pop': pop,
                                    'cap': cap,
                                    'steps': step,
                                    'tau': tau,
                                    'skip': ct,
                                    'mut_effect': [[fx, sx]],
                                    'mut_prob': [[pfx, psx]],
                                    'threads': 8
                                }, index=[0])
                            
                            filepath = Path(pathout + '/params'  + ".csv")  
                            filepath.parent.mkdir(parents=True, exist_ok=True)  
                            dfp.to_csv(filepath)  
                        pr = 0
                        if kind == 1:
                            iPop = [[0, pop, 1, 0, [], [], 0]]
                            pr = (Process(target=CEML.clonalEvolutionMainLoop, args=(iPop, params, name, "", pathout, save, -1, None, percent, kind, end)))
                        elif kind == 2:
                            iPop = [[0, pop, [], [0], sc.sparse.csr_matrix(np.array([[0] for x in range(pop)])), np.ones(pop), 0]]                    
                            pr = (Process(target=CEML.clonalEvolutionMainLoop, args=(iPop, params, name, "", pathout, save, -1, None, percent, kind, end)))
                        else:
                            iMuts = np.zeros(pop, dtype=np.int64).tolist()
                            iProp = np.ones(pop).tolist()
                            iClones = np.zeros(pop, dtype=np.int64).tolist()
                            iMutations = [[] for x in range(len(iMuts))]
                            iEffect =[[] for x in range(len(iMuts))]  
                            
                            iPop = np.array([copy.deepcopy(iMuts), copy.deepcopy(iProp), copy.deepcopy(iClones), copy.deepcopy(iMutations), copy.deepcopy(iEffect), copy.deepcopy(iClones)]).T.tolist()
                            pr = (Process(target=CEML.clonalEvolutionMainLoop, args=(iPop, params, name, "", pathout, save, -1, None, percent, kind, end)))
                            # CEML.clonalEvolutionMainLoop(iPop, params, name, "", pathout, save, -1, None, percent, kind)
                        pr.start()
                        print(str(round(percent/percent_max,3)*100) + '%')
                        processes.append(pr)
                for pr in processes:
                    pr.join()
                active = True
                while active:
                    ax = list(map(lambda x: x.is_alive(), processes))
                    active = any(ax)
    else:
        print('s, f, ps and pf vectors should be same size')
        
if __name__ == "__main__":
    p = np.array(sys.argv)
    print(p)
    if(p[p=='--admin']):
        adminMode()
    else:
        main()