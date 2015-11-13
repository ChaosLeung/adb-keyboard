# adb-keyboard

adb 键盘小工具，单纯为了能够直接使用电脑的键盘控制设备键盘

目前并不知道怎么获取 adb shell 执行后得到的 shell，所以程序效率较低

## 支持的按键
* 非编辑模式下：数字，字母，回车，Del，Home，上下左右
* 编辑模式下：所有可视字符

## 部分特殊按键

* CTRL + E: 进入编辑模式，该模式下执行的命令为 `adb shell input text <string>`，默认非编辑模式，执行的命令为 `adb shell input keyevent <keycode>`
* CTRL + W: 对应 UP 按钮
* CTRL + X: 对应 DOWN 按钮
* CTRL + A: 对应 LEFT 按钮
* CTRL + D: 对应 RIGHT 按钮
* CTRL + B: 对应 ESC 按钮
* CTRL + H: 对应 Android HOME 按钮