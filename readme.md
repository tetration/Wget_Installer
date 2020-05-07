This is a small python3 script to download and simplify the install steps of  EternallyBored's or Cyg32's port of linux wget for Windows


Warning: when running the python script you need to give it administrator privileges otherwise it wont be able to set up the environmment path to the folder where Wget path is located nor be able to install itself on your Windows System32 folder 
In order to do that you can execute cmd or powershell as an admin and then run it through cmd
exampe: py Wget_installer_script.py



Plans for future updates:
    -No need to install Wget on windows system32 anymore. The user will be able to any directory it wants to install my script will be able to create a system or user environmment path(depends on what the user will opt), and then Wget will be acessible from any folders as long as you type wgetlinux
    - User will be able to choose between installing Cygwin32 Wget or EternallyBored's Wget Windows Version 
    - User friendly CUI Menu letting the user pick between Install Wget Cywin32, Install Wget EternallyBored, Unistall Wget, Repair Wget Installation and so on.
    - Detects if installation shall install 32 bit or 64 bit version if user opts for installing EternallyBored's Wget, which is the only version that provides 32 bit and 64 bit executables
    - Update checker



FAQ
What version of Wget for Windows do you provide?
    For now, with my python script you will be able to install Cygwin32's Wget

Why do I have to type wgetlinux instead of wget in the cmd or powershell to use this version of wget? 

Since Windows's powershell uses the command wget as an alias for calling Invoke-WebRequest the solution I found to avoid conflict between Invoke-WebRequest and the Wget we will be installing was to rename it as wgetlinux.



Warning:
The entire risk arising out of the use or performance of   
these python scrips and my documentation remains with you. In no event shall  
I, or anyone else involved in the creation, production, or   
delivery of these python scripts shall be liable for any damages whatsoever (including,  
but not limited to: damages for loss of business profits, business interruption,  
loss of business information, or other pecuniary loss) arising out of the use  
of or inability to use the sample scripts or documentation I have provided, even if Github 
has been advised of the possibility of such damages  