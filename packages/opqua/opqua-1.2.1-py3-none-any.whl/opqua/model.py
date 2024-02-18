
"""Contains class Model; main class user interacts with."""

import numpy as np
import pandas as pd
import textdistance as td
import itertools as it
import copy as cp
import seaborn as sns
import joblib as jl

from opqua.internal.host import Host
from opqua.internal.vector import Vector
from opqua.internal.population import Population
from opqua.internal.setup import Setup
from opqua.internal.intervention import Intervention
from opqua.internal.simulation import Simulation
from opqua.analysis.data import saveToDf, getPathogens, getProtections, \
    getPathogenDistanceHistoryDf
from opqua.analysis.plot import populationsPlot, compartmentPlot, \
    compositionPlot, clustermap

class Model(object):
    """Class defines a Model.

    This is the main class that the user interacts with.

    The Model class contains populations, setups, and interventions to be used
    in simulation. Also contains groups of hosts/vectors for manipulations and
    stores model history as snapshots for each time point.

    *** --- CONSTANTS: --- ***
    ### Color scheme constants ###
    CB_PALETTE -- a colorblind-friendly 8-color color scheme
    DEF_CMAP -- a colormap object for Seaborn plots

    *** --- ATTRIBUTES: --- ***
    random -- Numpy Generator instance for random numbers
    populations -- dictionary with keys=population IDs, values=Population
        objects
    setups -- dictionary with keys=setup IDs, values=Setup objects
    interventions -- contains model interventions in the order they will occur
    groups -- dictionary with keys=group IDs, values=lists of hosts/vectors
    history -- dictionary with keys=time values, values=Model objects that
        are snapshots of Model at that timepoint
    t_var -- variable that tracks time in simulations

    *** --- METHODS: --- ***

    --- Model Initialization and Simulation: ---

    setRandomSeed -- set random seed for numpy random number generator
    newSetup -- creates a new Setup, save it in setups dict under given name
    saveSetup -- saves Setup parameters to given file location as a CSV file
    loadSetup -- loads Setup parameters from CSV file at given location
    newIntervention -- creates a new intervention executed during simulation
    run -- simulates model for a specified length of time
    runReplicates -- simulate replicates of a model, save only end results
    runParamSweep -- simulate parameter sweep with a model, save only end results
    copyState -- returns a slimmed-down version of the current model state

    --- Data Output and Plotting: ---

    saveToDataFrame -- saves status of model to dataframe, writes to file
    getPathogens -- creates Dataframe with counts for all pathogen genomes
    getProtections -- creates Dataframe with counts for all protection sequences
    populationsPlot -- plots aggregated totals per population across time
    compartmentPlot -- plots number of naive,inf,rec,dead hosts/vectors vs time
    compositionPlot -- plots counts for pathogen genomes or resistance vs. time
    clustermap -- create a heatmap and dendrogram for pathogen genomes in data
    pathogenDistanceHistory -- get pairwise distances for pathogen genomes
    getGenomeTimes -- create DataFrame with times genomes first appeared during
        simulation
    getCompositionData -- create dataframe with counts for pathogen genomes or
        resistance

    --- Model interventions: ---

    - Make and connect populations -
    newPopulation -- create a new Population object with setup parameters
    linkPopulationsHostMigration -- set host migration rate from one population
        towards another
    linkPopulationsVectorMigration -- set vector migration rate from one
        population towards another
    linkPopulationsHostHostContact -- set host-host inter-population contact
        rate from one population towards another
    linkPopulationsHostVectorMigration -- set host-vector inter-population
        contact rate from one population towards another
    linkPopulationsVectorHostMigration -- set vector-host inter-population
        contact rate from one population towards another
    createInterconnectedPopulations -- create new populations, link all of them
        to each other by migration and/or inter-population contact

    - Manipulate hosts and vectors in population -
    newHostGroup -- returns a list of random (healthy or any) hosts
    newVectorGroup -- returns a list of random (healthy or any) vectors
    addHosts -- adds hosts to the population
    addVectors -- adds vectors to the population
    removeHosts -- removes hosts from the population
    removeVectors -- removes vectors from the population
    addPathogensToHosts -- adds pathogens with specified genomes to hosts
    addPathogensToVectors -- adds pathogens with specified genomes to vectors
    treatHosts -- removes infections susceptible to given treatment from hosts
    treatVectors -- removes infections susceptible to treatment from vectors
    protectHosts -- adds protection sequence to hosts
    protectVectors -- adds protection sequence to vectors
    wipeProtectionHosts -- removes all protection sequences from hosts
    wipeProtectionVectors -- removes all protection sequences from vectors

    - Modify population parameters -
    setSetup -- assigns a given set of parameters to this population

    - Utility -
    customModelFunction -- returns output of given function run on model

    --- Preset fitness functions: ---
        * these are static methods

    peakLandscape -- evaluates genome numeric phenotype by decreasing with
        distance from optimal sequence
    valleyLandscape -- evaluates genome numeric phenotype by increasing with
        distance from worst sequence
    """

    ### CONSTANTS ###
    ### Color scheme constants ###
    CB_PALETTE = ["#E69F00", "#56B4E9", "#009E73",
                  "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#999999"]
     # www.cookbook-r.com/Graphs/Colors_(ggplot2)/#a-colorblind-friendly-palette
     # http://jfly.iam.u-tokyo.ac.jp/color/

    DEF_CMAP = sns.cubehelix_palette(
        start=.5, rot=-.75, as_cmap=True, reverse=True
        )


    ### CLASS CONSTRUCTOR ###

    def __init__(self):
        """Create a new Model object."""
        super(Model, self).__init__()
        self.random = np.random.default_rng() # random number generator
        self.populations = {}
            # dictionary with keys=population IDs, values=Population objects
        self.setups = {}
            # dictionary with keys=setup IDs, values=Setup objects
        self.interventions = []
            # contains model interventions in the order they will occur
        self.groups = {}
            # dictionary with keys=group IDs, values=lists of hosts/vectors
        self.history = {}
            # dictionary with keys=time values, values=Model objects that are
            # snapshots of Model at that timepoint
        self.global_trackers = {
                # dictionary keeping track of some global indicators over all
                # the course of the simulation
            'num_events' : { id:0 for id in Simulation.EVENT_IDS.values() },
                # tracks the number of each kind of event in the simulation
            'num_events_over_time' : { id:[0] for id in Simulation.EVENT_IDS.values() },
                # tracks the number of each kind of event in the simulation
            'last_event_time' : 0,
                # time point at which the last event in the simulation happened
            'genomes_seen' : [],
                # list of all unique genomes that have appeared in the
                # simulation
            'custom_conditions' : {}
                # dictionary with keys=ID of custom condition, values=lists of
                # times; every time True is returned by a function in
                # custom_condition_trackers, the simulation time will be stored
                # under the corresponding ID inside
                # global_trackers['custom_condition']
            }
        self.custom_condition_trackers = {}
            # dictionary with keys=ID of custom condition, values=functions that
            # take a Model object as argument and return True or False; every
            # time True is returned by a function in custom_condition_trackers,
            # the simulation time will be stored under the corresponding ID
            # inside global_trackers['custom_condition']

        self.t_var = 0 # used as time variable during simulation

    ### MODEL METHODS ###

    ### Model initialization and simulation: ###

    def setRandomSeed(self, seed):
        """Set random seed for numpy random number generator.

        Arguments:
        seed -- int for the random seed to be passed to numpy (int)
        """

        self.random = np.random.default_rng(seed) # random number generator

    def newSetup(self, name, preset=None, **kwargs):
        """Create a new Setup, save it in setups dict under given name.

        Two preset setups exist: "vector-borne" and "host-host". You may select
        one of the preset setups with the preset keyword argument and then
        modify individual parameters with additional keyword arguments, without
        having to specify all of them.

        Arguments:
        name -- name of setup to be used as a key in model setups dictionary

        Keyword arguments:
        preset -- preset setup to be used: "vector-borne" or "host-host", if
            None, must define all other keyword arguments (default None; None or
            String)
        **kwargs -- setup parameters and values
        """
        self.setups[name] = Setup()
        if preset is not None:
            self.loadSetup(name,None,preset=preset,**kwargs)
        elif len(kwargs) > 0:
            self.setups[name].setParameters(**kwargs)

    def saveSetup(self, setup_id, save_to_file):
        """
        Saves Setup parameters to given file location as a CSV file.

        Functions (e.g. fitness functions) cannot be saved in this format.

        Arguments:
        setup_id -- name of setup used as a key in setups dictionary
        save_to_file -- file path and name to save  parameters under (String)
        """
        self.setups[setup_id].save(save_to_file)

    def loadSetup(self, setup_id, file, preset=None, **kwargs):
        """
        Loads Setup parameters from CSV file at given location.

        Arguments:
        setup_id -- name of setup to be used as a key in setups dictionary
        file -- file path to CSV file with parameters (String)

        Keyword arguments:
        preset -- if using preset parameters, 'host-host' or 'vector-borne'
            (String, default None)
        **kwargs -- setup parameters and values
        """
        if setup_id not in self.setups.keys():
            self.setups[setup_id] = Setup()

        self.setups[setup_id].load(file, preset=preset, **kwargs)

    def newIntervention(self, time, method_name, args):
        """Create a new intervention to be carried out at a specific time.

        Arguments:
        time -- time at which intervention will take place (number >= 0)
        method_name -- intervention to be carried out, must correspond to the
            name of a method of the Model object (String)
        args -- contains arguments for function in positinal order (array-like)
        """

        self.interventions.append( Intervention(time, method_name, args, self) )

    def addCustomConditionTracker(self, condition_id, trackerFunction):
        """Add a function to track occurrences of custom events in simulation.

        Adds function trackerFunction to dictionary custom_condition_trackers
        under key condition_id. Function trackerFunction will be executed at
        every event in the simulation. Every time True is returned,
        the simulation time will be stored under the corresponding condition_id
        key inside global_trackers['custom_condition']

        Arguments:
        condition_id -- ID of this specific condition (String)
        trackerFunction -- function that take a Model object as argument and
            returns True or False; (Function)
        """

        self.custom_condition_trackers['condition_id'] = trackerFunction
        self.global_trackers['custom_conditions']['condition_id'] = []

    def run(
            self,t0,tf,method='exact',dt_leap=None,dt_thre=None,
            time_sampling=0,host_sampling=0,vector_sampling=0,
            skip_uninfected=False,print_every_n_events=1000):
        """Simulate model for a specified time between two time points.

        Simulates a time series using a variation of Gillespie tau-leaping
        algorithm.

        Saves a dictionary containing model state history, with keys=times and
        values=Model objects with model snapshot at that time point under this
        model's history attribute.

        Arguments:
        t0 -- initial time point to start simulation at (number >= 0)
        tf -- initial time point to end simulation at (number >= 0)

        Keyword arguments:
        method -- algorithm to be used; default is approximated solver
            (can be either 'approximated' or 'exact')
        dt_leap -- time leap size used to simulate bursts; if None, set to
            minimum growth threshold time across all populations (number,
            default None)
        dt_thre -- time threshold below which bursts are used; if None, set to
            dt_leap (number, default None)
        time_sampling -- how many events to skip before saving a snapshot of the
            system state (saves all by default), if <0, saves only final state
            (int, default 0)
        host_sampling -- how many hosts to skip before saving one in a snapshot
            of the system state (saves all by default) (int >= 0, default 0)
        vector_sampling -- how many vectors to skip before saving one in a
            snapshot of the system state (saves all by default)
            (int >= 0, default 0)
        skip_uninfected -- whether to save only infected hosts/vectors and
            record the number of uninfected host/vectors instead (Boolean,
            default False)
        """

        sim = Simulation(self)
        self.history = sim.run(
            t0, tf, method, dt_leap, dt_thre, time_sampling, host_sampling,
            vector_sampling, skip_uninfected, print_every_n_events
            )

    def runReplicates(
            self,t0,tf,replicates,method='exact',dt_leap=None,
            dt_thre=None,host_sampling=0,vector_sampling=0,
            skip_uninfected=False,n_cores=0,
            **kwargs):
        """Simulate replicates of a model, save only end results.

        Simulates replicates of a time series using a variation of the Gillespie
        tau-leaping algorithm.

        Saves a dictionary containing model end state state, with keys=times and
        values=Model objects with model snapshot. The time is the final
        timepoint.

        Arguments:
        t0 -- initial time point to start simulation at (number >= 0)
        tf -- initial time point to end simulation at (number >= 0)
        replicates -- how many replicates to simulate (int >= 1)

        Keyword arguments:
        method -- algorithm to be used; default is approximated solver
            (can be either 'approximated' or 'exact')
        dt_leap -- time leap size used to simulate bursts; if None, set to
            minimum growth threshold time across all populations (number,
            default None)
        dt_thre -- time threshold below which bursts are used; if None, set to
            dt_leap (number, default None)
        host_sampling -- how many hosts to skip before saving one in a snapshot
            of the system state (saves all by default) (int >= 0, default 0)
        vector_sampling -- how many vectors to skip before saving one in a
            snapshot of the system state (saves all by default)
            (int >= 0, default 0)
        skip_uninfected -- whether to save only infected hosts/vectors and
            record the number of uninfected host/vectors instead (Boolean,
            default False)
        n_cores -- number of cores to parallelize file export across, if 0, all
            cores available are used (default 0; int >= 0)
        **kwargs -- additional arguents for joblib multiprocessing

        Returns:
        List of Model objects with the final snapshots
        """

        if not n_cores:
            n_cores = jl.cpu_count()

        print('Starting parallel simulations...')

        def run(sim_num):
            model = self.deepCopy()
            sim = Simulation(model)
            mod = sim.run(
                t0,tf,method=method,time_sampling=-1,
                host_sampling=host_sampling,vector_sampling=vector_sampling,
                skip_uninfected=skip_uninfected
                )[tf]
            mod.history = { tf:mod }
            return mod

        return jl.Parallel(n_jobs=n_cores, verbose=10, **kwargs) (
            jl.delayed( run ) (_) for _ in range(replicates)
            )

    def runParamSweep(
            self,t0,tf,setup_id,
            param_sweep_dic={},
            host_population_size_sweep={}, vector_population_size_sweep={},
            host_migration_sweep_dic={}, vector_migration_sweep_dic={},
            host_host_population_contact_sweep_dic={},
            host_vector_population_contact_sweep_dic={},
            vector_host_population_contact_sweep_dic={},
            replicates=1,method='exact',dt_leap=None,dt_thre=None,
            host_sampling=0,vector_sampling=0,skip_uninfected=False,n_cores=0,
            **kwargs):
        """Simulate a parameter sweep with a model, save only end results.

        Simulates variations of a time series using a variation of the Gillespie
        tau-leaping algorithm.

        Saves a dictionary containing model end state state, with keys=times and
        values=Model objects with model snapshot. The time is the final
        timepoint.

        Arguments:
        t0 -- initial time point to start simulation at (number >= 0)
        tf -- initial time point to end simulation at (number >= 0)
        setup_id -- ID of setup to be assigned (String)

        Keyword arguments:
        param_sweep_dic -- dictionary with keys=parameter names (attributes of
            Setup), values=list of values for parameter (list, class of elements
            depends on parameter)
        host_population_size_sweep -- dictionary with keys=population IDs
            (Strings), values=list of values with host population sizes
            (must be greater than original size set for each population, list of
            numbers)
        vector_population_size_sweep -- dictionary with keys=population IDs
            (Strings), values=list of values with vector population sizes
            (must be greater than original size set for each population, list of
            numbers)
        host_migration_sweep_dic -- dictionary with keys=population IDs of
            origin and destination, separated by a colon ';' (Strings),
            values=list of values (list of numbers)
        vector_migration_sweep_dic -- dictionary with keys=population IDs of
            origin and destination, separated by a colon ';' (Strings),
            values=list of values (list of numbers)
        host_host_population_contact_sweep_dic -- dictionary with
            keys=population IDs of origin and destination, separated by a colon
            ';' (Strings), values=list of values (list of numbers)
        host_vector_population_contact_sweep_dic -- dictionary with
            keys=population IDs of origin and destination, separated by a colon
            ';' (Strings), values=list of values (list of numbers)
        vector_host_population_contact_sweep_dic -- dictionary with
            keys=population IDs of origin and destination, separated by a colon
            ';' (Strings), values=list of values (list of numbers)
        replicates -- how many replicates to simulate (int >= 1)
        method -- algorithm to be used; default is approximated solver
            (can be either 'approximated' or 'exact')
        dt_leap -- time leap size used to simulate bursts; if None, set to
            minimum growth threshold time across all populations (number,
            default None)
        dt_thre -- time threshold below which bursts are used; if None, set to
            dt_leap (number, default None)
        host_sampling -- how many hosts to skip before saving one in a snapshot
            of the system state (saves all by default) (int >= 0, default 0)
        vector_sampling -- how many vectors to skip before saving one in a
            snapshot of the system state (saves all by default)
            (int >= 0, default 0)
        skip_uninfected -- whether to save only infected hosts/vectors and
            record the number of uninfected host/vectors instead (Boolean,
            default False)
        n_cores -- number of cores to parallelize file export across, if 0, all
            cores available are used (default 0; int >= 0)
        **kwargs -- additional arguents for joblib multiprocessing

        Returns:
        DataFrame with parameter combinations, list of Model objects with the
            final snapshots
        """

        if not n_cores:
            n_cores = jl.cpu_count()

        for p in host_population_size_sweep:
            param_sweep_dic['pop_size_host:'+p] = host_population_size_sweep[p]

        for p in vector_population_size_sweep:
            param_sweep_dic['pop_size_vector:'+p] = vector_population_size_sweep[p]

        for p in host_migration_sweep_dic:
            param_sweep_dic['migrate_host:'+p] = host_migration_sweep_dic[p]

        for p in vector_migration_sweep_dic:
            param_sweep_dic['migrate_vector:'+p] = vector_migration_sweep_dic[p]

        for p in host_host_population_contact_sweep_dic:
            param_sweep_dic['population_contact_host_host:'+p] \
                = host_host_population_contact_sweep_dic[p]

        for p in host_vector_population_contact_sweep_dic:
            param_sweep_dic['population_contact_host_vector:'+p] \
                = host_vector_population_contact_sweep_dic[p]

        for p in vector_host_population_contact_sweep_dic:
            param_sweep_dic['population_contact_vector_host:'+p] \
                = vector_host_population_contact_sweep_dic[p]

        if len(param_sweep_dic) == 0:
            raise ValueError(
                'param_sweep_dic, host_migration_sweep_dic, vector_migration_sweep_dic, host_host_population_contact_sweep_dic, host_vector_population_contact_sweep_dic, and vector_host_population_contact_sweep_dic cannot all be empty in runParamSweep()'
                )

        params = param_sweep_dic.keys()
        value_lists = [ param_sweep_dic[param] for param in params ]
        combinations = list( it.product( *value_lists ) ) * replicates

        param_df = pd.DataFrame(combinations)
        param_df.columns = params
        results = {}

        print('Starting parallel simulations...')

        def run(param_values):
            model = self.deepCopy()
            for i,param_name in enumerate(params):
                if ':' in param_name:
                    pops = param_name.split(':')[1].split(';')
                    if 'pop_size_host:' in param_name:
                        pop = cp.deepcopy( model.populations[pops[0]] )
                        add_hosts = param_values[i] - len(pop.hosts)
                        if add_hosts < 0:
                            raise ValueError(
                                'Value ' + str(param_values[i]) + ' assigned to ' + pops[0] + ' in host_population_size_sweep must be greater or equal to the population\'s original number of hosts.'
                                )
                        else:
                            pop.addHosts(add_hosts)
                            model.populations[pops[0]] = pop
                            pop.model = model

                    elif 'pop_size_vector:' in param_name:
                        pop = cp.deepcopy( model.populations[pops[0]] )
                        add_vectors = param_values[i] - len(pop.vectors)
                        if add_vectors < 0:
                            raise ValueError(
                                'Values ' + str(param_values[i]) + ' assigned to ' + pops[0] + ' in vector_population_size_sweep must be greater or equal to the population\'s original number of vectors.'
                                )
                        else:
                            pop.addVectors(add_vectors)
                            model.populations[pops[0]] = pop
                            pop.model = model

                    elif 'migrate_host:' in param_name:
                        new_pops = [
                            cp.deepcopy( model.populations[pops[0]] ),
                            cp.deepcopy( model.populations[pops[1]] )
                            ]
                        new_pops[0].model = model
                        new_pops[1].model = model
                        model.populations[pops[0]] = new_pops[0]
                        model.populations[pops[1]] = new_pops[1]
                        model.linkPopulationsHostMigration(
                            new_pops[0],new_pops[1],param_values[i]
                            )
                    elif 'migrate_vector:' in param_name:
                        new_pops = [
                            cp.deepcopy( model.populations[pops[0]] ),
                            cp.deepcopy( model.populations[pops[1]] )
                            ]
                        new_pops[0].model = model
                        new_pops[1].model = model
                        model.populations[pops[0]] = new_pops[0]
                        model.populations[pops[1]] = new_pops[1]
                        model.linkPopulationsVectorMigration(
                            pops[0],pops[1],param_values[i]
                            )
                    elif 'population_contact_host_host:' in param_name:
                        new_pops = [
                            cp.deepcopy( model.populations[pops[0]] ),
                            cp.deepcopy( model.populations[pops[1]] )
                            ]
                        new_pops[0].model = model
                        new_pops[1].model = model
                        model.populations[pops[0]] = new_pops[0]
                        model.populations[pops[1]] = new_pops[1]
                        model.linkPopulationsHostHostContact(
                            pops[0],pops[1],param_values[i]
                            )
                        model.linkPopulationsHostHostContact(
                            pops[1],pops[0],param_values[i]
                            )
                    elif 'population_contact_host_vector:' in param_name:
                        new_pops = [
                            cp.deepcopy( model.populations[pops[0]] ),
                            cp.deepcopy( model.populations[pops[1]] )
                            ]
                        new_pops[0].model = model
                        new_pops[1].model = model
                        model.populations[pops[0]] = new_pops[0]
                        model.populations[pops[1]] = new_pops[1]
                        model.linkPopulationsHostVectorContact(
                            pops[0],pops[1],param_values[i]
                            )
                        model.linkPopulationsHostVectorContact(
                            pops[1],pops[0],param_values[i]
                            )
                    elif 'population_contact_vector_host:' in param_name:
                        new_pops = [
                            cp.deepcopy( model.populations[pops[0]] ),
                            cp.deepcopy( model.populations[pops[1]] )
                            ]
                        new_pops[0].model = model
                        new_pops[1].model = model
                        model.populations[pops[0]] = new_pops[0]
                        model.populations[pops[1]] = new_pops[1]
                        model.linkPopulationsVectorHostContact(
                            pops[0],pops[1],param_values[i]
                            )
                        model.linkPopulationsVectorHostContact(
                            pops[1],pops[0],param_values[i]
                            )
                else:
                    setattr(model.setups[setup_id],param_name,param_values[i])

            for name,pop in model.populations.items():
                pop.setSetup( model.setups[pop.setup.id] )

            sim = Simulation(model)
            mod = sim.run(
                t0,tf,time_sampling=-1,method=method,
                host_sampling=host_sampling,vector_sampling=vector_sampling,
                skip_uninfected=skip_uninfected
                )[tf]
            mod.history = { tf:mod }
            return mod

        return (
            param_df,
            jl.Parallel(n_jobs=n_cores, verbose=10, **kwargs) (
                jl.delayed( run ) (param_values)
                    for param_values in combinations
                )
            )

    def copyState(self,host_sampling=0,vector_sampling=0,skip_uninfected=False):
        """Returns a slimmed-down representation of the current model state.

        Keyword arguments:
        host_sampling -- how many hosts to skip before saving one in a snapshot
            of the system state (saves all by default) (int >= 0, default 0)
        vector_sampling -- how many vectors to skip before saving one in a
            snapshot of the system state (saves all by default)
            (int >= 0, default 0)
        skip_uninfected -- whether to save only infected hosts/vectors and
            record the number of uninfected host/vectors instead (Boolean,
            default False)

        Returns:
        Model object with current population host and vector lists.
        """

        copy = Model()

        copy.populations = {
            id: p.copyState(host_sampling,vector_sampling,skip_uninfected)
            for id,p in self.populations.items()
            }

        return copy

    def deepCopy(self):
        """Returns a full copy of the current model with inner references.

        Returns:
        copied Model object
        """

        model = cp.deepcopy(self)
        for intervention in model.interventions:
            intervention.model = model
        for pop in model.populations:
            model.populations[pop].model = model
            for h in model.populations[pop].hosts:
                h.population = model.populations[pop]
            for v in model.populations[pop].vectors:
                v.population = model.populations[pop]

        return model


    ### Output and Plots: ###

    def saveToDataFrame(self,save_to_file,n_cores=0,**kwargs):
        """Save status of model to dataframe, write to file location given.

        Creates a pandas Dataframe in long format with the given model history,
        with one host or vector per simulation time in each row, and columns:
            Time - simulation time of entry
            Population - ID of this host/vector's population
            Organism - host/vector
            ID - ID of host/vector
            Pathogens - all genomes present in this host/vector separated by ;
            Protection - all genomes present in this host/vector separated by ;
            Alive - whether host/vector is alive at this time, True/False

        Arguments:
        save_to_file -- file path and name to save model data under (String)

        Keyword arguments:
        n_cores -- number of cores to parallelize file export across, if 0, all
            cores available are used (default 0; int >= 0)
        **kwargs -- additional arguents for joblib multiprocessing

        Returns:
        pandas dataframe with model history as described above
        """

        data = saveToDf(
            self.history,save_to_file,n_cores,**kwargs
            )

        return data

    def getPathogens(self, dat, save_to_file=""):
        """Create Dataframe with counts for all pathogen genomes in data.

        Returns sorted pandas Dataframe with counts for occurrences of all
        pathogen genomes in data passed.

        Arguments:
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        save_to_file -- file path and name to save model data under, no saving
            occurs if empty string (default ''; String)

        Returns:
        pandas dataframe with Series as described above
        """

        return getPathogens(dat, save_to_file=save_to_file)

    def getProtections(self, dat, save_to_file=""):
        """Create Dataframe with counts for all protection sequences in data.

        Returns sorted pandas Dataframe with counts for occurrences of all
        protection sequences in data passed.

        Arguments:
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        save_to_file -- file path and name to save model data under, no saving
            occurs if empty string (default ''; String)

        Returns:
        pandas dataframe with Series as described above
        """

        return getProtections(dat, save_to_file=save_to_file)

    def populationsPlot(
            self, file_name, data, compartment='Infected',
            hosts=True, vectors=False, num_top_populations=7,
            track_specific_populations=[], save_data_to_file="",
            x_label='Time', y_label='Hosts', figsize=(8, 4), dpi=200,
            palette=CB_PALETTE, stacked=False):
        """Create plot with aggregated totals per population across time.

        Creates a line or stacked line plot with dynamics of a compartment
        across populations in the model, with one line for each population.

        A host or vector is considered part of the recovered compartment
        if it has protection sequences of any kind and is not infected.

        Arguments:
        file_name -- file path, name, and extension to save plot under (String)
        data -- dataframe with model history as produced by saveToDf function
            (DataFrame)

        Keyword arguments:
        compartment -- subset of hosts/vectors to count totals of, can be either
            'Naive','Infected','Recovered', or 'Dead'
            (default 'Infected'; String)
        hosts -- whether to count hosts (default True, Boolean)
        vectors -- whether to count vectors (default False, Boolean)
        num_top_populations -- how many populations to count separately and
            include as columns, remainder will be counted under column "Other";
            if <0, includes all populations in model (default 7; int)
        track_specific_populations -- contains IDs of specific populations to
            have as a separate column if not part of the top num_top_populations
            populations (default empty list; list of Strings)
        save_data_to_file -- file path and name to save model plot data under,
            no saving occurs if empty string (default ''; String)
        x_label -- X axis title (default 'Time', String)
        y_label -- Y axis title (default 'Hosts', String)
        legend_title -- legend title (default 'Population', String)
        legend_values -- labels for each trace, if empty list, uses population
            IDs (default empty list, list of Strings)
        figsize -- dimensions of figure (default (8,4), array-like of two ints)
        dpi -- figure resolution (default 200, int)
        palette -- color palette to use for traces (default CB_PALETTE, list of
            color Strings)
        stacked -- whether to draw a regular line plot instead of a stacked one
            (default False, Boolean)

        Returns:
        axis object for plot with model population dynamics as described above
        """

        return populationsPlot(
            file_name, data, compartment=compartment, hosts=hosts,
            vectors=vectors, num_top_populations=num_top_populations,
            track_specific_populations=track_specific_populations,
            save_data_to_file=save_data_to_file,
            x_label=x_label, y_label=y_label, figsize=figsize, dpi=dpi,
            palette=palette, stacked=stacked
            )

    def compartmentPlot(
            self, file_name, data, populations=[], hosts=True, vectors=False,
            save_data_to_file="", x_label='Time', y_label='Hosts',
            figsize=(8, 4), dpi=200, palette=CB_PALETTE, stacked=False):
        """Create plot with number of naive,inf,rec,dead hosts/vectors vs. time.

        Creates a line or stacked line plot with dynamics of all compartments
        (naive, infected, recovered, dead) across selected populations in the
        model, with one line for each compartment.

        A host or vector is considered part of the recovered compartment
        if it has protection sequences of any kind and is not infected.

        Arguments:
        file_name -- file path, name, and extension to save plot under (String)
        data -- dataframe with model history as produced by saveToDf function
            (DataFrame)

        Keyword arguments:
        populations -- IDs of populations to include in analysis; if empty, uses
            all populations in model (default empty list; list of Strings)
        hosts -- whether to count hosts (default True, Boolean)
        vectors -- whether to count vectors (default False, Boolean)
        save_data_to_file -- file path and name to save model data under, no
            saving occurs if empty string (default ''; String)
        x_label -- X axis title (default 'Time', String)
        y_label -- Y axis title (default 'Hosts', String)
        legend_title -- legend title (default 'Population', String)
        legend_values -- labels for each trace, if empty list, uses population
            IDs (default empty list, list of Strings)
        figsize -- dimensions of figure (default (8,4), array-like of two ints)
        dpi -- figure resolution (default 200, int)
        palette -- color palette to use for traces (default CB_PALETTE, list of
            color Strings)
        stacked -- whether to draw a regular line plot instead of a stacked one
            (default False, Boolean)

        Returns:
        axis object for plot with model compartment dynamics as described above
        """

        return compartmentPlot(
            file_name, data, populations=populations, hosts=hosts,
            vectors=vectors, save_data_to_file=save_data_to_file,
            x_label=x_label, y_label=y_label, figsize=figsize, dpi=dpi,
            palette=palette, stacked=stacked
            )

    def compositionPlot(
            self, file_name, data, composition_dataframe=None, populations=[],
            type_of_composition='Pathogens', hosts=True, vectors=False,
            num_top_sequences=7, track_specific_sequences=[],
            save_data_to_file="", x_label='Time', y_label='Infections',
            figsize=(8, 4), dpi=200, palette=CB_PALETTE, stacked=True,
            remove_legend=False, genomic_positions=[],population_fraction=False,
            count_individuals_based_on_model=None,
            legend_title='Genotype', legend_values=[], **kwargs):
        """Create plot with counts for pathogen genomes or resistance vs. time.

        Creates a line or stacked line plot with dynamics of the pathogen
        strains or protection sequences across selected populations in the
        model, with one line for each pathogen genome or protection sequence
        being shown.

        Of note: sum of totals for all sequences in one time point does not
        necessarily equal the number of infected hosts and/or vectors, given
        multiple infections in the same host/vector are counted separately.

        Arguments:
        file_name -- file path, name, and extension to save plot under (String)
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        composition_dataframe -- output of compositionDf() if already computed
            (Pandas DataFrame, None by default)
        populations -- IDs of populations to include in analysis; if empty, uses
            all populations in model (default empty list; list of Strings)
        type_of_composition -- field of data to count totals of, can be either
            'Pathogens' or 'Protection' (default 'Pathogens'; String)
        hosts -- whether to count hosts (default True, Boolean)
        vectors -- whether to count vectors (default False, Boolean)
        num_top_sequences -- how many sequences to count separately and include
            as columns, remainder will be counted under column "Other"; if <0,
            includes all genomes in model (default 7; int)
        track_specific_sequences -- contains specific sequences to have
            as a separate column if not part of the top num_top_sequences
            sequences (default empty list; list of Strings)
        genomic_positions -- list in which each element is a list with loci
            positions to extract (e.g. genomic_positions=[ [0,3], [5,6] ]
            extracts positions 0, 1, 2, and 5 from each genome); if empty, takes
            full genomes (default empty list; list of lists of int)
        count_individuals_based_on_model -- Model object with populations and
            fitness functions used to evaluate the most fit pathogen genome in
            each host/vector in order to count only a single pathogen per
            host/vector, as opposed to all pathogens within each host/vector; if
            None, counts all pathogens (default None; None or Model)
        save_data_to_file -- file path and name to save model data under, no
            saving occurs if empty string (default ''; String)
        x_label -- X axis title (default 'Time', String)
        y_label -- Y axis title (default 'Hosts', String)
        legend_title -- legend title (default 'Population', String)
        legend_values -- labels for each trace, if empty list, uses population
            IDs (default empty list, list of Strings)
        figsize -- dimensions of figure (default (8,4), array-like of two ints)
        dpi -- figure resolution (default 200, int)
        palette -- color palette to use for traces (default CB_PALETTE, list of
            color Strings)
        stacked -- whether to draw a regular line plot instead of a stacked one
            (default False, Boolean).
        remove_legend -- whether to print the sequences on the figure legend
            instead of printing them on a separate csv file
            (default True; Boolean)
        **kwargs -- additional arguents for joblib multiprocessing

        Returns:
        axis object for plot with model sequence composition dynamics as
            described
        """

        return compositionPlot(
            file_name, data,
            composition_dataframe=composition_dataframe,populations=populations,
            type_of_composition=type_of_composition, hosts=hosts,
            vectors=vectors, num_top_sequences=num_top_sequences,
            track_specific_sequences=track_specific_sequences,
            save_data_to_file=save_data_to_file,
            x_label=x_label, y_label=y_label, figsize=figsize, dpi=dpi,
            palette=palette, stacked=stacked, remove_legend=remove_legend,
            genomic_positions=genomic_positions,
            count_individuals_based_on_model=count_individuals_based_on_model,
            population_fraction=population_fraction, legend_title=legend_title,
            legend_values=legend_values,
            **kwargs
            )

    def clustermap(
            self,
            file_name, data, num_top_sequences=-1, track_specific_sequences=[],
            seq_names=[], n_cores=0, method='weighted', metric='euclidean',
            save_data_to_file="", legend_title='Distance', legend_values=[],
            figsize=(10,10), dpi=200, color_map=DEF_CMAP):
        """Create a heatmap and dendrogram for pathogen genomes in data passed.

        Arguments:
        file_name -- file path, name, and extension to save plot under (String)
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        num_top_sequences -- how many sequences to include in matrix; if <0,
            includes all genomes in data passed (default -1; int)
        track_specific_sequences -- contains specific sequences to include in
            matrix if not part of the top num_top_sequences sequences (default
            empty list; list of Strings)
        seq_names -- list with names to be used for sequence labels in matrix
            must be of same length as number of sequences to be displayed; if
            empty, uses sequences themselves (default empty list; list of
            Strings)
        n_cores -- number of cores to parallelize distance compute across, if 0,
            all cores available are used (default 0; int >= 0)
        method -- clustering algorithm to use with seaborn clustermap (default
            'weighted'; String)
        metric -- distance metric to use with seaborn clustermap (default
            'euclidean'; String)
        save_data_to_file -- file path and name to save model data under, no
            saving occurs if empty string (default ''; String)
        legend_title -- legend title (default 'Distance', String)
        figsize -- dimensions of figure (default (8,4), array-like of two ints)
        dpi -- figure resolution (default 200, int)
        color_map -- color map to use for traces (default DEF_CMAP, cmap object)

        Returns:
        figure object for plot with heatmap and dendrogram as described
        """

        return clustermap(
                file_name, data, num_top_sequences=num_top_sequences,
                track_specific_sequences=track_specific_sequences,
                seq_names=seq_names, n_cores=n_cores, method=method,
                metric=metric, save_data_to_file=save_data_to_file,
                legend_title=legend_title, legend_values=legend_values,
                figsize=figsize, dpi=dpi, color_map=color_map
                )

    def pathogenDistanceHistory(
        self,
        data, samples=-1, num_top_sequences=-1, track_specific_sequences=[],
        seq_names=[], n_cores=0, save_to_file=''):
        """Create DataFrame with pairwise Hamming distances for pathogen
        sequences in data.

        DataFrame has indexes and columns named according to genomes or argument
        seq_names, if passed. Distance is measured as percent Hamming distance
        from an optimal genome sequence.

        Arguments:
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        samples -- how many timepoints to uniformly sample from the total
            timecourse; if <0, takes all timepoints (default 1; int)
        num_top_sequences -- how many sequences to include in matrix; if <0,
            includes all genomes in data passed (default -1; int)
        track_specific_sequences -- contains specific sequences to include in
            matrix if not part of the top num_top_sequences sequences (default
            empty list; list of Strings)
        seq_names -- list with names to be used for sequence labels in matrix
            must be of same length as number of sequences to be displayed; if
            empty, uses sequences themselves
            (default empty list; list of Strings)
        n_cores -- number of cores to parallelize distance compute across, if 0,
            all cores available are used (default 0; int >= 0)
        save_to_file -- file path and name to save model data under, no saving
            occurs if empty string (default ''; String)

        Returns:
        pandas dataframe with distance matrix as described above
        """
        return getPathogenDistanceHistoryDf(data,
            samples=samples, num_top_sequences=num_top_sequences,
            track_specific_sequences=track_specific_sequences,
            seq_names=seq_names, n_cores=n_cores, save_to_file=save_to_file)

    def getGenomeTimes(
        self,
        data, samples=-1, num_top_sequences=-1, track_specific_sequences=[],
        seq_names=[], n_cores=0, save_to_file=''):
        """Create DataFrame with times genomes first appeared during simulation.

        Arguments:
        data -- dataframe with model history as produced by saveToDf function

        Keyword arguments:
        samples -- how many timepoints to uniformly sample from the total
            timecourse; if <0, takes all timepoints (default 1; int)
        save_to_file -- file path and name to save model data under, no saving
            occurs if empty string (default ''; String)
        n_cores -- number of cores to parallelize across, if 0, all cores
            available are used (default 0; int)

        Returns:
        pandas dataframe with genomes and times as described above
        """
        return getGenomeTimesDf(data,
            samples=samples, num_top_sequences=num_top_sequences,
            track_specific_sequences=track_specific_sequences,
            seq_names=seq_names, n_cores=n_cores, save_to_file=save_to_file)


    def getCompositionData(
            self, data=None, populations=[], type_of_composition='Pathogens',
            hosts=True, vectors=False, num_top_sequences=-1,
            track_specific_sequences=[], genomic_positions=[],
            count_individuals_based_on_model=None, save_data_to_file="",
            n_cores=0, **kwargs):
        """Create dataframe with counts for pathogen genomes or resistance.

        Creates a pandas Dataframe with dynamics of the pathogen strains or
        protection sequences across selected populations in the model,
        with one time point in each row and columns for pathogen genomes or
        protection sequences.

        Of note: sum of totals for all sequences in one time point does not
        necessarily equal the number of infected hosts and/or vectors, given
        multiple infections in the same host/vector are counted separately.

        Keyword arguments:
        data -- dataframe with model history as produced by saveToDf function;
            if None, computes this dataframe and saves it under
            'raw_data_'+save_data_to_file (DataFrame, default None)
        populations -- IDs of populations to include in analysis; if empty, uses
            all populations in model (default empty list; list of Strings)
        type_of_composition -- field of data to count totals of, can be either
            'Pathogens' or 'Protection' (default 'Pathogens'; String)
        hosts -- whether to count hosts (default True, Boolean)
        vectors -- whether to count vectors (default False, Boolean)
        num_top_sequences -- how many sequences to count separately and include
            as columns, remainder will be counted under column "Other"; if <0,
            includes all genomes in model (default -1; int)
        track_specific_sequences -- contains specific sequences to have
            as a separate column if not part of the top num_top_sequences
            sequences (default empty list; list of Strings)
        genomic_positions -- list in which each element is a list with loci
            positions to extract (e.g. genomic_positions=[ [0,3], [5,6] ]
            extracts positions 0, 1, 2, and 5 from each genome); if empty, takes
            full genomes(default empty list; list of lists of int)
        count_individuals_based_on_model -- Model object with populations and
            fitness functions used to evaluate the most fit pathogen genome in
            each host/vector in order to count only a single pathogen per
            host/vector, asopposed to all pathogens within each host/vector; if
            None, counts all pathogens (default None; None or Model)
        save_data_to_file -- file path and name to save model data under, no
            saving occurs if empty string (default ''; String)
        n_cores -- number of cores to parallelize processing across, if 0, all
            cores available are used (default 0; int)
        **kwargs -- additional arguents for joblib multiprocessing

        Returns:
        pandas dataframe with model sequence composition dynamics as described
            above
        """

        if data is None:
            data = saveToDf(
                self.history,'raw_data_'+save_to_file,n_cores,verbose=verbose,
                **kwargs
                )

        return compositionDf(
            data, populations=populations,
            type_of_composition=type_of_composition,
            hosts=hosts, vectors=vectors, num_top_sequences=num_top_sequences,
            track_specific_sequences=track_specific_sequences,
            genomic_positions=genomic_positions,
            count_individuals_based_on_model=count_individuals_based_on_model,
            save_to_file=save_data_to_file, n_cores=n_cores, **kwargs
            )

    ### Model interventions: ###

    def newPopulation(self, id, setup_id, num_hosts=0, num_vectors=0):
        """Create a new Population object with setup parameters.

        If population ID is already in use, appends _2 to it

        Arguments:
        id -- unique identifier for this population in the model (String)
        setup_id -- setup object with parameters for this population (Setup)

        Keyword arguments:
        num_hosts -- number of hosts to initialize population with (default 100;
            int >= 0)
        num_vectors -- number of hosts to initialize population with (default
            100; int >= 0)
        """

        if id in self.populations.keys():
            id = id+'_2'

        self.populations[id] = Population(
            self, id, self.setups[setup_id], num_hosts, num_vectors
            )

        for p in self.populations:
            self.populations[id].setHostMigrationNeighbor(self.populations[p],0)
            self.populations[id].setVectorMigrationNeighbor(
                self.populations[p],0
                )
            self.populations[id].setHostHostPopulationContactNeighbor(
                self.populations[p],0
                )
            self.populations[id].setVectorHostPopulationContactNeighbor(
                self.populations[p],0
                )
            self.populations[id].setHostVectorPopulationContactNeighbor(
                self.populations[p],0
                )

            self.populations[p].setHostMigrationNeighbor(
                self.populations[id],0
                )
            self.populations[p].setVectorMigrationNeighbor(
                self.populations[id],0
                )
            self.populations[p].setHostHostPopulationContactNeighbor(
                self.populations[id],0
                )
            self.populations[p].setVectorHostPopulationContactNeighbor(
                self.populations[id],0
                )
            self.populations[p].setHostVectorPopulationContactNeighbor(
                self.populations[id],0
                )

    def linkPopulationsHostMigration(self, pop1_id, pop2_id, rate):
        """Set host migration rate from one population towards another.

        Arguments:
        pop1_id -- origin population for which migration rate will be specified
            (String)
        pop1_id -- destination population for which migration rate will be
            specified (String)
        rate -- migration rate from one population to the neighbor; evts/time
            (number >= 0)
        """

        self.populations[pop1_id].setHostMigrationNeighbor(
            self.populations[pop2_id], rate
            )

    def linkPopulationsVectorMigration(self, pop1_id, pop2_id, rate):
        """Set vector migration rate from one population towards another.

        Arguments:
        pop1_id -- origin population for which migration rate will be specified
            (String)
        pop1_id -- destination population for which migration rate will be
            specified (String)
        rate -- migration rate from one population to the neighbor; evts/time
            (number >= 0)
        """

        self.populations[pop1_id].setVectorMigrationNeighbor(
            self.populations[pop2_id], rate
            )

    def linkPopulationsHostHostContact(self, pop1_id, pop2_id, rate):
        """Set host-host contact rate from one population towards another.

        Arguments:
        pop1_id -- origin population for which inter-population contact rate
            will be specified (String)
        pop1_id -- destination population for which inter-population contact
            rate will be specified (String)
        rate -- inter-population contact rate from one population to the
            neighbor; evts/time (number >= 0)
        """

        self.populations[pop1_id].setHostHostPopulationContactNeighbor(
            self.populations[pop2_id], rate
            )

    def linkPopulationsHostVectorContact(self, pop1_id, pop2_id, rate):
        """Set host-vector contact rate from one population towards another.

        Arguments:
        pop1_id -- origin population for which inter-population contact rate
            will be specified (String)
        pop1_id -- destination population for which inter-population contact
            rate will be specified (String)
        rate -- inter-population contact rate from one population to the
            neighbor; evts/time (number >= 0)
        """

        self.populations[pop1_id].setHostVectorPopulationContactNeighbor(
            self.populations[pop2_id], rate
            )

    def linkPopulationsVectorHostContact(self, pop1_id, pop2_id, rate):
        """Set vector-host contact rate from one population towards another.

        Arguments:
        pop1_id -- origin population for which inter-population contact rate
            will be specified (String)
        pop1_id -- destination population for which inter-population contact
            rate will be specified (String)
        rate -- inter-population contact rate from one population to the
            neighbor; evts/time (number >= 0)
        """

        self.populations[pop1_id].setVectorHostPopulationContactNeighbor(
            self.populations[pop2_id], rate
            )

    def createInterconnectedPopulations(
            self, num_populations, id_prefix, setup_id,
            host_migration_rate=0, vector_migration_rate=0,
            host_host_contact_rate=0,
            host_vector_contact_rate=0, vector_host_contact_rate=0,
            num_hosts=100, num_vectors=100):
        """Create new populations, link all of them to each other.

        All populations in this cluster are linked with the same migration rate,
        starting number of hosts and vectors, and setup parameters. Their IDs
        are numbered onto prefix given as 'id_prefix_0', 'id_prefix_1',
        'id_prefix_2', etc.

        Arguments:
        num_populations -- number of populations to be created (int)
        id_prefix -- prefix for IDs to be used for this population in the model,
            (String)
        setup_id -- setup object with parameters for all populations (Setup)

        Keyword arguments:
        host_migration_rate -- host migration rate between populations;
            evts/time (default 0; number >= 0)
        vector_migration_rate -- vector migration rate between populations;
            evts/time (default 0; number >= 0)
        host_host_contact_rate -- host-host inter-population contact rate
            between populations; evts/time (default 0; number >= 0)
        host_vector_contact_rate -- host-vector inter-population contact rate
            between populations; evts/time (default 0; number >= 0)
        vector_host_contact_rate -- vector-host inter-population contact rate
            between populations; evts/time (default 0; number >= 0)
        num_hosts -- number of hosts to initialize population with (default 100;
            int)
        num_vectors -- number of hosts to initialize population with (default
            100; int)
        """

        new_pops = [
            Population(
                self, str(id_prefix) + str(i), self.setups[setup_id],
                num_hosts, num_vectors
                ) for i in range(num_populations)
            ]
        new_pop_ids = []
        for pop in new_pops:
            if pop.id in self.populations.keys():
                pop.id = pop.id+'_2'

            self.populations[pop.id] = pop
            new_pop_ids.append(pop.id)

            for p in self.populations:
                pop.setHostMigrationNeighbor(self.populations[p],0)
                pop.setVectorMigrationNeighbor(self.populations[p],0)
                pop.setHostHostPopulationContactNeighbor(self.populations[p],0)
                pop.setHostVectorPopulationContactNeighbor(self.populations[p],0)
                pop.setVectorHostPopulationContactNeighbor(self.populations[p],0)

                self.populations[p].setHostMigrationNeighbor(pop,0)
                self.populations[p].setVectorMigrationNeighbor(pop,0)
                self.populations[p].setHostHostPopulationContactNeighbor(pop,0)
                self.populations[p].setHostVectorPopulationContactNeighbor(pop,0)
                self.populations[p].setVectorHostPopulationContactNeighbor(pop,0)

        for p1_id in new_pop_ids:
            for p2_id in new_pop_ids:
                self.linkPopulationsHostMigration(
                    p1_id,p2_id,host_migration_rate
                    )
                self.linkPopulationsVectorMigration(
                    p1_id,p2_id,vector_migration_rate
                    )
                self.linkPopulationsHostHostContact(
                    p1_id,p2_id,host_host_contact_rate
                    )
                self.linkPopulationsHostVectorContact(
                    p1_id,p2_id,host_vector_contact_rate
                    )
                self.linkPopulationsVectorHostContact(
                    p1_id,p2_id,vector_host_contact_rate
                    )

    def newHostGroup(self, pop_id, group_id, hosts=-1, type='any'):
        """Return a list of random hosts in population.

        Arguments:
        pop_id -- ID of population to be sampled from (String)
        group_id -- ID to name group with (String)

        Keyword arguments:
        hosts -- number of hosts to be sampled randomly: if <0, samples from
            whole population; if <1, takes that fraction of population; if >=1,
            samples that integer number of hosts (default -1, number)
        type -- whether to sample healthy hosts only, infected hosts only, or
            any hosts (default 'any'; String = {'healthy', 'infected', 'any'})

        Returns:
        list containing sampled hosts
        """

        self.groups[group_id] = self.populations[pop_id].newHostGroup(
            hosts, type
            )

    def newVectorGroup(self, pop_id, group_id, vectors=-1, type='any'):
        """Return a list of random vectors in population.

        Arguments:
        pop_id -- ID of population to be sampled from (String)
        group_id -- ID to name group with (String)

        Keyword arguments:
        vectors -- number of vectors to be sampled randomly: if <0, samples from
            whole population; if <1, takes that fraction of population; if >=1,
            samples that integer number of vectors (default -1, number)
        type -- whether to sample healthy vectors only, infected vectors
            only, or any vectors (default 'any'; String = {'healthy',
            'infected', 'any'})

        Returns:
        list containing sampled vectors
        """

        self.groups[group_id] = self.populations[pop_id].newVectorGroup(
            vectors, type
            )

    def addHosts(self, pop_id, num_hosts):
        """Add a number of healthy hosts to population, return list with them.

        Arguments:
        pop_id -- ID of population to be modified (String)
        num_hosts -- number of hosts to be added (int)

        Returns:
        list containing new hosts
        """

        self.populations[pop_id].addHosts(num_hosts)

    def addVectors(self, pop_id, num_vectors):
        """Add a number of healthy vectors to population, return list with them.

        Arguments:
        pop_id -- ID of population to be modified (String)
        num_vectors -- number of vectors to be added (int)

        Returns:
        list containing new vectors
        """

        self.populations[pop_id].addVectors(num_vectors)

    def removeHosts(self, pop_id, num_hosts_or_list):
        """Remove a number of specified or random hosts from population.

        Arguments:
        pop_id -- ID of population to be modified (String)
        num_hosts_or_list -- number of hosts to be sampled randomly for removal
            or list of hosts to be removed, must be hosts in this population
            (int or list of Hosts)
        """

        self.populations[pop_id].removeHosts(num_hosts_or_list)

    def removeVectors(self, pop_id, num_vectors_or_list):
        """Remove a number of specified or random vectors from population.

        Arguments:
        pop_id -- ID of population to be modified (String)
        num_vectors_or_list -- number of vectors to be sampled randomly for
            removal or list of vectors to be removed, must be vectors in this
            population (int or list of Vectors)
        """

        self.populations[pop_id].removeVectors(num_vectors_or_list)

    def addPathogensToHosts(self, pop_id, genomes_numbers, group_id=""):
        """Add specified pathogens to random hosts, optionally from a list.

        Arguments:
        pop_id -- ID of population to be modified (String)
        genomes_numbers -- dictionary containing pathogen genomes to add as keys
            and number of hosts each one will be added to as values (dict with
            keys=Strings, values=int)

        Keyword arguments:
        group_id -- ID of specific hosts to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            hosts = self.populations[pop_id].hosts
        else:
            hosts = self.groups[group_id]

        self.populations[pop_id].addPathogensToHosts(genomes_numbers,hosts)

    def addPathogensToVectors(self, pop_id, genomes_numbers, group_id=""):
        """Add specified pathogens to random vectors, optionally from a list.

        Arguments:
        pop_id -- ID of population to be modified (String)
        genomes_numbers -- dictionary containing pathogen genomes to add as keys
            and number of vectors each one will be added to as values (dict with
            keys=Strings, values=int)

        Keyword arguments:
        group_id -- ID of specific vectors to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            vectors = self.populations[pop_id].vectors
        else:
            vectors = self.groups[group_id]

        self.populations[pop_id].addPathogensToVectors(genomes_numbers,vectors)

    def treatHosts(self, pop_id, frac_hosts, resistance_seqs, group_id=""):
        """Treat random fraction of infected hosts against some infection.

        Removes all infections with genotypes susceptible to given treatment.
        Pathogens are removed if they are missing at least one of the sequences
        in resistance_seqs from their genome. Removes this organism from
        population infected list and adds to healthy list if appropriate.

        Arguments:
        pop_id -- ID of population to be modified (String)
        frac_hosts -- fraction of hosts considered to be randomly selected
            (number between 0 and 1)
        resistance_seqs -- contains sequences required for treatment resistance
            (list of Strings)

        Keyword arguments:
        group_id -- ID of specific hosts to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            hosts = self.populations[pop_id].hosts
        else:
            hosts = self.groups[group_id]

        self.populations[pop_id].treatHosts(frac_hosts,resistance_seqs,hosts)

    def treatVectors(self, pop_id, frac_vectors, resistance_seqs, group_id=""):
        """Treat random fraction of infected vectors agains some infection.

        Removes all infections with genotypes susceptible to given treatment.
        Pathogens are removed if they are missing at least one of the sequences
        in resistance_seqs from their genome. Removes this organism from
        population infected list and adds to healthy list if appropriate.

        Arguments:
        pop_id -- ID of population to be modified (String)
        frac_vectors -- fraction of vectors considered to be randomly selected
            (number between 0 and 1)
        resistance_seqs -- contains sequences required for treatment resistance
            (list of Strings)

        Keyword arguments:
        group_id -- ID of specific vectors to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            vectors = self.populations[pop_id].vectors
        else:
            vectors = self.groups[group_id]

        self.populations[pop_id].treatVectors(
            frac_vectors,resistance_seqs,vectors
            )

    def protectHosts(
            self, pop_id, frac_hosts, protection_sequence, group_id=""):
        """Protect a random fraction of infected hosts against some infection.

        Adds protection sequence specified to a random fraction of the hosts
        specified. Does not cure them if they are already infected.

        Arguments:
        pop_id -- ID of population to be modified (String)
        frac_hosts -- fraction of hosts considered to be randomly selected
            (number between 0 and 1)
        protection_sequence -- sequence against which to protect (String)

        Keyword arguments:
        group_id -- ID of specific hosts to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            hosts = self.populations[pop_id].hosts
        else:
            hosts = self.groups[group_id]

        self.populations[pop_id].protectHosts(
            frac_hosts,protection_sequence,hosts
            )

    def protectVectors(
            self, pop_id, frac_vectors, protection_sequence, group_id=""):
        """Protect a random fraction of infected vectors against some infection.

        Adds protection sequence specified to a random fraction of the vectors
        specified. Does not cure them if they are already infected.

        Arguments:
        pop_id -- ID of population to be modified (String)
        frac_vectors -- fraction of vectors considered to be randomly selected
            (number between 0 and 1)
        protection_sequence -- sequence against which to protect (String)

        Keyword arguments:
        group_id -- ID of specific vectors to sample from, if empty, samples
            from whole population (default empty String; empty)
        """

        if group_id == "":
            vectors = self.populations[pop_id].vectors
        else:
            vectors = self.groups[group_id]

        self.populations[pop_id].protectVectors(
            frac_vectors,protection_sequence,vectors
            )

    def wipeProtectionHosts(self, pop_id, group_id=""):
        """Removes all protection sequences from hosts.

        Arguments:
        pop_id -- ID of population to be modified (String)

        Keyword arguments:
        group_id -- ID of specific hosts to sample from, if empty, samples from
            whole from whole population (default empty String; String)
        """

        if group_id == "":
            hosts = self.populations[pop_id].hosts
        else:
            hosts = self.groups[group_id]

        self.populations[pop_id].wipeProtectionHosts(hosts)

    def wipeProtectionVectors(self, pop_id, group_id=""):
        """Removes all protection sequences from vectors.

        Arguments:
        pop_id -- ID of population to be modified (String)

        Keyword arguments:
        group_id -- ID of specific vectors to sample from, if empty, samples
            from whole population (default empty String; String)
        """

        if group_id == "":
            vectors = self.populations[pop_id].vectors
        else:
            vectors = self.groups[group_id]

        self.populations[pop_id].wipeProtectionVectors(vectors)

    ### Modify population parameters: ###

    def setSetup(
            self, pop_id, setup_id,
            update_coefficients_hosts=True, update_coefficients_vectors=True):
        """Assign parameters stored in Setup object to this population.

        Arguments:
        pop_id -- ID of population to be modified (String)
        setup_id -- ID of setup to be assigned (String)
        update_coefficients_hosts -- whether to recalculate all host
            coefficients (Boolean)
        update_coefficients_vectors -- whether to recalculate all vector
            coefficients (Boolean)
        """

        self.populations[pop_id].setSetup(
            self.setups[setup_id],
            update_coefficients_hosts=update_coefficients_hosts,
            update_coefficients_vectors=update_coefficients_vectors
            )

    ### Utility: ###

    def customModelFunction(self, function):
        """Returns output of given function, passing this model as a parameter.

        Arguments:
        function -- function to be evaluated; must take a Model object as the
                    only parameter (function)

        Returns:
        Output of function passed as parameter
        """

        return function(self)

    ### Preset fitness functions: ###

    @staticmethod
    def peakLandscape(genome, peak_genome, min_value):
        """Return genome phenotype by decreasing with distance from optimal seq.

        A purifying selection fitness function based on exponential decay of
        fitness as genomes move away from the optimal sequence. Distance is
        measured as percent Hamming distance from an optimal genome sequence.

        Arguments:
        genome -- the genome to be evaluated (String)
        peak_genome -- the genome sequence to measure distance against, has
            value of 1 (String)
        min_value -- minimum value at maximum distance from optimal
            genome (number 0-1)

        Return:
        value of genome (number)
        """

        distance = td.hamming(genome, peak_genome) / len(genome)
        value = np.exp( np.log( min_value ) * distance )

        return value

    @staticmethod
    def roundPeakLandscape(genome, peak_genome, max_value, floor=1e-6):
        """Return genome phenotype by decreasing with distance from optimal seq.

        A purifying selection fitness function based on exponential decay of
        fitness as genomes move away from the optimal sequence. Distance is
        measured as percent Hamming distance from an optimal genome sequence.

        Arguments:
        genome -- the genome to be evaluated (String)
        peak_genome -- the genome sequence to measure distance against, has
            value of 1 (String)
        min_value -- minimum value at maximum distance from optimal
            genome (number 0-1)

        Return:
        value of genome (number)
        """

        distance = td.hamming(genome, peak_genome) / len(genome)
        value = max( 1 - np.exp( np.log( 1-max_value ) * ( 1-distance ) ),floor)

        return value

    @staticmethod
    def valleyLandscape(genome, valley_genome, min_value):
        """Return genome phenotype by increasing with distance from worst seq.

        A disruptive selection fitness function based on exponential decay of
        fitness as genomes move closer to the worst possible sequence. Distance
        is measured as percent Hamming distance from the worst possible genome
        sequence.

        Arguments:
        genome -- the genome to be evaluated (String)
        valley_genome -- the genome sequence to measure distance against, has
            value of min_value (String)
        min_value -- fitness value of worst possible genome (number 0-1)

        Return:
        value of genome (number)
        """

        distance = td.hamming(genome, valley_genome) / len(genome)
        value = np.exp( np.log( min_value ) * ( 1 - distance ) )

        return value
