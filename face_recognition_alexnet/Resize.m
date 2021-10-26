clc ;
close all;
clear all ;

%สร้างโฟลเดอร์ไหม่
mkdir('modified_images');
dd = dir('*.png');

%วนลูปให้ครบทุกไฟล์ใน Folder พร้อมแปลงขนาดให้เท่ากันคือ 227x227x3
for cntr = 1:length(dd)
    img = imread(dd(cntr).name);
    imgresized = imresize(img,[227 227]); %gray image 227x227
   %imgreszed_RGB = cat(3,imgresized,imgresized,imgresized); %gray image 227x227x3
    imwrite(imgresized,['modified_images\',dd(cntr).name]);
end 
