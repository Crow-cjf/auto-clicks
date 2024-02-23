# auto-clicks
利用py实现的自动点击函数
rapid_clicks(targets,text=None) 为单次自动点击，可通过text，传入字典实现文字的插入，字典key为第几次点击后添加文本，value为文本内容
images_read(number=30) 为点击目标，需要命名为target+数字+.png格式，数字代表点击顺序
clicks(targets,time=5) cycle_clicks(targets,time=5) 功能类似，实现方法有些区别，均为循环点击，time为循环次数
使用时，导入fun文件后，使用images_read()读入点击目标，接着根据需要调用其他函数，参考3.0文件
