## Location-Controlled Oscillator Model

This repository contains the IPython Notebook files that were used to develop the location-controlled oscillator (LCO) model that I presented at the Society for Neuroscience 2014 meeting:

* J. D. Monaco, K. Zhang, and H. T. Blair. (2014) **Spatial rate/phase codes provide landmark-based error correction in a temporal model of theta cells**. Society for Neuroscience 2014, Washington, D.C. 752.07.

The poster is available in PDF form on my website:

* [http://jdmonaco.com/monaco-landmark-poster-sfn14.pdf](http://jdmonaco.com/monaco-landmark-poster-sfn14.pdf)

### Abstract

The spatial firing patterns of place cells in hippocampus and grid cells in entorhinal cortex form a spatial representation that is stable during active navigation but also able to encode changes in external landmarks or environmental structure. One class of model that has been investigated as a possible mechanism for generating these spatial patterns relies on temporal synchronization between theta cells, which fire strongly with the septohippocampal theta rhythm (6–10 Hz) and are found throughout the hippocampal formation, that act as velocity-controlled oscillators. However, a critical problem for these models is that the oscillatory interference patterns that they generate become unstable in the presence of phase noise and errors in self-motion signals. Previous studies have proposed hybridizing temporal models with attractor network models or integrating environmental feedback from sensory cues. Preliminary data from subcortical regions in rats suggest that some theta cells exhibit spatially selective firing similar to hippocampal place fields or entorhinal/subicular boundary fields. These cells also demonstrate a consistent phase relationship across space, relative to ongoing hippocampal theta and to other simultaneously recorded cells, that is correlated with the firing rate at a given location. Inspired by this data, we present a novel synchronization model in which place cells or boundary-vector cells provide a stable, landmark-based excitatory input that drives a rate-to-phase mechanism to generate a population of cells that act as location-controlled oscillators. These cells fire preferentially at theta phases that are specific to a given location, determined by the presence of external landmarks. We show that these location-controlled oscillators provide a stable spatial reference that corrects phase errors in velocity-controlled oscillators, thus preventing the encoded position from drifting with respect to the environment and the actual position of the animal. Thus landmark-based rate/phase correlations in extrahippocampal areas may provide the sensory feedback required by temporal models of neural representations of space.

### NBViewer Links

These links will display the model notebooks using the IPython project's [NBViewer](http://nbviewer.ipython.org/) service. These links do not actually run the code, they only render the notebook cells.

* [notebooks/load_cylinder_trackdata.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/load_cylinder_trackdata.ipynb)
    * Extract the trajectory data from the preliminary data set
* [notebooks/trajectory.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/trajectory.ipynb)
    * Set up the model inputs representing the spatial trajectory and arena
* [notebooks/mehta_mechanisms_demo.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/mehta_mechanisms_demo.ipynb)
    * Demonstration of Mehta mechanism with Izhikevich bursting neuron and fixed depolarization
* [notebooks/mehta_ramp_demo.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/mehta_ramp_demo.ipynb)
    * Demonstration of rate-to-phase conversion in bursting neuron with ramping depolarization
* [notebooks/rate_lvc.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/rate_lvc.ipynb)
    * Landmark-vector cells (LVCs) that represent landmark/object responses in LEC/CA1
* [notebooks/rate_bvc.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/rate_bvc.ipynb)
    * Boundary-vector cells (BVCs) that represent boundary responses in subiculum/MEC
* [notebooks/rate_lco.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/rate_lco.ipynb)
    * Location-controlled oscillators (LCOs) are a hypothetical layer of theta-rhythmic cells that combine landmark/boundary (LVC/BVC) input with theta oscillations to create a phase-code that depends on external environmental features
* [notebooks/rate_vco.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/rate_vco.ipynb)
    * Velocity-controlled oscillators (VCOs) are path-integrating oscillators where frequency is modulated by heading and velocity of the virtual rat's trajectory
* [notebooks/find_weights.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/find_weights.ipynb)
    * Moore-Penrose pseudoinverse is used to compute a weight matrix that drives VCOs with antiphase LCO input
* [notebooks/error_correction_model.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/error_correction_model.ipynb)
    * LCOs provide sensory feedback to the VCO layer to correct accumulating errors due to phase noise
* [notebooks/grid_cell_model.ipynb](http://nbviewer.ipython.org/github/jdmonaco/lcomodel/blob/master/notebooks/grid_cell_model.ipynb)
    * Combine VCOs across conditions into grid cell outputs
