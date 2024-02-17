from mpi4py import MPI
from copy import deepcopy
import numpy as np
from math import floor, log, exp
from itertools import groupby
from .tmatrix import make_dumb_tmatrix, make_tmatrix_by_condition
from time import time
from . import metropolis
from .make_regr import make_regr
from susmost.savexyz import save_lattice_as_xyz
from susmost.sitestate import SPMI_db
import types
from collections import namedtuple
from scipy.spatial import cKDTree
from scipy.interpolate import interp1d


def param_idx(self, param_name):
	if param_name == 'energy':
		return -2
	return self.param_names.index(param_name)

def means(self, param_name):
	pidx = self.param_idx(param_name)
	return np.mean(self.full_params_log[:,:,pidx], axis=1)

def save_as_xyz(self, fn, comment='', multiplier = [1,1,1], mulmul=0.0):
	return self.lattice.save_as_xyz(fn, comment, multiplier, mulmul)


setattr(metropolis.Metropolis, "param_idx", param_idx)
setattr(metropolis.Metropolis, "means", means)
setattr(metropolis.Metropolis, "save_as_xyz", save_as_xyz)

"""
m.params_log:

0)	additive_params[0] / lattice.cells_count
1)	additive_params[1] / lattice.cells_count
........
-8)	in-site avgE / lattice.cells_count
-7)	in-site entropy / lattice.cells_count
-6)	in-site min_E / lattice.cells_count
-5)	in-site free_E / lattice.cells_count
-4)	acceptance rate
-3)	curE.internal / lattice.cells_count
-2)	curE.sum() / lattice.cells_count
-1)	T_idx
"""

def make_additive_params(states, param_names):
	return [[[props[pname].value for pname in param_names] for _,props in s.EP_list()] for s in states]
	
class Lattice:
	"""
		python -c 'import numpy as np; from susmost import mc, load_lattice_task; lt = load_lattice_task("tmp_00"); lt.set_ads_energy("atop-triang", -1.); m = mc.make_metropolis(lt, 10, [10.], 1.); mc.run(m, 10); print(m.cells, lt.states[0].state_type.__dict__);  l = mc.Lattice(metropolis=m); print(l.calc_fp()); print (l.calc_lateral_energy_per_site()), print (m.curE.internal); print (lt.site_state_types);  print ("PPP",l.calc_property_per_site("ads_energy")) '
	"""
	def __init__(self, lattice_task=None, lattice_size=None, metropolis=None):
		if lattice_task is None:
			assert lattice_size is None
			assert metropolis is not None
			
			self.lattice_task = metropolis.lattice_task
			self.regr = metropolis.regr
			self.regr_array = metropolis.regr_array
			self.cells = metropolis.cells
		else:
			self.lattice_task = lattice_task
			self.regr = make_regr(lattice_size, lattice_task)
			self.regr_array = self.regr.as_nparray(lattice_task.edges_count) # fill regr_array from regr
			self.cells = np.full(len(self.regr), lattice_task.zero_coverage_state_index, dtype=int)	# fill by empty_state_index

	def calc_fp(self):
		ei = np.arange(self.lattice_task.IM_int.shape[1], dtype=int) + 1
		max_sample_idx = np.max(self.lattice_task.IM_int)
		fp_state_types = np.zeros(len(self.lattice_task.site_state_types))
		fp_list = []
		for i,si in enumerate(self.cells):
			i_sst_idx = self.lattice_task.states[si].state_type.props['idx'].value
			fp_state_types[i_sst_idx] += 1
			j = self.regr_array[i, ei]
			sj = self.cells[j]
			samples = self.lattice_task.IM_int[si, ei-1, sj]
			fp = np.bincount(samples, minlength = max_sample_idx + 1)[1:] # skip 0-th sample as non-representative
			fp_list += [fp]
			#print (i, fp)
		fp_list = np.array(fp_list)
		fp_mean = fp_list.mean(axis=0)
		fp_sigma = fp_list.std(axis=0)
		fp_corr = np.corrcoef(fp_list, rowvar = False)
		fp_state_types /= len(self.cells)

		return fp_state_types, fp_mean, fp_sigma, fp_corr
	
	def calc_lateral_energy_per_site(self, fp_means=None):
		if fp_means is None:
			_, fp_means, _, _ = self.calc_fp()
		sample_energies = self.lattice_task.sample_energies[1:len(fp_means) + 1] # skip 0-th sample as it is allways zero energy
		return np.dot(fp_means,  np.nan_to_num(sample_energies))

	def calc_property_per_site(self, property_name, fp_state_types=None):
		if fp_state_types is None:
			fp_state_types, _, _, _ = self.calc_fp()
		prop_values =  [sst.props[property_name].value for sst in self.lattice_task.site_state_types]
		return np.dot(fp_state_types, prop_values)
		
	def save_cells(self, fn):
		with open(fn, 'w') as f:
			f.write("{}\n\n".format(len(self.cells)))
			for i in range(len(self.cells)):
				state_idx = self.cells[i]
				state_type = self.lattice_task.states[state_idx].state_type
				s = "{}\t{}\t{}\t{}\t{}\n".format(state_type.props['name'].value, state_idx, *self.regr[i].coords)
				f.write(s)
	
	def load_cells(self, fn):
		with open(fn, 'r') as f:
			n = int(next(f).strip())
			next(f)
			data = [[s for s in l.split()[1:]] for l in f]
			loaded_cell_state_indices = [int(row[0]) for row in data ]
			loaded_cell_coords = [[float(x) for x in row[1:]] for row in data ]
		
		loaded_tree = cKDTree(loaded_cell_coords)
		
		self_coords = [self.regr[i].coords for i in range(len(self.cells))]
		dd, loaded_ii = loaded_tree.query(self_coords)
		for self_i, (d, loaded_i) in enumerate(zip(dd, loaded_ii)):
			#print ("T", d, i)
			if d < 1e-3:
				self.cells[self_i] = loaded_cell_state_indices[loaded_i]
			else:
				print ("Nearest point is too far: ", (self_i, d, loaded_i), "(self_i, d, loaded_i)")

	def save_as_xyz(self, fn, comment='', multiplier = [1,1,1], mulmul=0.0):
		return save_lattice_as_xyz(fn, self, comment, multiplier, mulmul)
		
	
