from detecto import core, utils

model = core.Model(['One','Peace'])

dataset = core.Dataset('Data/')
loader = core.DataLoader(dataset, batch_size = 2, shuffle = True)

val_dataset = core.Dataset('valData/')

losses = model.fit(loader,val_dataset,epochs= 5)

model.save('Gestures2.pth')