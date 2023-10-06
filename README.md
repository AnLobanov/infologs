# infologs
Collecting information about the ATOL device and fiscal storage expiration date
## How to start
0. Install drivers from [ATOL official file storage](https://fs.atol.ru/)
1. Put libfprt10.py file from drivers folder to script folder
2. Connect your ATOL device to PC through USB
3. Run script
   ```
   python infologs.py
   ```
## How it works
Script tries to connect to ATOL device. If device connected - it gets info and put to log-file IL.log. 1 startup - 1 file - 1 line!
## Log-file format
```
[Serial number];[Registration number];[Expiration date (%d.%m.%Y)]
```
