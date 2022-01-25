# ZoomAutoJoiner
A simple program I wrote that autojoins zoom links without having to open the browser.

## Update
Added logging facility to monitor script when running in background. Binaries of the same have been built.

## Usage
Either run the script with `python3 zoomautojoiner.foreground` or `pythonw zoomautojoiner.background` or run the EXE file.
If you are on on a POSIX system use either `python3 zoomautojoiner.foreground` or `sudo nohup python3 zoomautojoiner.foreground` to run in 
background.
Run with `-verbose` argument to show extra information. I use this to see whether the parsing worked correctly.
## Format of `meetings.txt`
`<time in 24hour format> <zoom meeting link>`
## Requirments
Python3 and nothing else alternatively you can natively run this on windows with the binary.The script should work on both windows and POSIX systems. 
## Binaries
.exe (recommended for windows users as it doesnt pause out of focus) binaries are available in the `binaries` folder. The folder also contains the SHA256 and MD5 checksum of the file. Be sure to verify the files before running.
## Notes for noobs
Run the `installdependancy.bat` file before running the script. If it shows a error check your python installation and ensure that 
`pip` is accessible through the shell. If for some reason you are unable to run the script use the binaries provided.
