import pyautogui

pyautogui.FAILSAFE = True


def skip_ad():
    print("Ad skipper is running...")
    print("To stop the ad skipper, you need to shut the program or press Ctrl+C in the terminal.")
    while True:
        video_ad = pyautogui.locateCenterOnScreen("play.png") # type: ignore

        if video_ad is not None:
            break

    if video_ad is not None:
        pyautogui.click(video_ad)

    skip_ad()


skip_ad()
