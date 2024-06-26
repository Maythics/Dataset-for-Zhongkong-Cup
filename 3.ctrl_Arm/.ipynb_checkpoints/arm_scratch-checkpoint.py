{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "#coding=utf-8\n",
    "import time\n",
    "from Arm_Lib import Arm_Device\n",
    "\n",
    "Arm = Arm_Device()\n",
    "time.sleep(.1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Individually control a steering gear to move to a certain angle\n",
    "# 单独控制一个舵机运动到某个角度\n",
    "id = 6\n",
    "\n",
    "Arm.Arm_serial_servo_write(id, 90, 500)\n",
    "time.sleep(1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Control a steering gear cycle switching angle\n",
    "# 控制一个舵机循环切换角度\n",
    "id = 6\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        Arm.Arm_serial_servo_write(id, 120, 500)\n",
    "        time.sleep(1)\n",
    "        Arm.Arm_serial_servo_write(id, 50, 500)\n",
    "        time.sleep(1)\n",
    "        Arm.Arm_serial_servo_write(id, 120, 500)\n",
    "        time.sleep(1)\n",
    "        Arm.Arm_serial_servo_write(id, 180, 500)\n",
    "        time.sleep(1)\n",
    "\n",
    "    \n",
    "try :\n",
    "    main()\n",
    "except KeyboardInterrupt:\n",
    "    print(\" Program closed! \")\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Release arm object \n",
    "# 释放Arm对象\n",
    "del Arm "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
