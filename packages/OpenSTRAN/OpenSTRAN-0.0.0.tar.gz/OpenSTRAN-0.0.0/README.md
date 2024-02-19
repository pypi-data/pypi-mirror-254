# OpenSTRAN

OpenSTRAN - Open Source Structural Analysis with Python

## Installation
```
$ pip install OpenSTRAN
```

## Capabilities

OpenStruct allows for the creation of simple two-dimensional frame elements
and complex three-dimensional structures alike.

* 2D truss
* 3D truss
* 2D frame
* 3D space frame
* Interactive diagrams

## Limitations
* First order elastic analysis only.
* Shear and torsional deformations are not considered.

Second order inelastic analysis methods are currently under development.


## Example
Simply supported beam subject to a point load.
```python
import OpenSTRAN

model = OpenSTRAN.Model(plane='xy')

N1 = model.nodes.addNode(0,0,0,'N1')
N2 = model.nodes.addNode(10,0,0,'N2')

N1.restraint([1,1,1,0,0,0])
N2.restraint([1,1,1,0,0,0])

M1 = model.members.addMember(N1, N2)

model.loads.addPointLoad(M1, direction='Y', D=-10, location=50)

model.plot()
```