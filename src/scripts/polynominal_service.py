#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`
import time
import rospy # импортируем основной модуль `rospy`
from system1.msg import sum # импортируем модуль сообщения
from system1.srv import poly, polyRequest, polyResponse

def start_polynominal_service():
    msg = sum()  # создаем объект сообщения
    x1 = 0
    x2 = 0
    while not rospy.is_shutdown():  # бесконечный цикл, пока ROS система работает
        
        # заполнение сообщения
        msg.x1 = x1
        msg.x2 = x2

        data = 'polynominal service send x1: %d / x2: %d' % (msg.x1, msg.x2)

        rospy.loginfo(data)  # вывод в терминал информации (содержание сообщения)
        pub1.publish(msg)  # публикация сообщения в топик

        

        rospy.wait_for_service('request_service')
        try:
            request_service = rospy.ServiceProxy('request_service', poly)  # получаем объект сервиса
            resp = request_service(x1, x2) # получаем объект `polyResponse`

            rospy.loginfo('pesponse by service: %s' % resp.sumFromRequestService)
        except rospy.ServiceException:
            rospy.loginfo("service call failed.")

        x1 += 1
        x2 += 2
        time.sleep(1)
        rospy.Subscriber('my_chat_topic2', sum, polynominal_service, queue_size=10)  # зарегистрировать топик на подписку
        time.sleep(1)
        
def polynominal_service(msg):
    rospy.loginfo('callback from summing_service, sum is %d' % msg.sumFromSummingService) # Вывод в терминал
    # информации (содержание сообщения)
    pub1.publish(msg)

rospy.init_node('polynominal_service') # необходимо зарегистрировать узел в системе ROS
pub1 = rospy.Publisher('my_chat_topic1', sum, queue_size=10) # зарегистрировать топик на публикацию
# с указанием имени, типа сообщения для топика и размера очереди

try:
    start_polynominal_service()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')