def make_metropolis(lat_task, supercell, T, k_B, param_names=None, precoverage = None, seed=None, pbc_flags=[True, True, False]):
	"""
		Create Metropolis object for specified LatticeTask and ReGraph objects
		
		Parameters:
			:lat_task: LatticeTask object
			:supercell: size of the lattice. See :func:`susmost.cell.universal_cell_size` for possible formats
			:T: list of temperatures in Kalvin units for replica exchange (*aka* parallel tempering), number of temperatures must be equal to number of MPI processes
			:k_B: Boltzmann constant, used as energy scale parameter
			:param_names: list of names of states properties that will be sampled in Metropolis iterations as simulaion parameters; default value - ['coverage']
			:precoverage: index of the state that will be used for initialization of the lattice, by default the state with zero ``coverage`` parameter is used
			:seed: random number generator for Metropolis simulaion
			:pbc_flags: list or tuple of three boolean flags, that enables/disables Periodic Boundary Conditions along each axis; default value - ``[True, True, False]``
		
		Returns:
			Metropolis object
	"""
	
	regr = make_regr(supercell, lat_task, pbc_flags=pbc_flags)

	# key constants:
	cells_count	=	len(regr)
	edges_count	=	lat_task.edges_count
	lc_count 	= 	lat_task.states_count
	#----------------------------------
	try:
		T_list = [t for t in T]
	except TypeError:
		T_list = [T]
	#----------------------------------
	if param_names is None:
		param_names = sorted(list(SPMI_db.keys() - set(['name', 'xyz_mark', 'ads_energy', 'idx'])))
	#----------------------------------
	if seed is None:
		seed = int(time())
	#----------------------------------
	if precoverage is None:
		precoverage = lat_task.zero_coverage_state_index
	
	precov_state_index = int(precoverage)
	cells = np.full(cells_count, precov_state_index, dtype=int)	# fill by empty_state_index

	#----------------------------------

	
	allowed_cells = np.full( (cells_count,lc_count), True, dtype=bool)	# all allowed
	transitions = make_dumb_tmatrix(lat_task.states) # any to any allowed
	internal_energies = [[E for E,_ in s.EP_list()] for s in lat_task.states]	# from adsorption energies, s.E - is a  list of
	lattice_graph=regr.as_nparray(edges_count) # fill lattice_graph from regr
	interaction = lat_task.IM.asarray()  # fill interaction from IM
	additive_params = make_additive_params(lat_task.states, param_names)
	
	m = metropolis.Metropolis(lattice_graph, cells, allowed_cells, interaction, internal_energies, transitions, T_list, additive_params, k_B, seed) 
	m.phys_diffusion = False
	m.E_inf = lat_task.INF_E
	m.PT_period = 10 * len(cells) 	# Each m.PT_period steps we try to switch the temperature
	m.diff_cui_min = 1 # Minimal
	m.diff_cui_max = 1

	m.regr = regr
	m.regr_array = lattice_graph
	m.lattice_task = lat_task
	m.param_names = param_names
	m.lattice = Lattice(metropolis = m)

	return m

