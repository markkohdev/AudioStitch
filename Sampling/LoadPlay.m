function varargout = LoadPlay(varargin)
% LOADPLAY MATLAB code for LoadPlay.fig
%      LOADPLAY, by itself, creates a new LOADPLAY or raises the existing
%      singleton*.
%
%      H = LOADPLAY returns the handle to a new LOADPLAY or the handle to
%      the existing singleton*.
%
%      LOADPLAY('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in LOADPLAY.M with the given input arguments.
%
%      LOADPLAY('Property','Value',...) creates a new LOADPLAY or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before LoadPlay_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to LoadPlay_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help LoadPlay

% Last Modified by GUIDE v2.5 22-Jan-2015 16:45:52

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @LoadPlay_OpeningFcn, ...
                   'gui_OutputFcn',  @LoadPlay_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT



% --- Executes just before LoadPlay is made visible.
function LoadPlay_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to LoadPlay (see VARARGIN)

% Choose default command line output for LoadPlay
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes LoadPlay wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = LoadPlay_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in play_button.
function play_button_Callback(hObject, eventdata, handles)
% hObject    handle to play_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
    play(handles.player);

% --- Executes on button press in stop_button.
function stop_button_Callback(hObject, eventdata, handles)
% hObject    handle to stop_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
    stop(handles.player);


% --- Executes on button press in choose_file_button.
function choose_file_button_Callback(hObject, eventdata, handles)
% hObject    handle to choose_file_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[filename,pathname] = uigetfile({'*.mp3;*.wav','Audio Files (*.mp3, *.wav)'},'What audio file would you like to open?');
file = strcat(pathname,filename);
set(handles.filename,'String',file);
[y,Fs] = audioread(file);
disp(size(y));
handles.player = audioplayer(y,Fs);

% Plot the audio
% We're only gonna take 1000 samples
newY = y(10000:11000,:);
m = length(newY);
n = pow2(nextpow2(m));
y = fft(newY,n);
f = (0:n-1)*(Fs/n)/10;
p = y.*conj(y)/n;

%handles.audio_plot =  plot(20*log10(abs(fftshift(fft(y(10000:10500,:))))));

handles.audio_plot =  plot(f(1:floor(n/2)),p(1:floor(n/2)));
title('{\bf Audio FFT}');
ylabel('Decibels');
xlabel('Frequency (Hz)');

% Update handles structure
guidata(hObject, handles);


function filename_Callback(hObject, eventdata, handles)
% hObject    handle to filename (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of filename as text
%        str2double(get(hObject,'String')) returns contents of filename as a double


% --- Executes during object creation, after setting all properties.
function filename_CreateFcn(hObject, eventdata, handles)
% hObject    handle to filename (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function start_time_Callback(hObject, eventdata, handles)
% hObject    handle to start_time (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of start_time as text
%        str2double(get(hObject,'String')) returns contents of start_time as a double


% --- Executes during object creation, after setting all properties.
function start_time_CreateFcn(hObject, eventdata, handles)
% hObject    handle to start_time (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


function end_sample_Callback(hObject, eventdata, handles)
% hObject    handle to end_sample (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of end_sample as text
%        str2double(get(hObject,'String')) returns contents of end_sample as a double


% --- Executes during object creation, after setting all properties.
function end_sample_CreateFcn(hObject, eventdata, handles)
% hObject    handle to end_sample (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in update_button.
function update_button_Callback(hObject, eventdata, handles)
% hObject    handle to update_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
