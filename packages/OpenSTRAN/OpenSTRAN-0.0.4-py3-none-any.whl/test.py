from OpenSTRAN.model import Model

model = Model()

N1 = model.nodes.addNode(0,0,0,'N1')
N2 = model.nodes.addNode(10,0,0,'N2')

N1.restraint = [1,1,1,0,0,0]
N2.restraint = [1,1,1,0,0,0]

M1 = model.members.addMember(N1, N2)

model.loads.addPointLoad(M1, direction='Y', D=-10, location=50)

model.plot()