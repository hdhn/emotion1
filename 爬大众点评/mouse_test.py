import pyautogui,time,random



#print(pyautogui.size())
try:
    while True:#pyautogui.pixelMatchesColor(209,972,(6,184,184))
        im = pyautogui.screenshot()
        x,y = pyautogui.position()
        print(im.getpixel((x,y)))
        positionStr = 'x: ' + str(x).rjust(4) + ' y: '+ str(y).rjust(4)
        print(positionStr)
        #print('\b' * len(positionStr),end = '',flush=True)

        input('\033[33;46m请按enter键继续    \033[0m')
        time.sleep(2)
        # pyautogui.click(215, 1059, button='left')
        # pyautogui.click(131, 45, button='left')
        # pyautogui.moveTo(547, 329, duration=1)
        # pyautogui.dragTo(748, 331, duration=random.randint(1, 2))
except KeyboardInterrupt:
    print('\nDone.')



    #x: 131        x:  209 y:  972
    #y: 45
    # x: 215
    # y: 1059
    # x: 547
    # y: 329
    # x: 748
    # y: 331