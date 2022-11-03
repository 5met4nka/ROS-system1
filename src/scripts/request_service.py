#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from study_pkg.srv import Poly, PolyResponse # импортируем модуль типа сервиса `Poly` вместе с типом ответа

def handle_poly_srv(req):
    result = req.x + req.x ** 2
    rospy.loginfo("Returning [%s + %s^2 = %s]" % (req.x, req.x, result))

    resp = PolyResponse()
    resp.y = result

    return resp


def poly_server():
    rospy.init_node('poly_server') # основная инициализация
    s = rospy.Service('poly', Poly, handle_poly_srv) # передаем имя сервиса
    rospy.loginfo("Ready to calc polynomial.") # вывод в терминал информации
    rospy.spin() # будет удерживать программу рабочей до тех пор,
    # пока ROS не завершится или узел не бует прерван


poly_server() # запускаем этот сервер