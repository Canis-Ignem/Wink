from detecto import core, utils

model = core.Model(['One','Peace'])

dataset = core.Dataset('Data/')
#loader = core.DataLoader(dataset, batch_size = 2, shuffle = True)

val_dataset = core.Dataset('valData/')

losses = model.fit(dataset,val_dataset)

model.save('Gestures4.pth')