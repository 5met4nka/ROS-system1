#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from system1.srv import poly, polyResponse # импортируем модуль типа сервиса `Poly` вместе с типом ответа

def handle_request_service(req):
    result = req.x1 + req.x2 ** 2
    rospy.loginfo("Returning [%s + %s^2 = %s]" % (req.x1, req.x2, result))

    resp = polyResponse()
    resp.result = result

    return resp

def poly_service():
    rospy.init_node('poly_service') # инициализация узла
    s = rospy.Service('poly', poly, handle_request_service) # передаем имя сервиса,
    # тип сообщений и функцию обработчика
    rospy.loginfo("Ready to calc.") # вывод в терминал информации
    rospy.spin() # будет удерживать программу рабочей до тех пор,
    # пока ROS не завершится или узел не бует прерван


poly_service() # запускаем этот сервер