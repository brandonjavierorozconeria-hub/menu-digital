from flask import Flask, render_template

app = Flask(__name__)

menu = {
    "Comida 🔥": [
        {
            "nombre": "Alitas", 
            "precio": 80, 
            "img": "https://www.annarecetasfaciles.com/files/alitas-a-la-barbacoa-scaled.jpg",
            "desc": "Bañadas en tu salsa favorita, acompañadas de aderezo."
        },
        {
            "nombre": "Boneless", 
            "precio": 100, 
            "img": "https://1.bp.blogspot.com/-DB3G1LtvBjY/XwawK92iksI/AAAAAAABssY/eYoM2NIs09YxoISPCRxOw4xyeOOHeVGXwCLcBGAsYHQ/s1600/boneless-receta.jpg",
            "desc": "Pechuga de pollo crujiente sin hueso."
        },
        {
            "nombre": "Tenders", 
            "precio": 100, 
            "img": "https://airfryanytime.com/wp-content/uploads/2023/03/air-fryer-frozen-chicken-tenders-w1-768x512.jpg",
            "desc": "Tiras de pollo premium súper crujientes."
        },
        {
            "nombre": "Hamburguesa", 
            "precio": 85, 
            "img": "https://cdn.pixabay.com/photo/2024/10/19/02/29/burger-9131773_1280.jpg",
            "desc": "Con queso fundido, vegetales frescos y pan artesanal."
        },
    ],
    "Papas y Aros 🍟": [
        {
            "nombre": "Papas a la Francesa", 
            "precio": 50, 
            "img": "https://tse4.mm.bing.net/th/id/OIP.koKVPx9N046lvIXJ7Pf0wAHaEe?rs=1&pid=ImgDetMain&o=7&rm=3",
            "desc": "Clásicas y crujientes con un toque de sal."
        },
        {
            "nombre": "Papas Gajo", 
            "precio": 60, 
            "img": "https://th.bing.com/th/id/R.48f96494b02965dbfc3f2b1606f1413d?rik=HI3YvJrSlhZqkQ&pid=ImgRaw&r=0",
            "desc": "Sazonadas con especias de la casa."
        },
        {
            "nombre": "Aros de Cebolla", 
            "precio": 65, 
            "img": "https://www.pequerecetas.com/wp-content/uploads/2013/05/aros-de-cebolla-receta-800x571.jpeg",
            "desc": "Crujientes aros de cebolla empanizados."
        },
    ],
    "Bebidas y Extras 🥤": [
        {
            "nombre": "Refrescos", 
            "precio": 30, 
            "img": "https://tse3.mm.bing.net/th/id/OIP.V0ZvZ1TizCBuHiwmxOym7QHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
            "desc": "Variedad de sabores bien fríos."
        },
        {
            "nombre": "Agua Embotellada", 
            "precio": 20, 
            "img": "https://tse1.mm.bing.net/th/id/OIP.hIelWrzbteBZoKOsdtZ7sQHaFN?rs=1&pid=ImgDetMain&o=7&rm=3",
            "desc": "Hidratación natural 500ml."
        },
        {
            "nombre": "Salsa Extra", 
            "precio": 10, 
            "img": "https://tse2.mm.bing.net/th/id/OIP.1f49r_8WVCmrJ3fRD6N0cgHaE8?rs=1&pid=ImgDetMain&o=7&rm=3",
            "desc": "¿Quieres más picante? Elige tu salsa extra."
        },
    ]
}

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)