from selfdrive.car import dbc_dict

class CAR:
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  OUTBACK = "SUBARU OUTBACK 2015 - 2017"
  LEGACY = "SUBARU LEGACY 2015 - 2017"


FINGERPRINTS = {
  CAR.IMPREZA: [{
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # Crosstrek 2018 (same platform as Impreza)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  }],
  # OUTBACK PREMIUM 2.5i 2015
  CAR.OUTBACK: [{
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  },
  # OUTBACK PREMIUM 3.6r 2015
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1779: 8, 1786:5
  }],
  #LEGACY LIMITED 2.5i 2015
  CAR.LEGACY: [{
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5
  },
  #LEGACY 2.5i 2017
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  },
  #LEGACY 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1778: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  }],
}

STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
  CAR.OUTBACK: 600,
  CAR.LEGACY: 600,
}

class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [290, 356],   # steer torque cmd
}

DBC = {
  CAR.IMPREZA: dbc_dict('subaru_global_2017', None),
  CAR.OUTBACK: dbc_dict('subaru_outback_2015_eyesight', None),
  CAR.LEGACY: dbc_dict('subaru_outback_2015_eyesight', None),
}
