# KBE_chair
## Introduction
 A chair KBE model with a webpage interface.

## Requirement
- Python
- Chrome or other browser
- Siemens NX
- fuseki server: https://jena.apache.org/download/index.cgi

## How to use
1. Run server_chair_zzz.py and manufChecker.py in CMD.
2. Do preparation in Siemens NX.
    2.1. Add "Exercise3-KBE chair" into Knowledge Fusion working folder. (File -> Preference -> KF)
    2.2. Load chair_zzz.dfa in Siemens NX and set a good view for screenshot.
    2.3. Run exportImgFromNX.py in Siemens NX.
3. Make sure the fuseki server is running with a dataset named “kbe”.
4. Open http://127.0.0.1:4321/setParamsIntervals to initialise the range in fuseki server.
5. Open http://127.0.0.1:1234/orderChair to check the UI.
6. Input the wanted value for each parameter or use Load Default.
7. Submit to see if the chair based on the parameter set can be manufactured.
8. The DFA file will be generated automatically, which can be visualized in Siemens NX.