def run(m, log_periods_cnt, log_period_steps=None, log_callback=None, params_period_steps=None, relaxation_steps = None, bcast_full_params_log = True, traj_fns='auto', recalc_curs=True):
	"""
		Perform Metropolis iterations
		
		Parameters:
			:m: Metropolis object
			:log_periods_cnt: number of log periods to perform
			:log_period_steps: number of Metropolis iterations in a single log period. By default ``m.cells_count`` value is used so log period is equivalent to conventional *Monte Carlo step* notion
			:log_callback: function to be called after each log period, ``log_callback`` function must take ``m`` as a parameter and can return any object as result. List of all objects returned from ``log_callback`` will be returned as a result of overall ``run()`` call. By default is None, so nothing is logged.
			:params_period_steps: period for sampling of energy and state properties (see notes on ``make_metropolis()`` function). Samples are stored in ``full_params_log`` attribute of ``m`` object. Meassured in Metropolis iterations. Default value ``(log_periods_cnt * log_period_steps)//1000 + 1`` so up to 1000 entries will be added to ``full_params_log``.
			:relaxation_steps: number of Metropolis iterations to be skipped before logging and parameters sampling. Default value ``log_periods_cnt * log_period_steps``
			:bcast_full_params_log: set to False if parameters samples should not be broadcasted to all MPI processes. By default ``True``, so every processes receives complete sample of parameters.
			:traj_fns: list of XYZ file names to be used to save snapshots of the lattice each ``log_period_steps`` iteration. ``traj_fns[i]`` is used to save samples from *i*-th replica (see notes on ``make_metropolis()`` function). By default "traj.{temperature}.xyz" is used for each temperature
			:recalc_curs: Call ``recalc_curs()`` method before running Metropolis simulaions. ``recalc_curs()`` recomputes total energy and additive parameter values. It is computationally expensive, but necessary if ``cells`` property was modified outside of Metropolis iterations, for example due to coverage initialization.
			
		Number of steps to execute: ``relaxation_steps + log_periods_cnt * log_period_steps``.
		Number of ``full_params_log`` entries: ``(log_periods_cnt * log_period_steps) / params_period_steps``.
		Number of samples in trajectory files: ``log_periods_cnt``.
		
			
		Results:
			List of objects returned by ``log_callback`` function calls
			
			After the function call ``m.full_params_log`` contains three-dimensional array with samples of simulation parameters. Parameter values are averaged over lattice sites.
			
			``m.full_params_log[i,j,k]`` is the value of the *k*-th parameter on *j*-th time period from *i*-th replica. Parameter index ``k`` correspond to the *k*-th item of ``param_names`` argument of ``make_metropolis()`` function. In addition to state parameters, several system-wide parameters are included into ``m.full_params_log``. In particular:
			
				- ``m.full_params_log[i,j,-1]`` index of the temperature of this sample
				- ``m.full_params_log[i,j,-2]`` total energy of the system per one lattice cell
				- ``m.full_params_log[i,j,-3]`` lateral interactions energy (total energy minus adsoprtion energy) per lattice cell
				- ``m.full_params_log[i,j,-4]`` acceptance rate of Metropolis iterations
				- ``m.full_params_log[i,j,-5]`` KMC r0 parameter, i.e. maximal step rate, should be constant through correct simulaion
				
				- ``m.full_params_log[i,j,-6]`` free adsorption energy per lattice cell
				- ``m.full_params_log[i,j,-7]`` ground state (minimal) adsorption energy per lattice cell
				- ``m.full_params_log[i,j,-8]`` entropy of adsoprtion complexes per lattice cell
				- ``m.full_params_log[i,j,-9]`` mean internal energy (enthalpy) of adsoprtion complexes per lattice cell
				
				- ``m.full_params_log[i,j,:-9]`` samples of states parameters - see ``param_names`` argument of ``make_metropolis()`` function.
	"""

	if log_period_steps is None:
		log_period_steps = m.cells_count

	if relaxation_steps is None:
		relaxation_steps = log_periods_cnt * log_period_steps

	if params_period_steps is None:
		params_period_steps = (log_periods_cnt * log_period_steps)//1000 + 1
	
	if log_callback is None:
		def log_callback(m):
			return None
	
	if traj_fns=='auto':
		traj_fns = ["traj.{}.xyz".format(T) for T in m.T_list]
	
	if traj_fns is not None:
		assert len(traj_fns) == len(m.T_list), "Improper number of trajectory filenames: {} instead of {}".format(len(traj_fns), len(m.T_list))
		def write_traj(m):
			m.save_as_xyz(traj_fns[m.T_idx], comment='E={}'.format(m.curE.sum()))
	else:
		def write_traj(m):
			pass
		

	result = {}  # dict of temperatures to lists with log_callback() results  
	m.params_log_period = log_period_steps
	
	if MPI.COMM_WORLD.Get_rank() == 0:
		if relaxation_steps > 0:
			print ("Relaxation steps...")
		else:
			print ("No relaxation steps requested.")
	if recalc_curs:
		if MPI.COMM_WORLD.Get_rank() == 0:
			#print ("Calling recalc_curs() ...")
			pass
		m.recalc_curs()
	m.run(relaxation_steps)
	if relaxation_steps > 0 and MPI.COMM_WORLD.Get_rank() == 0:
		print ("Relaxation completed.")

	# assert all([pl.enabled for pl in m.param_limits]), [pl.enabled for pl in m.param_limits]
	m.full_params_log = []
	m.params_log_period = params_period_steps
	time_start = time()
	for i in range(log_periods_cnt):
		if MPI.COMM_WORLD.Get_rank() == 0:
			time_passed = time() - time_start
			time_per_step = time_passed / i if i > 0 else np.inf
			ETA = log_periods_cnt * time_per_step - time_passed
			print('\rStep # {} of {}. Time passed: {:.2f} seconds. Estimated time before completion: {:.2f} seconds'.format(i, log_periods_cnt, time_passed, ETA), end = '\r')
		
		m.run(log_period_steps)
		m.full_params_log += [deepcopy(m.params_log)]
		res_i = log_callback(m)
		result.setdefault(m.T_idx,list()).append(res_i)
		write_traj(m)
	if MPI.COMM_WORLD.Get_rank() == 0:
		print ("\n\nDone!\n\n")
	#print "Gathering callback results..."
	result = MPI.COMM_WORLD.gather(result,root=0)
	#print "Gathering callback results... done!"

	if MPI.COMM_WORLD.Get_rank() == 0:
		aggr = result[0]  # use root dict as initial for aggregated dict
		for dict_i in result[1:]:
			for T_idx, res_log in dict_i.items():
				aggr.setdefault(T_idx, list()).extend(res_log)
				
		result = [res_log for T_idx, res_log in aggr.items()]
		
		assert all([len(log_i) == log_periods_cnt for log_i in result]) # check for each temperature
	
	result = MPI.COMM_WORLD.bcast(result,root=0)

	full_params_log = np.concatenate(m.full_params_log)	# [time, param] concatenate along `time` axis
	full_params_log = MPI.COMM_WORLD.gather(full_params_log,root=0) # [rank, time, param]
	if MPI.COMM_WORLD.Get_rank() == 0:
		full_params_log = np.swapaxes(full_params_log, 0, 1)	# # [time, rank, param]
		
		# sort by the last element (T_idx)
		full_params_log = np.array([sorted(r, key=lambda v: v[-1]) for r in full_params_log]) # r[T_idx, param], v[param] [time, T_idx, param]
		full_params_log = np.swapaxes(full_params_log, 0, 1)	# [T_idx, time, param]

	if bcast_full_params_log:
		#print "bcast full param log..."
		m.full_params_log = MPI.COMM_WORLD.bcast(full_params_log, root=0)
		#print "bcast full param log... done!"
	else:
		m.full_params_log = full_params_log

	return result
	
