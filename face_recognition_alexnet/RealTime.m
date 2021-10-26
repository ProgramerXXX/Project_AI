clc 
close all 

%เปิดกล้อง 
delete(imaqfind)
vid=videoinput('winvideo',1);
triggerconfig(vid,'manual');
set(vid,'FramesPerTrigger',1);
set(vid,'TriggerRepeat',inf);

color_spec = vid.ReturnedColorSpace;

%เซตภาพเป็น rgb
if ~strcmp(color_spec,'rgb');
    set(vid,'ReturnedColorspace','rgb');
end 

%เริ่มเปิกล้องจับภาพและใช้การตรวจจับใบหน้า
start(vid)
faceDetector = vision.CascadeObjectDetector;

%ดึงภาพมาจากวิดีโอ
for ii = 1:600    
    trigger(vid);
    img = getdata(vid,1);    

%วาดภาพสี่เหลี่ยมรอบใบหน้า
bbox = step(faceDetector,img);
if ~isempty(bbox)
    bbox = bbox(1,:);
    rectangle('Position',bbox,'edgecolor','b','LineWidth',5);
    FaceCropped = imcrop(img,bbox);
    
% ทำนายใบหน้า
    face_Resized = imresize(FaceCropped,[227 227]);
    [YPred,scores] = classify(netTransfer, face_Resized);


    a = nominal(YPred);
    pred_str = cellstr(a);
    position = [0,0];
    box_color = {'red'};
    RGB = insertText(img,position,pred_str,'FontSize',18,'BoxColor',...
        box_color,'BoxOpacity',0.4,'TextColor','Black');
   imshow(RGB)

    rectangle('Position',bbox,'edgecolor','b','LineWidth',5);
end
end