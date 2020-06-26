from detecto import core, utils

model = core.Model(['One'])

dataset = core.Dataset('frames/')
loader = core.DataLoader(dataset, batch_size = 2, shuffle = True)

val_dataset = core.Dataset('valData/')

losses = model.fit(loader,val_dataset,epochs= 5)

model.save('finger.pth')