from src.api.apiHandler import ApiHandler

order = ApiHandler.makeOrder()

print("Pedido criado, id: {}".format(order["order_id"]))

orderConsultada = ApiHandler.getOrder(order["order_id"])

print("Consultando id criado... : {}".format(orderConsultada))

confirmandoPagamento = ApiHandler.webhookApi(order["order_id"])

print("Confirmando pagamento...")

orderConsultadaPgm = ApiHandler.getOrder(order["order_id"])

print("Consultando pedido pago... : {}".format(orderConsultadaPgm))

      
