[Setup]
AppName=KoeScribe AI
AppVersion=1.0
AppPublisher=Weslley Harakawa
AppPublisherURL=https://github.com/weslleyharakawa
AppSupportURL=https://github.com/weslleyharakawa
AppUpdatesURL=https://github.com/weslleyharakawa
DefaultDirName={autopf}\KoeScribe AI
DefaultGroupName=KoeScribe AI
AllowNoIcons=yes
OutputDir=C:\Users\HarakawaTech\Desktop\KoeScribe_AI_Projeto
OutputBaseFilename=KoeScribe_AI_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=
UninstallDisplayName=KoeScribe AI
UninstallDisplayIcon={app}\KoeScribe AI.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "startupicon"; Description: "Start KoeScribe AI automatically with Windows"; GroupDescription: "Startup:";

[Files]
Source: "dist\KoeScribe AI.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\KoeScribe AI"; Filename: "{app}\KoeScribe AI.exe"
Name: "{group}\Uninstall KoeScribe AI"; Filename: "{uninstallexe}"
Name: "{commondesktop}\KoeScribe AI"; Filename: "{app}\KoeScribe AI.exe"; Tasks: desktopicon
Name: "{userstartup}\KoeScribe AI"; Filename: "{app}\KoeScribe AI.exe"; Tasks: startupicon

[Run]
Filename: "{app}\KoeScribe AI.exe"; Description: "{cm:LaunchProgram,KoeScribe AI}"; Flags: nowait postinstall skipifsilent

[Code]
procedure InitializeWizard;
begin
  WizardForm.Caption := 'KoeScribe AI - Setup Wizard';
end;
