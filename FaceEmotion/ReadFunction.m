% Copyright 2017 The MathWorks, Inc.

function I = readFunctionTrain('man.jpg')
% Resize the flowers images to the size required by the network.
I = imread(filename);

I = imresize(I, [227 227]);
