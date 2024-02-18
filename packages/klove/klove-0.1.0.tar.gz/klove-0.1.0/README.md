
<a class="reference external image-reference" href="https://gitlab.com/benvial/klove/-/releases" target="_blank"><img alt="Release" src="https://img.shields.io/endpoint?url=https://gitlab.com/benvial/klove/-/jobs/artifacts/main/raw/logobadge.json?job=badge&labelColor=c9c9c9"></a> 
<a class="reference external image-reference" href="https://gitlab.com/benvial/klove/commits/main" target="_blank"><img alt="Release" src="https://img.shields.io/gitlab/pipeline/benvial/klove/main?logo=gitlab&labelColor=dedede&style=for-the-badge"></a> 
<a class="reference external image-reference" href="https://benvial.gitlab.io/klove" target="_blank"><img alt="License" src="https://img.shields.io/badge/documentation-website-dedede.svg?logo=readthedocs&logoColor=e9d672&style=for-the-badge"></a>
<a class="reference external image-reference" href="https://gitlab.com/benvial/klove/commits/main" target="_blank"><img alt="Release" src="https://img.shields.io/gitlab/coverage/benvial/klove/main?logo=python&logoColor=e9d672&style=for-the-badge"></a>
<a class="reference external image-reference" href="https://black.readthedocs.io/en/stable/" target="_blank"><img alt="Release" src="https://img.shields.io/badge/code%20style-black-dedede.svg?logo=python&logoColor=e9d672&style=for-the-badge"></a>
<a class="reference external image-reference" href="https://gitlab.com/benvial/klove/-/blob/main/LICENSE.txt" target="_blank"><img alt="License" src="https://img.shields.io/badge/license-GPLv3-blue?color=aec2ff&logo=open-access&logoColor=aec2ff&style=for-the-badge"></a>


# KLOVE

**Numerical modelling of waves on thin elastic plates**

`klove` is a Python package designed to study wave propagation on thin elastic plates based on the 
Kirchhoff–Love theory. The plate can be loaded with elements that will affect the propagation of elastic waves: the aim 
is to find the solution to this problem numerically. Key features of the code are:


<!-- start elevator-pitch -->

- **Easy to use interface** --- simply define the plate and scatterers (pins, masses, mass-spring or beam resonators).
- **Multiple scattering simulations** --- with plane wave and point load excitation.
- **Far field quantities** --- with plane wave excitation.
- **Diffraction by gratings** --- with calculation of efficiencies.
- **Quasi-normal mode analysis and expansion** --- by solving a nonlinear eigenvalue problem.
- **Calculation of phononic band diagrams** --- with utilities to define the path along the edges of the Brillouin zone.
- **Auto-differentiable** --- allowing for gradient-based optimization of elastic wave propagation.


<!-- end elevator-pitch -->



## Documentation

See the website with API reference and some examples at [benvial.gitlab.io/klove](https://benvial.gitlab.io/klove).



<!-- start installation -->

## Installation


### From Pypi

Simply run

```bash 
pip install klove
```
If you want more numerical backends (pytorch, autograd and jax), including 
auto-differentiation and GPU acceleration, install the full version:

```bash 
pip install klove[full]
```


### From conda/mamba

For the full installation including GPU/autodiff support

```bash 
mamba install -c pytorch -c nvidia pytorch pytorch-cuda=12.1 jaxlib=*=*cuda* jax 
pip install klove[full]
```

<!-- cuda-nvcc ?  -->

### From source

Clone the repository

```bash 
git clone https://gitlab.com/benvial/klove.git
cd klove
```

Install the package locally

```bash 
pip install -e .
```

For the full version:

```bash 
pip install -e .[full]
```

### From gitlab

Basic:

```bash 
pip install -e git+https://gitlab.com/benvial/klove.git#egg=klove
```


Full:

```bash 
pip install -e git+https://gitlab.com/benvial/klove.git#egg=klove[full]
```




<!-- end installation -->