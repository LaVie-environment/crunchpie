#!/usr/bin/env python3

import sys, time
import plyte

try:
    while True:
        print('\n' * 60)
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 24)
        if hours == '0':
            hours = '24'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        hDigits = plyte.getSevSegStr(hours, 2)
        hTopRow, hMiddileRow, hBottomRow = hDigits.splitlines()

        mDigits = plyte.getSevSegStr(minutes, 2)
        mTopRow, mMiddileRow, mBottomRow = mDigits.splitlines()

        sDigits = plyte.getSevSegStr(seconds, 2)
        sTopRow, sMiddileRow, sBottomRow = sDigits.splitlines()

        print(hTopRow   + '     ' + mTopRow     + '     ' + sTopRow)
        print(hMiddileRow   + '     *   ' + mMiddileRow +  '    *   ' + sMiddileRow)
        print(hBottomRow    + '     *   ' + mBottomRow +   '   *   ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit. ')

    while True:
        time.sleep(0.01)
        if time.localtime().tm_sec != currentTime.tm_sec:
            break
except KeyboardInterrupt:
    print('Digital clock, modified by Taofeek bellotaophyc@outlook.com')
    sys.exit()