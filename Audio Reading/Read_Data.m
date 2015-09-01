[filename,pathname] = uigetfile('*.mp3','What audio file would you like to open?');
file = strcat(pathname,filename);

[y,Fs] = audioread(file);
player = audioplayer(y,Fs);

disp(y(:,1:10));

%play(player);

%plot(fft(y));
