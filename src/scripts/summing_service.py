#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from system1.msg import sum # импортируем модуль сообщения

def summing_service(msg):
    x1 = msg.x1
    x2 = msg.x2
    msg.sum = msg.x1 + msg.x2
    rospy.loginfo('summing service heard x1 is: %d , x2 is: %d according sum is: %d' % (msg.x1, msg.x2, msg.sum)) # Вывод в терминал
    # информации (содержание сообщения)

rospy.init_node('summing_service') # необходимо зарегистрировать узел в системе ROS
rospy.Subscriber('my_chat_topic1', sum, summing_service, queue_size=10) # зарегистрировать топик на подписку
rospy.spin() # будет удерживать программу рабочей до тех пор, пока ROS не завершится или узел не бует прерван