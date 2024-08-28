from flask import Blueprint, request, jsonify, session
import requests
from orders.models.order_model import Orders
from db.db import db
from datetime import timedelta


order_controller = Blueprint('order_controller', __name__)


@order_controller.route('/api/orders', methods=['GET'])
def get_all_orders():
    print("listado de ordenes")
    orders = Orders.query.all()
    result = [{'id': order.id, 'userName': order.userName, 'userEmail': order.userEmail, 'saleTotal': order.saleTotal} for order in orders]
    return jsonify(result)

@order_controller.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    print("obteniendo orden")
    order = Orders.query.get_or_404(order_id)
    return jsonify({'id': order.id, 'userName': order.userName, 'userEmail': order.userEmail, 'saleTotal': order.saleTotal})

@order_controller.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_name = session['username']
    user_email = session['email']

    if not user_name or not user_email:
      return jsonify({'message': 'Información de usuario inválida'}), 400
   
    products = data.get('products')

    if not products or not isinstance(products, list):
      return jsonify({'message': 'Falta o es inválida la información de los productos'}), 400
    
    # INSERTAR SU CODIGO AQUI
    # Calcular el total de la venta
    total = 0
    for product in products:
      response = requests.get(f'http://192.168.80.3:5003/api/products/{product["id"]}')
      product_data = response.json()

      if product_data['quantity'] < product['quantity']:
        return jsonify({'message': f'No hay suficiente inventario para el producto {product_data["name"]}'}), 400
      # Verificar el resultado
      total += product_data['price'] * product['quantity']

      # Actualizar el inventario (llamando al endpoint de actualización de Productos)
      product_data['quantity'] -= product['quantity']

      response = requests.put(f'http://192.168.80.3:5003/api/products/{product["id"]}', json=product_data)
      
      if response.status_code == 200:
        print('Actualización exitosa:', response.json())
      else:
        print('Error al actualizar:', response.status_code, response.text)

    # Crear una nueva instancia de Order y guardarla en la base de datos
    new_order = Orders(userName=user_name, userEmail=user_email, saleTotal=total)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Orden creada exitosamente'}), 201
