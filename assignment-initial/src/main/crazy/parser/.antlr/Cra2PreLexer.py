# Generated from c://Users//hp450//Desktop//assignment2-initial//src//main//crazy//parser//Cra2Pre.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,56,486,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,
        1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,
        1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,
        1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,
        1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,46,1,46,1,47,
        1,47,1,48,1,48,1,49,1,49,5,49,331,8,49,10,49,12,49,334,9,49,1,49,
        3,49,337,8,49,1,50,1,50,5,50,341,8,50,10,50,12,50,344,9,50,1,50,
        1,50,3,50,348,8,50,1,51,1,51,1,51,3,51,353,8,51,1,51,4,51,356,8,
        51,11,51,12,51,357,1,52,1,52,1,52,1,52,3,52,364,8,52,1,53,1,53,1,
        53,1,54,1,54,5,54,371,8,54,10,54,12,54,374,9,54,1,54,3,54,377,8,
        54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,
        55,1,55,3,55,393,8,55,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,
        56,3,56,404,8,56,1,57,1,57,5,57,408,8,57,10,57,12,57,411,9,57,1,
        57,1,57,1,57,1,58,1,58,1,58,1,58,5,58,420,8,58,10,58,12,58,423,9,
        58,1,59,1,59,1,59,1,59,5,59,429,8,59,10,59,12,59,432,9,59,1,59,1,
        59,1,60,1,60,1,60,1,60,5,60,440,8,60,10,60,12,60,443,9,60,1,60,1,
        60,1,60,1,60,1,60,1,61,4,61,451,8,61,11,61,12,61,452,1,61,1,61,1,
        62,1,62,1,62,1,63,1,63,5,63,462,8,63,10,63,12,63,465,9,63,1,63,1,
        63,1,63,3,63,470,8,63,1,63,1,63,1,64,1,64,1,64,1,65,1,65,5,65,479,
        8,65,10,65,12,65,482,9,65,1,65,1,65,1,65,1,441,0,66,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,
        53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,
        75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,0,93,0,95,0,97,
        0,99,0,101,0,103,0,105,0,107,0,109,46,111,47,113,48,115,49,117,50,
        119,51,121,52,123,53,125,54,127,55,129,0,131,56,1,0,11,1,0,48,57,
        1,0,49,57,1,0,97,122,1,0,65,90,2,0,69,69,101,101,3,0,9,10,39,39,
        92,92,1,0,39,39,3,0,92,92,110,110,116,116,1,0,10,10,3,0,9,10,13,
        13,32,32,1,1,10,10,501,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,
        1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,
        0,125,1,0,0,0,0,127,1,0,0,0,0,131,1,0,0,0,1,133,1,0,0,0,3,141,1,
        0,0,0,5,145,1,0,0,0,7,151,1,0,0,0,9,155,1,0,0,0,11,163,1,0,0,0,13,
        171,1,0,0,0,15,176,1,0,0,0,17,183,1,0,0,0,19,189,1,0,0,0,21,193,
        1,0,0,0,23,202,1,0,0,0,25,205,1,0,0,0,27,210,1,0,0,0,29,216,1,0,
        0,0,31,220,1,0,0,0,33,229,1,0,0,0,35,232,1,0,0,0,37,235,1,0,0,0,
        39,238,1,0,0,0,41,243,1,0,0,0,43,253,1,0,0,0,45,259,1,0,0,0,47,264,
        1,0,0,0,49,268,1,0,0,0,51,274,1,0,0,0,53,278,1,0,0,0,55,281,1,0,
        0,0,57,283,1,0,0,0,59,286,1,0,0,0,61,288,1,0,0,0,63,290,1,0,0,0,
        65,292,1,0,0,0,67,294,1,0,0,0,69,296,1,0,0,0,71,298,1,0,0,0,73,300,
        1,0,0,0,75,302,1,0,0,0,77,304,1,0,0,0,79,306,1,0,0,0,81,308,1,0,
        0,0,83,310,1,0,0,0,85,312,1,0,0,0,87,314,1,0,0,0,89,317,1,0,0,0,
        91,320,1,0,0,0,93,322,1,0,0,0,95,324,1,0,0,0,97,326,1,0,0,0,99,336,
        1,0,0,0,101,338,1,0,0,0,103,349,1,0,0,0,105,363,1,0,0,0,107,365,
        1,0,0,0,109,376,1,0,0,0,111,392,1,0,0,0,113,403,1,0,0,0,115,405,
        1,0,0,0,117,415,1,0,0,0,119,424,1,0,0,0,121,435,1,0,0,0,123,450,
        1,0,0,0,125,456,1,0,0,0,127,459,1,0,0,0,129,473,1,0,0,0,131,476,
        1,0,0,0,133,134,5,112,0,0,134,135,5,114,0,0,135,136,5,111,0,0,136,
        137,5,103,0,0,137,138,5,114,0,0,138,139,5,97,0,0,139,140,5,109,0,
        0,140,2,1,0,0,0,141,142,5,118,0,0,142,143,5,97,0,0,143,144,5,114,
        0,0,144,4,1,0,0,0,145,146,5,98,0,0,146,147,5,101,0,0,147,148,5,103,
        0,0,148,149,5,105,0,0,149,150,5,110,0,0,150,6,1,0,0,0,151,152,5,
        101,0,0,152,153,5,110,0,0,153,154,5,100,0,0,154,8,1,0,0,0,155,156,
        5,98,0,0,156,157,5,111,0,0,157,158,5,111,0,0,158,159,5,108,0,0,159,
        160,5,101,0,0,160,161,5,97,0,0,161,162,5,110,0,0,162,10,1,0,0,0,
        163,164,5,105,0,0,164,165,5,110,0,0,165,166,5,116,0,0,166,167,5,
        101,0,0,167,168,5,103,0,0,168,169,5,101,0,0,169,170,5,114,0,0,170,
        12,1,0,0,0,171,172,5,114,0,0,172,173,5,101,0,0,173,174,5,97,0,0,
        174,175,5,108,0,0,175,14,1,0,0,0,176,177,5,115,0,0,177,178,5,116,
        0,0,178,179,5,114,0,0,179,180,5,105,0,0,180,181,5,110,0,0,181,182,
        5,103,0,0,182,16,1,0,0,0,183,184,5,99,0,0,184,185,5,111,0,0,185,
        186,5,110,0,0,186,187,5,115,0,0,187,188,5,116,0,0,188,18,1,0,0,0,
        189,190,5,97,0,0,190,191,5,110,0,0,191,192,5,100,0,0,192,20,1,0,
        0,0,193,194,5,99,0,0,194,195,5,111,0,0,195,196,5,110,0,0,196,197,
        5,116,0,0,197,198,5,105,0,0,198,199,5,110,0,0,199,200,5,117,0,0,
        200,201,5,101,0,0,201,22,1,0,0,0,202,203,5,111,0,0,203,204,5,102,
        0,0,204,24,1,0,0,0,205,206,5,116,0,0,206,207,5,104,0,0,207,208,5,
        101,0,0,208,209,5,110,0,0,209,26,1,0,0,0,210,211,5,97,0,0,211,212,
        5,114,0,0,212,213,5,114,0,0,213,214,5,97,0,0,214,215,5,121,0,0,215,
        28,1,0,0,0,216,217,5,100,0,0,217,218,5,105,0,0,218,219,5,118,0,0,
        219,30,1,0,0,0,220,221,5,102,0,0,221,222,5,117,0,0,222,223,5,110,
        0,0,223,224,5,99,0,0,224,225,5,116,0,0,225,226,5,105,0,0,226,227,
        5,111,0,0,227,228,5,110,0,0,228,32,1,0,0,0,229,230,5,111,0,0,230,
        231,5,114,0,0,231,34,1,0,0,0,232,233,5,100,0,0,233,234,5,111,0,0,
        234,36,1,0,0,0,235,236,5,105,0,0,236,237,5,102,0,0,237,38,1,0,0,
        0,238,239,5,108,0,0,239,240,5,111,0,0,240,241,5,111,0,0,241,242,
        5,112,0,0,242,40,1,0,0,0,243,244,5,112,0,0,244,245,5,114,0,0,245,
        246,5,111,0,0,246,247,5,99,0,0,247,248,5,101,0,0,248,249,5,100,0,
        0,249,250,5,117,0,0,250,251,5,114,0,0,251,252,5,101,0,0,252,42,1,
        0,0,0,253,254,5,98,0,0,254,255,5,114,0,0,255,256,5,101,0,0,256,257,
        5,97,0,0,257,258,5,107,0,0,258,44,1,0,0,0,259,260,5,101,0,0,260,
        261,5,108,0,0,261,262,5,115,0,0,262,263,5,101,0,0,263,46,1,0,0,0,
        264,265,5,109,0,0,265,266,5,111,0,0,266,267,5,100,0,0,267,48,1,0,
        0,0,268,269,5,119,0,0,269,270,5,104,0,0,270,271,5,105,0,0,271,272,
        5,108,0,0,272,273,5,101,0,0,273,50,1,0,0,0,274,275,5,110,0,0,275,
        276,5,111,0,0,276,277,5,116,0,0,277,52,1,0,0,0,278,279,5,58,0,0,
        279,280,5,61,0,0,280,54,1,0,0,0,281,282,5,61,0,0,282,56,1,0,0,0,
        283,284,5,60,0,0,284,285,5,62,0,0,285,58,1,0,0,0,286,287,5,46,0,
        0,287,60,1,0,0,0,288,289,5,44,0,0,289,62,1,0,0,0,290,291,5,59,0,
        0,291,64,1,0,0,0,292,293,5,58,0,0,293,66,1,0,0,0,294,295,5,91,0,
        0,295,68,1,0,0,0,296,297,5,93,0,0,297,70,1,0,0,0,298,299,5,40,0,
        0,299,72,1,0,0,0,300,301,5,41,0,0,301,74,1,0,0,0,302,303,5,43,0,
        0,303,76,1,0,0,0,304,305,5,45,0,0,305,78,1,0,0,0,306,307,5,42,0,
        0,307,80,1,0,0,0,308,309,5,47,0,0,309,82,1,0,0,0,310,311,5,60,0,
        0,311,84,1,0,0,0,312,313,5,62,0,0,313,86,1,0,0,0,314,315,5,60,0,
        0,315,316,5,61,0,0,316,88,1,0,0,0,317,318,5,62,0,0,318,319,5,61,
        0,0,319,90,1,0,0,0,320,321,7,0,0,0,321,92,1,0,0,0,322,323,7,1,0,
        0,323,94,1,0,0,0,324,325,7,2,0,0,325,96,1,0,0,0,326,327,7,3,0,0,
        327,98,1,0,0,0,328,332,3,93,46,0,329,331,3,91,45,0,330,329,1,0,0,
        0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,337,1,0,0,
        0,334,332,1,0,0,0,335,337,5,48,0,0,336,328,1,0,0,0,336,335,1,0,0,
        0,337,100,1,0,0,0,338,347,5,46,0,0,339,341,3,91,45,0,340,339,1,0,
        0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,345,1,0,
        0,0,344,342,1,0,0,0,345,348,3,93,46,0,346,348,5,48,0,0,347,342,1,
        0,0,0,347,346,1,0,0,0,348,102,1,0,0,0,349,352,7,4,0,0,350,353,5,
        45,0,0,351,353,1,0,0,0,352,350,1,0,0,0,352,351,1,0,0,0,352,353,1,
        0,0,0,353,355,1,0,0,0,354,356,3,91,45,0,355,354,1,0,0,0,356,357,
        1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,104,1,0,0,0,359,364,
        8,5,0,0,360,364,3,107,53,0,361,362,7,6,0,0,362,364,7,6,0,0,363,359,
        1,0,0,0,363,360,1,0,0,0,363,361,1,0,0,0,364,106,1,0,0,0,365,366,
        5,92,0,0,366,367,7,7,0,0,367,108,1,0,0,0,368,372,3,93,46,0,369,371,
        3,91,45,0,370,369,1,0,0,0,371,374,1,0,0,0,372,370,1,0,0,0,372,373,
        1,0,0,0,373,377,1,0,0,0,374,372,1,0,0,0,375,377,5,48,0,0,376,368,
        1,0,0,0,376,375,1,0,0,0,377,110,1,0,0,0,378,379,3,99,49,0,379,380,
        3,101,50,0,380,381,3,103,51,0,381,393,1,0,0,0,382,383,3,99,49,0,
        383,384,3,101,50,0,384,393,1,0,0,0,385,386,3,99,49,0,386,387,3,103,
        51,0,387,393,1,0,0,0,388,389,3,101,50,0,389,390,3,103,51,0,390,393,
        1,0,0,0,391,393,3,101,50,0,392,378,1,0,0,0,392,382,1,0,0,0,392,385,
        1,0,0,0,392,388,1,0,0,0,392,391,1,0,0,0,393,112,1,0,0,0,394,395,
        5,116,0,0,395,396,5,114,0,0,396,397,5,117,0,0,397,404,5,101,0,0,
        398,399,5,102,0,0,399,400,5,97,0,0,400,401,5,108,0,0,401,402,5,115,
        0,0,402,404,5,101,0,0,403,394,1,0,0,0,403,398,1,0,0,0,404,114,1,
        0,0,0,405,409,7,6,0,0,406,408,3,105,52,0,407,406,1,0,0,0,408,411,
        1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,412,1,0,0,0,411,409,
        1,0,0,0,412,413,7,6,0,0,413,414,6,57,0,0,414,116,1,0,0,0,415,421,
        3,95,47,0,416,420,3,95,47,0,417,420,3,97,48,0,418,420,3,91,45,0,
        419,416,1,0,0,0,419,417,1,0,0,0,419,418,1,0,0,0,420,423,1,0,0,0,
        421,419,1,0,0,0,421,422,1,0,0,0,422,118,1,0,0,0,423,421,1,0,0,0,
        424,425,5,47,0,0,425,426,5,47,0,0,426,430,1,0,0,0,427,429,8,8,0,
        0,428,427,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,0,430,431,1,0,0,
        0,431,433,1,0,0,0,432,430,1,0,0,0,433,434,6,59,1,0,434,120,1,0,0,
        0,435,436,5,47,0,0,436,437,5,42,0,0,437,441,1,0,0,0,438,440,9,0,
        0,0,439,438,1,0,0,0,440,443,1,0,0,0,441,442,1,0,0,0,441,439,1,0,
        0,0,442,444,1,0,0,0,443,441,1,0,0,0,444,445,5,42,0,0,445,446,5,47,
        0,0,446,447,1,0,0,0,447,448,6,60,1,0,448,122,1,0,0,0,449,451,7,9,
        0,0,450,449,1,0,0,0,451,452,1,0,0,0,452,450,1,0,0,0,452,453,1,0,
        0,0,453,454,1,0,0,0,454,455,6,61,1,0,455,124,1,0,0,0,456,457,9,0,
        0,0,457,458,6,62,2,0,458,126,1,0,0,0,459,463,7,6,0,0,460,462,3,105,
        52,0,461,460,1,0,0,0,462,465,1,0,0,0,463,461,1,0,0,0,463,464,1,0,
        0,0,464,469,1,0,0,0,465,463,1,0,0,0,466,467,5,13,0,0,467,470,5,10,
        0,0,468,470,7,10,0,0,469,466,1,0,0,0,469,468,1,0,0,0,470,471,1,0,
        0,0,471,472,6,63,3,0,472,128,1,0,0,0,473,474,5,92,0,0,474,475,8,
        7,0,0,475,130,1,0,0,0,476,480,7,6,0,0,477,479,3,105,52,0,478,477,
        1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,481,1,0,0,0,481,483,
        1,0,0,0,482,480,1,0,0,0,483,484,3,129,64,0,484,485,6,65,4,0,485,
        132,1,0,0,0,21,0,332,336,342,347,352,357,363,372,376,392,403,409,
        419,421,430,441,452,463,469,480,5,1,57,0,6,0,0,1,62,1,1,63,2,1,65,
        3
    ]

