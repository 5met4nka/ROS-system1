#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from system1.msg import sum # импортируем модуль сообщения


def start_polynominal_service():
    msg = sum()  # создаем объект сообщения
    x1 = 0
    x2 = 0
    while not rospy.is_shutdown():  # бесконечный цикл, пока ROS система работает

        data = 'x1: %d / x2: %d' % (msg.x1, msg.x2)

        rospy.loginfo(data)  # вывод в терминал информации (содержание сообщения)
        pub.publish(msg)  # публикация сообщения в топик

        x1 += 2
        x2 += 4

        # заполнение сообщения
        msg.x1 = x1
        msg.x2 = x2

        rate.sleep()  # сон в соответствии с выдерживаемой частотой

rospy.init_node('polynominal_service') # необходимо зарегистрировать узел в системе ROS
pub = rospy.Publisher('my_chat_topic1', sum, queue_size=10) # зарегистрировать топик на публикацию
# с указанием имени, типа сообщения для топика и размера очереди
rate = rospy.Rate(1) # используется для выдерживания частоты выполнения кода, Гц

try:
    start_polynominal_service()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')