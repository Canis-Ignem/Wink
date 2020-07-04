from detecto import core, utils
from torchvision import transforms

model = core.Model(['Palm','Peace','Fist'])


utils.xml_to_csv('DataLabels/', 'train_labels.csv')
utils.xml_to_csv('ValLabels/', 'val_labels.csv')

custom_transforms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize(800),
    transforms.ColorJitter(saturation=0.3),
    transforms.ToTensor(),
    utils.normalize_transform(),
])

#Training Dataset after
#dataset = core.Dataset('Data/')
dataset = core.Dataset('train_labels.csv','Data/',transform=custom_transforms)

loader = core.DataLoader(dataset, batch_size = 2, shuffle = True)

#Validation Dataset
val_dataset = core.Dataset('val_labels.csv','ValData/')


#Fitting the model in a custom manner
losses = model.fit(loader, val_dataset, epochs=5,
                   learning_rate=0.001, verbose=True)

model.save('Gestures5.pth')