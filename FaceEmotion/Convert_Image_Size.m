clc 
close all
clear all 

mkdir('modified_images')
dd = dir('*.jpg')

for cntr = 1:length(dd)
    img = imread(dd(cntr).name)
    imgresized = imgresize(img,[227 227]); %gray image 227x227x3
    
end 

figure;imshow(img)