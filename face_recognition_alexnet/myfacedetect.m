%สร้างฟังก์ชั่นขึ้นมา เพื่อเรียกใช้งาน CascadeObjectDetector
%ซึ่งมันจะสามารถช่ยเราหาใบหน้าในภาพได้ 

function [CroppedImage , bboxPoints] = myfacedetect(Img)
faceDetector = vision.CascadeObjectDetector;
faceDetector.MergeThreshold = 10;
bboxes = faceDetector(Img);

% หากพบภาพ ให้ทำการ ขยายกรอบของการ detect ออกไปอีก เนื่องจากเรารู้สึกว่า
% model มัน detect ภาพหน้าค่อนข้างแคบเกินไป 
if ~isempty(bboxes)
    bboxes(1,1) = bboxes(1,1)-50;
    bboxes(1,2) = bboxes(1,2)-50;
    bboxes(1,3) = bboxes(1,3)+100;
    bboxes(1,4) = bboxes(1,4)+100;
    
    %ครอปภาพ 
    CroppedImage = imcrop(Img,bboxes);
    %จดจำมุมทั้งสี่จุดของกรอบภาพที่ครอปมา
    bboxPoints = bbox2points(bboxes(1,:));
else 
    CroppedImage = [];
    bboxPoints = [];
end 

