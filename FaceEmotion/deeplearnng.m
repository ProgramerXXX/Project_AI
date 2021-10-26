
%% Load Training Images
allImages = imageDatastore('test', 'IncludeSubfolders', true,...
    'LabelSource', 'foldernames');


%% Split data into training and test sets 
[trainingImages, testImages] = splitEachLabel(allImages, 0.8, 'randomize');
 
%% Load Pre-trained Network (AlexNet)
alex = alexnet; 

%% Review Network Architecture 
layers = alex.Layers 

%% Modify Pre-trained Network 
% recognize just 4 classes. 
layers(23) = fullyConnectedLayer(4); 
layers(25) = classificationLayer

%% Perform Transfer Learning
opts = trainingOptions('sgdm', 'InitialLearnRate', 0.001,...
    'MaxEpochs', 20, 'MiniBatchSize', 64);

%% Set custom read function 
trainingImages.ReadFcn = @readFunctionTrain;

%% Train the Network 
myNet = trainNetwork(trainingImages, layers, opts);
save AlexNe.mat

%% Test Network Performance
testImages.ReadFcn = @readFunctionTrain;
predictedLabels = classify(myNet, testImages); 
accuracy = mean(predictedLabels == testImages.Labels)

