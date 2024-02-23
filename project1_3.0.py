import project1_fun as fun

# 参数
time=4
#number=2
#texts={2:'2387315'}

# 循环点击
#fun.cycle_click(time,number)

# 读入点击目标
targets=fun.images_read(number=1)

# 有填充点击或要求快速,text可为空:
fun.rapid_clicks(targets,time)


