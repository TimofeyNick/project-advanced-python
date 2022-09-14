'''
The workspace is a virtual structure that contains an initial data tree as well as a list of tasks that could be performed.
The exusion is made as follows:
1. Task model. The system calculates an acyclic dependency graph of tasks and data.
2.  Lazy computation model. The Goal tree is created for each specific computation.
3. Computation. When the top level goal is triggered, it invokes computation of all goals in chain behind it.

'''
