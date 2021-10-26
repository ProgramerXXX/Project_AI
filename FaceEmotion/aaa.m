clc ;
close all;
clear all ;

mkdir('modified_images');
dd = dir('*.jpg');

for cntr = 1:length(dd)
    img = imread(dd(cntr).name);
    imgresized = imresize(img,[227 227 3]); %gray image 227x227
   %imgreszed_RGB = cat(3,imgresized,imgresized,imgresized); %gray image 227x227x3
    imwrite(imgreszed,['modified_images\',dd(cntr).name]);
end 
