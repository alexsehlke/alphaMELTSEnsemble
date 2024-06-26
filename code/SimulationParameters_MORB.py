import os
from collections import OrderedDict
import numpy as np
from CombineMELTSEnsemble import Make2DCrossSection

# Only needs to be done if changing bulk composition or initial conditions/parameterization.
DoMELTSSims = True
# Only needs to be run if we changed the fitindex properties or something like that.
DoAnalysis = True
# We should replot.
DoPlotting = True

# Set up directory structure
# Location to the alphamelts executable.
alphaMELTSLocation = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'alphamelts')
# Location to where to put the compute files.
ComputeScratchSpace = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ComputeScratchSpace')

# Constant inputs
ConstantInputs = dict()
ConstantInputs['Title'] = 'VaryfO2'
ConstantInputs['Buffer'] = 'QFM'
# Set the temperature.  Because this is a single value, there will only be an initial temperature entry made in the inputs melt file.
ConstantInputs['T'] = 1600 # Temperature
ConstantInputs['P'] = 1 # Bar
# And so for all the elements.
ConstantInputs['SiO2'] = 48.68
ConstantInputs['TiO2'] = 1.01
ConstantInputs['Al2O3'] = 17.64
ConstantInputs['Cr2O3'] = 0.03
ConstantInputs['Fe2O3'] = 0.89
ConstantInputs['FeO'] = 7.59
ConstantInputs['MnO'] = 0.00
ConstantInputs['MgO'] = 9.10
ConstantInputs['CaO'] = 12.45
ConstantInputs['Na2O'] = 2.65
ConstantInputs['K2O'] =  0.03
ConstantInputs['P2O5'] =  0.08
ConstantInputs['H2O'] =  0.20
ConstantInputs['NiO'] = 0.00

# Set up the inputs to the simulation that vary.
ParameterizedInputs = OrderedDict()
# Set the fugacity.  Because this is a set of values, a new MELTS simulation will be created for each value.
ParameterizedInputs['fO2'] = np.arange(-6, 6, 0.125)
# ParameterizedInputs['Na2O'] = np.arange(0.00, 5.00, 1)

# Create a dictionary for each phase that we want to include in a fit index.
# Each phase has a dictionary for all the oxides to include.
TargetCompositions = dict()
#TargetCompositions['Olivine'] = {'SiO2':41.626, 'MgO':48.536, 'FeO':7.849}#, 'MnO':1.494, 'CaO':0.101, 'Cr2O3':0.394}
#TargetCompositions['Orthopyroxene'] = {'SiO2':54.437, 'MgO':31.335, 'FeO':4.724}
#TargetCompositions['Alloy-Liquid'] = {'Fe':91.428, 'Ni':8.572}
#TargetCompositions['Liquid'] = {'SiO2':48.736, 'MgO':25.867}

# At the end of the plotting stage, after all data is gathered and processed, which final plots do you want to draw?
def DrawEnsemblePlots(ComputeScratchSpace, DataGrid):

    #fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Olivine/Temperature', 'MELTS/Olivine/FitIndex', SavePath=os.path.join(ComputeScratchSpace, 'FitIndexOlivine.pdf'))

    #fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Orthopyroxene/Temperature', 'MELTS/Orthopyroxene/FitIndex', SavePath=os.path.join(ComputeScratchSpace, 'FitIndexOrthopyroxene.pdf'))

    #fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Liquid/Temperature', 'MELTS/Liquid/FitIndex', SavePath=os.path.join(ComputeScratchSpace, 'FitIndexLiquid.pdf'))

    #fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/CombinedFitIndex/Temperature', 'MELTS/CombinedFitIndex/FitIndex', SavePath=os.path.join(ComputeScratchSpace, 'FitIndexCombined.pdf'))

    #fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Olivine/Temperature', 'MELTS/Olivine/FeO', SavePath=os.path.join(ComputeScratchSpace, 'OlivineMgO.pdf'))

    #Plot Olivine Forsterite Component
    fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Olivine/Temperature', 'MELTS/Olivine/Fo', SavePath=os.path.join(ComputeScratchSpace, 'Olivine_Fo.pdf'))
    
    #Plot Feldspar Anorthite Component
    fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Plagioclase/Temperature', 'MELTS/Plagioclase/An#', SavePath=os.path.join(ComputeScratchSpace, 'Plagioclase_An.pdf'))

    #Plot Spinel Component
    fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Spinel/Temperature', 'MELTS/Spinel/MgOverTet', SavePath=os.path.join(ComputeScratchSpace, 'Spinel_MgOverTet.pdf'))

    #Plot Orthopyroxene Component
    fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Orthopyroxene/Temperature', 'MELTS/Orthopyroxene/Mg#', SavePath=os.path.join(ComputeScratchSpace, 'Orthopyroxene_Mg-number.pdf'))

    #Plot Clinopyroxene Component
    fO2Axis, TempAxis, CrossSec = Make2DCrossSection(DataGrid, 'fO2', 'MELTS/Clinopyroxene/Temperature', 'MELTS/Clinopyroxene/Mg#', SavePath=os.path.join(ComputeScratchSpace, 'Clinopyroxene_Mg-number.pdf'))