"""
def make_CDF(y):
	x = sorted(y)
	N = len(y)
	p = 1./N
	CDF = []
	cum_CDF = 0.
	for x in x:
		CDF.append(cum_CDF)
		cum_CDF += p
	assert abs(cum_CDF - 1.0) < 1e-6
	return np.array(x), np.array(CDF)
"""

def bins_count(brange, group_step, origin):
	""""""
	"""
		see divisibles() in metropolis.cpp for implementation explanation
	"""
	totalBins = int(floor((brange[1] - origin)/group_step))
	excludeBins = int(floor((brange[0] - origin)/group_step))
	return totalBins - excludeBins


def make_histo(y, brange, group_step, origin=0.0):
	N = bins_count(brange, group_step, origin)
	assert N > 0
	h = np.histogram(y, bins=N, range=brange, density = False)
	return h[0] * (1./len(y)), h[1]
	
def group_by_column(data, grouping_column, brange, group_step, origin=0.0):
	""""""
	"""
		data[time, param]
		
		Returns:
			data[group, time, param]
	"""
	N = bins_count(brange, group_step, origin)
	assert N > 0
	def bin_index(r):
		idx = int(floor((r[grouping_column] - brange[0])/group_step))
		if idx < 0:
			return -1	# too small outlier
		if idx >= N:
			return N	# too big outlier
		return idx

	d =dict([ (k,list(g)) for k,g in groupby(sorted(data, key=bin_index), bin_index)])
	
	return [d.get(i, []) for i in range(N)]
	

