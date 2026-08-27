#define MyAppName "JuntarPDFs"
#define MyAppVersion "0.1.1"
#define MyAppPublisher "MarivaldoDev"
#define MyAppExeName "JuntarPDFs.exe"

[Setup]
AppId={{JuntarPDFs}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}

OutputDir=installer
OutputBaseFilename=JuntarPDFs-Setup

SetupIconFile=logo.ico

Compression=lzma
SolidCompression=yes

ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "dist\JuntarPDFs.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Executar {#MyAppName}"; Flags: nowait postinstall skipifsilent
