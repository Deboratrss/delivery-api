# delivery-api
## Installing
*First we need to configure Python development environments and install dependencies :*
```ruby
$ pip install -r requirements.txt
```
 
 *How to run*
 ```
 $ python3 routes.py
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```
  ## Instructions for development
  
  *Now let's create a complete CRUD (create, read, update and delete) for the database connection.The application has endpoints
for creating, updating, deleting and querying orders.*
  
  ###### GET
*This method ```get_pedidos() ``` returns all requests from the database:*
```ruby
@app.route('/')
def get_pedidos():
```
  
  ###### POST
  *The method ``` add_pedido() ``` adds orders:*
  
   ```ruby
@app.route('/add', methods=["POST"])
def add_pedido():
    pedido = request.get_json()
   ```
   ```
{
    "cliente": "felipe",
    "produto": "camarão internacional",
    "valor": "139.98"   
}
```
  ###### PUT

  *The method ``` edit_pedidos(id) ``` edit orders:*
  
  ```ruby
@app.route('/edit/<id>', methods=['PUT'])
def edit_pedidos(id):
    pedido_alterado = request.get_json()
  ```
  ```
{
    "cliente": "felipe",
    "produto": "camarão internacional",
    "valor": "139.98"    
}
  ```
  
  ###### DELETE 
  *The method ``` delete_pedidos(id) ``` delete orders:*
  
 ``` ruby
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_pedidos(id):
  ```
  
  ## links
  
###### Documentation
  - https://flask.palletsprojects.com/en/2.0.x/api/?highlight=delete#application-object
  - https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-pt
  - https://pip.pypa.io/en/stable/user_guide/#requirements-files