def group_statistics(params_log, param_idx, lower_limit, upper_limit, step):
	""""""
	"""
		params_log[time, param_idx]
		Returns:
			means: [group, param], zeros for empty groups
			stds: [group, param], zeros for empty groups
			probs: [group]
			outliers_part: float from 0 to 1
	"""
	m = params_log.shape[1] # number of parameters
	
	#hist,bins = mc.make_histo(params_log[:, limit_param_idx], (lower_limit, upper_limit), limit_step)
	groups = group_by_column(params_log,  param_idx, (lower_limit, upper_limit), step)
	means = np.array([np.mean(g, axis=0) if len(g) > 0 else [0.]*m for g in groups]) # [group, param]
	stds  = np.array([np.std(g, axis=0)  if len(g) > 0 else [0.]*m for g in groups]) # [group, param]
	lens = np.array([len(g) for g in groups], dtype=float) # [group, param]
	probs = lens / sum(lens) if sum(lens) > 0 else [0.] * len(lens)
	outliers_part = 1.0 - sum(lens) / len(params_log)
	return means, stds, probs, outliers_part

		

	
class ACFAnalysis:
	def __init__(self):
		pass
	
	def __repr__(self):
		return "AC times: zero {0.zero_time:.3f}; exp {0.ac_time_exp:.3f} (rmse {0.ac_time_exp_rmse:.3f}); int {0.ac_time_int:.3f} len: {1}".format(self, len(self.acf))

