import random  #biblioteca para generar productos randoms

class Producto:
    ids = 1  # variable para generar los id empezando desde el 1

    def __init__(self, nombre, precio, categoria, stock, rating):
        self.id = Producto.ids
        Producto.ids += 1

        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.rating = rating

    def __str__(self):
        return(
            f"ID: {self.id}, Nombre: {self.nombre}, "
            f"Precio: ${self.precio:.2f}, Categoria: {self.categoria}, "
            f"Stock: {self.stock}, Calificacion: {self.rating:.2f}"
        )
    

def GProductos(num = 50):
        categoria = ["televisores","tablets","laptops","barras de sonido",
                     "power banks","teclados","mouse","webcams","unidades USB",
                     "routers","escáneres","tóner","camaras"]
        base = [
            "Samsung","LG","Sony","Philips","Panasonic","TCL","Hisense",
            "Apple","Xiaomi","Huawei","OnePlus","Google","Nokia",
            "Acer","Asus","HP","Dell","Lenovo","MSI","Razer",
            "Corsair","Logitech","Anker","Bose","JBL","Canon","Nikon",
            "GoPro","Seagate","WesternDigital","Kingston","SanDisk","TP-Link","Netgear"
        ]
        randoms = [
            "Pro","Pro Max","Ultra","Mini","Plus","S","X","G",
            "4K","8K","OLED","QLED","HDR","Smart","Gaming","Wireless",
            "Bluetooth","NoiseCancel","RGB","RTX 4070","RTX 4080","i7","i5",
            "Ryzen 5","Ryzen 7","16GB","32GB","64GB","1TB","512GB",
            "AX3000","AC1200","Action","Hero","Studio","Max 2025","TV 55","TV 65"
        ]

        productos = []

        for _ in range(num):
            nombre = random.choice(base) + "-" + random.choice(randoms)
            precio = random.uniform(1.0,1499.99)
            categoria = random.choice(categoria)
            stock = random.randint(1,100)
            CProm = round(random.uniform(1.0,5.0))

            productos.append(Producto(nombre,precio,categoria,stock,CProm))

        return productos