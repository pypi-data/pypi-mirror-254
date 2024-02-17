from sage.modules.free_module_element import vector
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ

def coboundary_basis (s, verb=False):
	"""
	Return a basis of the space of coboundaries, as a matrix.
	A coboundary is a linear form such that image of ab(w) is zero
	for every w such that w.w_0 is a word of the language of s.

	INPUT:

		- ``s`` - WordMorphism

		- ``verb`` - Boolean (default: ``False``) if True print informations.

	OUTPUT:
		A matrix

	EXAMPLES:

		sage: from eigenmorphic import *
		sage: s = WordMorphism('a->ab,b->a')
		sage: coboundary_basis(s)
		[
		<BLANKLINE>
		]

		sage: s = WordMorphism('a->b,b->cd,c->ab,d->c')
		sage: coboundary_basis(s)
		[
		(1, 0, 0, -1),
		(0, 1, -1, 0)
		]

	"""
	_,lr = return_substitution(s, getrw=True)
	if verb > 0:
		print("return words : %s" % list(lr))
	return matrix([w.abelian_vector() for w in lr]).transpose().kernel().basis()

def return_substitution (s, check_primitive=True, getrw=False, verb=False):
	"""
	Return the set of return words on some letter.

	INPUT:

		- ``s`` - WordMorphism

		- ``check_primitive`` - bool (default: ``True``) - if True, check that the substitution is primitive

		- ``getrw`` - bool (default: ``False``) - if True, return also the set of return words

		- ``verb`` - bool (default: ``False``) - if True print informations.

	OUTPUT:
		A substitution.

	EXAMPLES:

		sage: from eigenmorphic import *
		sage: s = WordMorphism('a->ab,b->a')
		sage: return_substitution(s, getrw=True)
		(WordMorphism: 0->01, 1->0, {word: a: 1, word: ab: 0})

	"""
	from sage.combinat.words.morphism import WordMorphism
	if check_primitive:
		if not s.is_primitive():
			raise ValueError("The input substitution must be primitive !")
	rw = dict() # set of return words
	rs = dict() # result substitution
	to_see = [] # set of words to consider
	# take a word u in the subshift
	s0 = s
	n = 0
	while True:
		l = s.fixed_points()
		if len(l) > 0:
			break
		s = s*s0
		n += 1
	if verb > 0:
		print("take the %s-th power of s" % (n+1))
	u = l[0]
	if verb > 1:
		print("chosen fixed point: %s" % u)
	# find a first return word
	for i,a in enumerate(u):
		if i > 0 and a == u[0]:
			to_see.append(u[:i])
			rw[u[:i]] = 0
			rs[0] = []
			break
	if verb > 0:
		print("first return word found: %s" % u[:i])
	def add(w):
		if w not in rw:
			to_see.append(w) # do the same for every new return word
			rs[len(rw)] = []
			rw[w] = len(rw)
	while len(to_see) > 0:
		w = to_see.pop()
		# compute the image by s and decompose it as return words
		sw = s(w)
		ri = 0
		for i,a in enumerate(sw):
			if i > 0 and a == sw[0]:
				w2 = sw[ri:i]
				add(w2)
				rs[rw[w]].append(rw[w2])
				ri = i
		w2 = sw[ri:]
		add(w2)
		rs[rw[w]].append(rw[w2])
	if getrw:
		return WordMorphism(rs), rw
	return WordMorphism(rs)

