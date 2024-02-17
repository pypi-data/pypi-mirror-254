from  math import log, ceil, floor
from susmost.savexyz import shift_xyz_data, generate_xyz
import sys, copy, time

def to_bin(x, B):
	"""
		x - index
		B - bitness
	"""	
	res = [0]*B
	list(range(x)) # assertion x is integer
	for i in range(B):
		res[B-1-i] = x%2
		x = x / 2
	return res
	
def from_bin(b):
	res = 0
	for ai in b:
		res = res*2 + ai		
	return res
	
def list_of_transitions(x, B, max_x):
	bin_x = to_bin(x,B)
	res = []
	res.append(x) # stay here
	for i in range(len(bin_x)):
		new_x = bin_x[:]
		new_x[i] = 1-new_x[i]
		y = from_bin(new_x)
		res.append(y if y <= max_x else x)
	return res
	
def make_tmatrix(states, beta, M):
	sorted_states = sorted( zip(states, list(range(len(states)))) , key = lambda s : -s[0].free_E(beta))
	res = [[] for s in states]
	for si,(s,i) in enumerate(sorted_states):
		ri = []
		for s2,i2 in sorted_states[max(0, si-M) : min(len(states), si+M+1)]:
			ri.append(i2)
		res[i] = sorted(ri)
	return res
	
def make_one_state_tmatrix(states):
	def states_distance(s1,s2):
		if hasattr(s1,'substates'):
			s1 = s1.substates[0]
		if hasattr(s2,'substates'):
			s2 = s2.substates[0]

		return len([1 for os1,os2 in zip(s1.orig_states,s2.orig_states) if os1.idx != os2.idx])
		
	res = []
	for s in states:
		nears = []
		for i2,s2 in enumerate(states):
			if states_distance(s,s2) <=1:
				nears.append(i2)
		res.append(nears)
	#print 'res == ',res
	return res

def hashed_IM(states, edges, IM):
	hIM = dict()
	for s1,_ in enumerate(states):
		hIM_s1 = dict()
		for ei,_ in enumerate(edges):
			hIM_s1[ei] = IM.edge_hash(s1,ei)
		hIM[s1] = hIM_s1
	return hIM

def IM_distance(s1, s2, hIM, edges):
	d = 0
	for ei,_ in enumerate(edges):
		if hIM[s1][ei] != hIM[s2][ei]:
			d += 1
	return d

def make_IMdiff_tmatrix(states, edges, IM, M, Ediff):
	hIM = hashed_IM(states,edges,IM)
	res = []
	for s1,_ in enumerate(states):
		dists = sorted([(IM_distance(s1, s2, hIM, edges),s2) for s2,_ in enumerate(states)])
		#print s1, dists
		nears = [s2 for d,s2 in dists if d <= M and abs(states[s1].min_E() - states[s2].min_E()) < Ediff]
		res.append(sorted(nears))
	return res


def make_one_IMdiff_tmatrix(states, edges, IM, diff_limit):
				
	sd_cache = dict()
	def states_too_different_2(s1,s2):
		cache_val =  sd_cache.get((s1.idx,s2.idx), None)
		if cache_val is not None:
			return cache_val
			
		different_edges_cnt = 0		
		for edge_idx in range(1,len(edges)):
			edge_int1 = IM[s1.idx].get(edge_idx, None) if s1.idx in IM else None
			edge_int2 = IM[s2.idx].get(edge_idx, None) if s2.idx in IM else None

			if ((edge_int1 is None) != (edge_int2 is None)) or (edge_int1 != edge_int2):
				if edge_int1 is None:
					different_edges_cnt += len(edge_int2)
				elif edge_int2 is None:
					different_edges_cnt += len(edge_int1)
				else:				
					#different_edges_cnt += len(set(edge_int1.keys()).symmetric_difference(set(edge_int2.keys())))
					different_edges_cnt += len(set(edge_int1.items()).symmetric_difference(set(edge_int2.items())))
				#print 'DIFF2', edge_idx
				#print 'DIFF2\t', sorted(edge_int1.iteritems())
				#print 'DIFF2\t', sorted(edge_int2.iteritems())
				
		sd_cache[(s1.idx,s2.idx)] = different_edges_cnt
		sd_cache[(s2.idx,s1.idx)] = different_edges_cnt
		
		return different_edges_cnt
			

		
	res = [set() for s in states]
	for i1,s in enumerate(states):
		print(i1,'of', len(states))
		assert(i1 == s.idx)
		#nears = []
		sds = sorted([ (states_too_different_2(s,s2), i2) for i2,s2 in enumerate(states) ])
		for sd, i2 in sds[:15]:
			res[i1].add(i2)
			res[i2].add(i1)
		
		'''
		min_sd = None
		min_sd_state = None
		for i2,s2 in enumerate(states):
			assert(i2 == s2.idx)
			if s.idx == s2.idx:
				res[i1].add(i2)	#stay the same
			else:
				sd = states_too_different_2(s,s2)
				#if (s.idx == 163):
				#	print 'SD', sd
				#print 'SD:', sd, '\t', s, '\t', s2
				if sd <= diff_limit:
					res[i1].add(i2)
				if sd == 0:
					print 'EQUAL:', s, '\t', s2
					
				if (min_sd is None) or (sd < min_sd):
					min_sd  = sd
					min_sd_state = i2
		#assert len(nears) > 1, (s, nears, diff_limit)
		if len(res[i1]) <=1:
			assert (min_sd_state is not None), (s, res[i1], diff_limit)
			res[i1].add(min_sd_state)
			res[min_sd_state].add(i1)
		'''

	for i1,s in enumerate(states):
		print('TM:', len(res[i1]), s)

	#print 'res == ',res
	return res


