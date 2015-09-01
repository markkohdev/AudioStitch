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

% Last Modified by GUIDE v2.5 13-Jan-2015 18:07:59

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
[filename,pathname] = uigetfile('*.mp3','What audio file would you like to open?');
file = strcat(pathname,filename);
set(handles.filename,'String',file);
[y,Fs] = audioread(file);
handles.player = audioplayer(y,Fs);
handles.audio_plot = plot(y);

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