def autocorr_analysis(acf, m=10):
	r = ACFAnalysis()
	r.acf = acf
	r.zero_time = np.argmax(acf <= 0.)
	if r.zero_time == 0 :
		r.zero_time = len(acf)
		
	if r.zero_time > 2:
		x = np.arange(r.zero_time-1)
		y = np.log(acf[:r.zero_time-1])
		r.ac_time_exp = -sum(x*x)/sum(x*y)	# exponential AC time - least squares fitting to exponential shape of ACF
		
		r.ac_time_exp_rmse = sum(np.exp( x * (-1./ r.ac_time_exp) - acf[:r.zero_time-1])**2)**0.5 / (r.zero_time-1)
	else:
		r.ac_time_exp = 1.
		r.ac_time_exp_rmse = 0.

	r.expected_acf_sputter = 1./(len(acf)**0.5)
	r.acf_sputter = [np.std(acf[i*len(acf)//m:(i+1)*len(acf)//m]) for i in range(m)]
	r.acf_mean = [np.mean(acf[i*len(acf)//m:(i+1)*len(acf)//m]) for i in range(m)]
	
	r.ac_time_int = sum(acf[1:r.zero_time])*2. + 1.	# integrated AC time
	return r

	
def autocorr_func(y_, m = None, method="fft"):
	""""""
	
	"""
		m - number of items lefter and righter of origin in autocorr_func
		returns 2*m+1 element array
		
		Note: 
		http://golem.fjfi.cvut.cz/wiki/Library/others/BenczeA_Autocorrelation_05.pdf
			Autocorrelation analysis and statistical consideration for the determination of velocity fluctuations in fusion plasmas
			DOI: 10.1063/1.1909200
			"Our result may be surprising as the relative scatter does not depend on the ns=Ns/DT event rate. 
			One would expect that  for  higher  event  rates  the  statistics  should  improve. However, in our
			 case the scatter of the correlation function is produced  by  random  overlapping  of  events;  
			 this  is  proportional  to nS.  The  mean  of  the  correlation  function  is  also proportional to
			 nS, therefore the relative scatter will not de-pend  on  the  event  rate.  On  the  other  hand,  
			 when DT is  increased  at  a  fixed  event  rate  the NS number  of  events  increases  as  well  
			 without  changing  the  random  coincidence between  the  events,  and  as  a  result  the  relative 
			 scatter  de-creases.  In  this  sense  the  number  of  measured  events  does improve statistics."
	"""
	N = len(y_)
	if m is None:
		m = N-1
	assert m < len(y_), ["ACF length must be smaller than sample size", m, N]
	y = y_ - np.mean(y_)
	std_y = np.std(y)
	if std_y == 0:
		print ("WARNING! Standart deviation of time series is zero. Can't compute autocorrelation. Return None")
		return None
	y /= std_y
	if method=="naive":
		c = np.correlate(y, y, 'full')
		assert len(c) == (2*N-1), [len(c), N]
		Ns = np.array(list(range(1,N)) + [N] + list(range(N-1,0,-1)))
		c = c / Ns
		c =  c[len(c)/2 :]
	elif method=="fft":
		r = np.fft.rfft(y)
		s = abs(r)**2
		c = np.fft.irfft(s)
		c /= N
	else:
		assert False, method
	
	return c[: m ]
	

def stat_digest(m, verbose=True):
	if MPI.COMM_WORLD.Get_rank() != 0:
		return

	param_names = m.param_names + ["Energy"]
	param_indices = list(range(0, len(m.param_names))) + [-2]

	digest = []
	for Ti,T in enumerate(m.T_list):
		d = {} # i-th temperature dict
		print ("Temperature # {} = {}".format(Ti,T))
		d["T"] = T
		for pi, pn in zip(param_indices, param_names):
			pd = {} # param dict
			print ("\tParameter # {} : '{}'".format(pi,pn))
			data = m.full_params_log[Ti,:,pi]
			mean = np.mean(data)
			std = np.std(data)
			pd['mean'] = mean
			pd['std'] = std
			print ("\t\tSample size\t", len(data))
			print ("\t\tSample mean\t{:.6f}".format(mean))
			print ("\t\tSample stdDev\t{:.6f}".format(std))
			acf = autocorr_func(data)
			pd['acf'] = acf
			if acf is not None:
				acf_a = autocorr_analysis(acf)
				pd['acf_a'] = acf_a
				#print ("\t\tACF\t", acf_a)
				print ("\t\tAutocorrelation function parameters:")
				print ("\t\t\tFirst zero time:\t", acf_a.zero_time)
				print ("\t\t\tExponential time:\t{:.3f} (RMSE={:.3f})".format(acf_a.ac_time_exp, acf_a.ac_time_exp_rmse))
				print ("\t\t\tIntegrated time:\t{:.3f}".format(acf_a.ac_time_int))
				neff_int = len(data) / acf_a.ac_time_int
				pd['neff_int'] = neff_int
				print ("\t\tEffective sample size integrated\t{:.3f}".format(neff_int))
				neff_exp = len(data) / (2. * acf_a.ac_time_exp)
				pd['neff_exp'] = neff_exp
				print ("\t\tEffective sample size exponential\t{:.3f}".format(neff_exp))
				if abs(1. - neff_exp/neff_int) > 0.1:
					pass # not accurate criterion
					# print ("\t\t\033[1;33mAchtung!\033[0;0m Integrated and exponential autocorrelation times too different! Probably non-equilibrium state")
				print ("\t\tSample mean stdDev\t{:.3f}".format(std / neff_int))
			d[pn] = pd
		digest += [d]
		data = m.full_params_log[Ti,:,param_indices]
		corrs = np.corrcoef(data, rowvar=True)
		print ("\tCorrelations between parameters:")
		for row in corrs:
			print ('\t\t', ' '.join(map("{:.3f}".format, row)))

	meanEs = [d['Energy']['mean'] for d in digest]
	if len(m.T_list) > 1:
		print("Recommended temperatures:", recommended_temperatures(m.T_list, meanEs))
	return digest

def recommended_temperatures(T, E):
	f = interp1d(E, T)
	desired_energies = np.linspace(min(E), max(E), len(E))
	return [f(Ei).item() for Ei in desired_energies]
	
def kmc_setup(m, r0 = 0.0):
	"""
		Initialize Metropolis object for Kinetic Monte Carlo simulaion and set r0 parameter
	"""
	m.setup_kmc(r0)
	
def wl_setup(m, emin, emax, bins_count):
	m.wl_emin = emin
	m.wl_emax = emax
	m.wl_bins_count = bins_count
	m.setup_wl({-2:[emin, emax, bins_count]}, 0.8, 1., 1., 1., 100000, 1000000)
	
def wl_analysis_base(lng, N, T, k_B, emin, emax, bins_count):
	assert len(lng) == bins_count, (len(lng), bins_count)

	E = np.linspace(emin, emax, bins_count)
	
	beta = 1./(T*k_B)
	w_per_N = np.exp( (lng - E*beta)/N ) # = np.exp( (lng + A - E*beta)/N )  / exp(A/N) = w_per_N_cor / exp(A/N)
	# w == w_per_N ** N
	w_per_N_max = max(w_per_N) # = max(w_per_N_cor / exp(A/N)) = max(w_per_N_cor) /  exp(A/N) = w_per_N_max_cor /  exp(A/N) 
	w_per_N_normed = w_per_N / w_per_N_max
	# w_per_N == w_per_N_max * w_per_N_normed
	# w == (w_per_N_max ** N) * (w_per_N_normed ** N)
	w_normed = w_per_N_normed ** N
	# w == (w_per_N_max ** N) * w_normed
	# Z == sum(w) == (w_per_N_max ** N) * sum(w_normed)
	Z_normed = sum(w_normed)
	# Z = (w_per_N_max ** N) * Z_normed
	# Z_per_N == Z ** (1/N) == w_per_N_max * (Z_normed ** 1/N)
	Z_per_N = w_per_N_max * (Z_normed ** (1/N))
	
	F_per_N = -log(Z_per_N)/beta
	# probs = w/Z = (w_per_N_max ** N) * w_normed / ((w_per_N_max ** N) * Z_normed) = w_normed / Z_normed
	probs = w_normed / Z_normed
	
	E_per_N = E / N
	
	U_per_N = sum(E_per_N*probs)
	DE_per_N = N * sum(E_per_N*E_per_N*probs)
	
	C_per_N = (DE_per_N - N* (U_per_N**2) ) / (k_B * T**2)
	S_per_N = beta * (U_per_N - F_per_N)
	
	WLAnalysis = namedtuple('WLAnalysis', 'T beta w Z F probs U DE C S')
	return WLAnalysis(T, beta, w_per_N, Z_per_N, F_per_N, probs, U_per_N, DE_per_N, C_per_N, S_per_N)
	
def wl_analysis(m, T=None):
	if T is None:
		T = m.T_list[0]

	lng = m.get_named_data('ln_g')[1:-1]
	lng -= min(lng)
	return wl_analysis_base(lng, m.cells_count, T, m.k_B, m.wl_emin, m.wl_emax, m.wl_bins_count)

