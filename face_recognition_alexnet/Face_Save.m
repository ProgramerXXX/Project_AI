%เปิดกล้อง webcam
cam = webcam;
nof = input('Enter NO. of requured frames: ');
count = 1;

%วนลูปตามจำนวนครั้งที่ผู้ใช้กรอกมา 
while count<=nof
    img = snapshot(cam);
    %หากพบภาพ ก็จะทำการครอปโดยการใช้ฟังก์ชั่น myfacedetect ที่เขียนเอาไว้ 
    if ~isempty(img)
    [croppedframe , bboxPoint] = myfacedetect(img);
    imshow(croppedframe);
    end
    
    %หากมีการครอปภาพหน้า จะทำการเซฟรูปไว้ ตามไดรฟ์ที่กำหนด
    if ~isempty(croppedframe)
        filename = strcat('E:\',sprintf('%d.png',count));
        imwrite(croppedframe,filename);
        msg = ['Image Aquired No: ',num2str(count)];
        disp(msg)
        count=count+1;
    %หากไม่พบภาพหรือใบหน้าในภาพให้แสดงข้อความบอกผู้ใช้ 
    else 
        disp('No face Detection')
    end
    %ถ่ายภาพ ด้วยความเร็ว 0.5 วินาทีต่อภาพ
    clf('reset')
    pause(0.5)
end
clear cam;