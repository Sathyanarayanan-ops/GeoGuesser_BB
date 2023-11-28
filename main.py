import time

import pyscreenshot as ImageGrab
import schedule


from datetime import datetime


def take_screenshot():
    print("Taking screenshot...")

    image_name = f"Gables-{str(datetime.now())}"
    screenshot = ImageGrab.grab((250,250,1800,1800))

    filepath = f"./Gables/{image_name}.png"

    screenshot.save(filepath)

    print("Screenshot taken...")

    return filepath


def main():
    schedule.every(2).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()