def make_dumb_tmatrix(states):
	return [[i for i,_ in enumerate(states) if i!=j] for j,_ in enumerate(states)]
	

def make_tmatrix_with_fixes(states, fixed_prop_name, fixed_prop_diff=0):
	return [[i for i,s2 in enumerate(states) if abs(s2.get_prop(fixed_prop_name) - s.get_prop(fixed_prop_name)) <= fixed_prop_diff] for s in states]
	
def make_tmatrix_by_condition(states, condition_function):
	return [[i for i,s2 in enumerate(states) if condition_function(s, s2)] for s in states]

	

def show_tmatrix(TM, states):
	import graphviz as gv
	data = []
	g1 = gv.Graph(format='svg')
	for i1,s1 in enumerate(states):
		g1.node(str(i1))
		data += shift_xyz_data(s1.xyz, [i1*20, 0, 0])
		for shift_i,i2 in enumerate(TM[i1]):
			assert(i2 in TM[i1]), (i1,i2)
			assert(i1 in TM[i2]), (i1,i2)
			
			s2 = states[i2]
			data += shift_xyz_data(s2.xyz, [i1*20, (shift_i+2)*5, 0])
			g1.edge(str(i1), str(i2))
	#print g1.render(filename='g1')
	return data


def solve_tmatrix(TM, ads_energies):
	return []
	'''
	b = sy.Symbol('b')
	E = ads_energies[:]
	al = [[sy.Symbol('alpha_'+str(i)+'_'+str(j)) for j in range(len(TM)) ] for i in range(len(TM))]
		
	eqs = sum([ [al[j][i]*sy.exp(b*E[i]) - al[i][j]*sy.exp(b*E[j]), al[i][j]+al[j][i]-1.0] for i in range(len(TM)) for j in TM[i] if j > i], []) + [ sum( [al[i][j]  for j in TM[i]] ) -1  for i in range(len(TM)) ]
	
	for i in range(len(TM)):
		for j in TM[i]:
			if j > i:
				
	
	print 'eqs:'
	print  sy.pprint(eqs, use_unicode=True)
	print 'solving:'
	sys.stdout.flush()
	ss = sy.solve(eqs, sum(al,[]))
	print 'solved'
	print 'solved'
	sys.stdout.flush()
	for ssi in ss:
		print 'Solution #:'
		print sy.pprint(ssi, use_unicode=True)
	sys.stdout.flush()
	'''
	
	'''
	print 'sys.getdefaultencoding().', sys.getdefaultencoding()
	s = [sy.Symbol('s' + str(i)) for i in range(len(TM))]
	print 's = ', s
	b = sy.Symbol('b')
	ads_energies = [sy.Symbol('E' + str(i)) for i in range(len(TM))]
	eqs = [  s[i]*sum([s[k] for k in TM[i]]) - sy.exp(-b*ads_energies[i])  for i in range(len(TM)) ]
	print 'eqs:'
	print  sy.pprint(eqs, use_unicode=True)
	print 'solving:'
	sys.stdout.flush()
	ss = sy.solve(eqs, s)
	print 'solved'
	sys.stdout.flush()
	for ssi in ss:
		print 'Solution #:'
		print sy.pprint(ssi, use_unicode=True)
	sys.stdout.flush()
	'''
	
	
	
	
	
