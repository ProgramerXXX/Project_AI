clc 
close all 
img = imread('man21.jpg');
faceDetector = vision.CascadeObjectDetector;
bbox = step(faceDetector,img);


if ~isempty(bbox)
    bbox = bbox(1,:);
    rectangle('Position',bbox,'edgecolor','b','LineWidth',5);
    FaceCropped = imcrop(img,bbox);
    
end 

face_Resized = imresize(FaceCropped,[227 227]);
[YPred,scores] = classify(myNet,face_Resized);

a = nominal(YPred);
pred_str = cellstr(a);
position = [0,0];
box_color = {'red'};
RGB = insertText(img,position,pred_str,'FontSize',18,'BoxColor',...
    box_color,'BoxOpacity',0.4,'TextColor','Black');
 imshow(RGB);

rectangle('Position',bbox,'edgecolor','b','LineWidth',5);