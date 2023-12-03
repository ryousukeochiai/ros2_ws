import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self, nh):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        # ↑ selfはオブジェクトのこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
        nh.create_timer(0.5, cb) #ここでタイマーをしかける。

    def cb(self):              #関数内のnやpubをtalkerのものに変更
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker()      #オブジェクトを作成（__init__が実行される。）
rclpy.spin(node)
