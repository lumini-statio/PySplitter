import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

nombres = {
    'Emi': 488000,
    'Rome': 650000,
    'Claudio': 620000
}

alquiler = 355000
sueldos = []
nombres_list = list(nombres.keys())
porcentajes = []
dinero_correspondido = []


for _, item in enumerate(nombres.items()):
    sueldos.append(float(item[1]))

# suma total de todos los sueldos
sueldo_total = round(float(sum(sueldos)), 2)

# calcula porcentaje y dinero correspondiente a poner en el alquiler/compra
for i in range(len(nombres_list)):
    porcentaje: int = (sueldos[i] / sueldo_total) * 100
    porcentajes.append(round(porcentaje, 2))

    corresponde = (porcentaje / 100) * alquiler
    corresponde_redondeado = round(float(corresponde), 2)
    dinero_correspondido.append(corresponde_redondeado)


x = range(len(nombres_list))

# ancho de las barras
width = 0.35

plt.figure(figsize=(10, 6))

# barras para los sueldos
bar_sueldos = plt.bar([i - width / 2 for i in x], sueldos, width=width, color='skyblue', alpha=0.7, label='Sueldos')

# barras de dinero correspondiente
bar_dinero = plt.bar([i + width / 2 for i in x], dinero_correspondido, width=width, color='lightgreen', alpha=0.7, label='Dinero Correspondido')

# Sueldos sobre las barras
for i, bar in enumerate(bar_sueldos):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2000,
             f'${sueldos[i]:,.0f}', ha='center', va='bottom', fontsize=10)

# porcentajes sobre las barras
for i, bar in enumerate(bar_dinero):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 25000,
             f'{porcentajes[i]:.2f}%', ha='center', va='bottom', fontsize=10)

# dinero correspondiente sobre las barras
for i, bar in enumerate(bar_dinero):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f'${dinero_correspondido[i]:,.0f}', ha='center', va='bottom', fontsize=10)

plt.title('Comparación de Sueldos y Distribución del Dinero del Alquiler')
plt.xlabel('Empleado')
plt.ylabel('Cantidad en pesos')
plt.xticks(x, nombres_list)
plt.legend()
plt.show()