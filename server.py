import json
import numpy as np
from .utils import predict_model, reversed_categories
from socketserver import BaseRequestHandler, ThreadingTCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        msg = self.request.recv(1024)
        data = msg.decode()
        predict = predict_model(data)
        order = np.argsort(predict)
        result = {}
        for i in range(6):
            value_index = order[0][-i - 1]
            result[reversed_categories[value_index]] = predict[0][value_index]
        result = dict((str(k), str(v)) for k, v in result.items())
        print(result)
        json_data = json.dumps(result)
        self.request.send(json_data.encode())


if __name__ == '__main__':
    print("Сервер запущен")
    server = ThreadingTCPServer(('', 5000), EchoHandler)
    server.serve_forever()
