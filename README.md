# cahn-hilliard-equation
As originally proposed, the Cahn-Hilliard equation describes the process of a single phase (region of material that is chemically uniform) changing without nucleation into two phases that aren't able to be mixed. This process is called spinodal decomposition and the two at most partially miscible (mixable) fluids is called a binary fluid. The absence of nucleation means that the transition happens smoothly everywhere rather than at discrete points. An example of spinodal decomposition is an alloy of at least two metals being rapidly cooled from a high temperature, under certain conditions, will separate into distinct areas rich in a particular metal. The Cahn-Hilliard equation is

```math
\frac{\partial c}{\partial t}=D\nabla^2(c^3-c-\gamma\nabla^2c)
```

where $c\in[-1,1]$ represents the concentration of each component in the binary fluid. Positive $c$ indicates the presence of one component at a particular point, negative $c$ of the other. $D$ is the diffusion coefficient and $\gamma$ controls the length of the transition from one component to another. The equation also can be extended to a variety of areas, such as in biology, it can be modified to describe the front of cells invading a wound and clustering of tumor cells (Khain and Sander 2008).

I numerically solved the Cahn-Hilliard equation with periodic boundary conditions via Fast Fourier Transform. The initial condition is randomized to represent the two components beginning well-mixed before separating. Now for the fun part, the visualization:

![Visualization of a solution to the Cahn-Hilliard equation with periodic boundary conditions](https://github.com/DonFactorial/cahn-hilliard-equation/blob/main/CahnHilliard.gif?raw=true)

Reference:
Sander LM Khain E. “Generalized Cahn-Hilliard equation for biological applications”. In: Phys Rev E Stat Nonlin Soft Matter Phys. 77.5 Pt 1 (2008), p. 051129. doi: https://doi.org/10.1103/PhysRevE.77.051129.

A neat resource all about the Cahn-Hilliard equation:
A. Miranville. “The Cahn-Hilliard equation: recent advances and applications”. In: SIAM, Society for Industrial and Applied Mathematics, 2019.