class Cra2PreLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM = 1
    VAR = 2
    BEGIN = 3
    END = 4
    BOOLEAN = 5
    INTEGER = 6
    REAL = 7
    STRING = 8
    CONST = 9
    AND = 10
    CONTINUE = 11
    OF = 12
    THEN = 13
    ARRAY = 14
    DIV = 15
    FUNCTION = 16
    OR = 17
    DO = 18
    IF = 19
    LOOP = 20
    PROCEDURE = 21
    BREAK = 22
    ELSE = 23
    MOD = 24
    WHILE = 25
    NOT = 26
    ASSOPE = 27
    EQUAL = 28
    DIFF = 29
    DOT = 30
    COMMA = 31
    SEMICOLON = 32
    COLON = 33
    LS = 34
    RS = 35
    LR = 36
    RR = 37
    ADD = 38
    SUB = 39
    MUL = 40
    DIVV = 41
    LESS = 42
    GREATER = 43
    LE = 44
    GE = 45
    INTEGER_LIT = 46
    REAL_LIT = 47
    BOOLEAN_LIT = 48
    STRING_LIT = 49
    ID = 50
    LINE_COMMENT = 51
    BLOCK_COMMENT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'program'", "'var'", "'begin'", "'end'", "'boolean'", "'integer'", 
            "'real'", "'string'", "'const'", "'and'", "'continue'", "'of'", 
            "'then'", "'array'", "'div'", "'function'", "'or'", "'do'", 
            "'if'", "'loop'", "'procedure'", "'break'", "'else'", "'mod'", 
            "'while'", "'not'", "':='", "'='", "'<>'", "'.'", "','", "';'", 
            "':'", "'['", "']'", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
            "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "VAR", "BEGIN", "END", "BOOLEAN", "INTEGER", "REAL", 
            "STRING", "CONST", "AND", "CONTINUE", "OF", "THEN", "ARRAY", 
            "DIV", "FUNCTION", "OR", "DO", "IF", "LOOP", "PROCEDURE", "BREAK", 
            "ELSE", "MOD", "WHILE", "NOT", "ASSOPE", "EQUAL", "DIFF", "DOT", 
            "COMMA", "SEMICOLON", "COLON", "LS", "RS", "LR", "RR", "ADD", 
            "SUB", "MUL", "DIVV", "LESS", "GREATER", "LE", "GE", "INTEGER_LIT", 
            "REAL_LIT", "BOOLEAN_LIT", "STRING_LIT", "ID", "LINE_COMMENT", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "PROGRAM", "VAR", "BEGIN", "END", "BOOLEAN", "INTEGER", 
                  "REAL", "STRING", "CONST", "AND", "CONTINUE", "OF", "THEN", 
                  "ARRAY", "DIV", "FUNCTION", "OR", "DO", "IF", "LOOP", 
                  "PROCEDURE", "BREAK", "ELSE", "MOD", "WHILE", "NOT", "ASSOPE", 
                  "EQUAL", "DIFF", "DOT", "COMMA", "SEMICOLON", "COLON", 
                  "LS", "RS", "LR", "RR", "ADD", "SUB", "MUL", "DIVV", "LESS", 
                  "GREATER", "LE", "GE", "DIGIT", "DIGIT_S", "LOWER_CHAR", 
                  "UPPER_CHAR", "INT_PART", "FRAC_PART", "EX_PART", "STRING_CHAR", 
                  "ESCSEQ", "INTEGER_LIT", "REAL_LIT", "BOOLEAN_LIT", "STRING_LIT", 
                  "ID", "LINE_COMMENT", "BLOCK_COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCSEQ", "ILLEGAL_ESCAPE" ]

    grammarFileName = "Cra2Pre.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.STRING_LIT_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if (len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
                      raise UncloseString(self.text[0:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[0:-1])
            	else:
                      raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[0:])
     


