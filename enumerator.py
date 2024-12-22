import requests

def obtener_usuarios_wordpress(dominio):
    try:
        
        url = f"{dominio}/wp-json/wp/v2/users"
        
       
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            usuarios = respuesta.json()
            if usuarios:
                print("Usuarios encontrados:")
                for usuario in usuarios:
                    print(f"- Nombre: {usuario.get('name', 'N/A')} | Username: {usuario.get('slug', 'N/A')}")
            else:
                print("No se encontraron usuarios en este dominio.")
        else:
            print(f"Error al intentar acceder al dominio. Código de estado: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

if __name__ == "__main__":
    dominio = input("Introduce el dominio de WordPress (ejemplo: https://rafaroca.com): ")
    obtener_usuarios_wordpress(dominio)
