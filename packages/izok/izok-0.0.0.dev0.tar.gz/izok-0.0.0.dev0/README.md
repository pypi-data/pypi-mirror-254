Izok
=====

Izok is an open source Python-based software package that allows you to formulate an optimization problem in an easy-to-learn and efficient modeling language similar to other modeling languages AMPL, AIMMS and GAMS, and then automatically implement it in open source software package Pyomo.

It includes:

-   The objects of the Izok model and the Pyomo model have the same names.
-   Model are compiled to optimized Pyomo code just-in-time.
-   Exceptions point to the correct line in model to make debugging easier.

Izok's philosophy is that while working with the inputs and outputs of mathematical models is done using Python and Pyomo whenever possible, this should not make the mathematical modeler's job more difficult by limiting functionality and expressiveness too much.

In A Nutshell
-------------

Pyomo code (pyomo-tutorials: https://github.com/brentertainer/pyomo-tutorials/blob/master/introduction/02-lp-pyomo.ipynb)


.. code-block:: python

    expr = sum(model.c[w, t] * model.x[w, t]
           for w in model.workers for t in model.tasks)
    model.objective = pe.Objective(sense=pe.minimize, expr=expr)

    model.tasks_done = pe.ConstraintList()
    for t in model.tasks:
        lhs = sum(model.x[w, t] for w in model.workers)
        rhs = 1
        model.tasks_done.add(lhs == rhs)

Izok code

.. code-block:: python

    build(model, """
    obj minimize obj.. sum(w, sum(t, c(w,t) * x(w,t)));
    st1(t).. sum(w, x(w,t)) =l= 1;
    """)

Links
-----

-   Source Code: https://gitflic.ru/project/enom/izok
