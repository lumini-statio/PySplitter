from flet.plotly_chart import PlotlyChart
import plotly.graph_objs as go


def calculate_charts(alquiler: float, values: dict):
    nombres_list = list(values.keys())
    sueldos = list(values.values())
    porcentajes = []
    dinero_correspondido = []

    # Suma total de todos los sueldos
    suma_total = round(sum(sueldos), 2)

    # Calcular porcentajes y dinero correspondiente
    for sueldo in sueldos:
        porcentaje = round((sueldo / suma_total) * 100, 2)
        porcentajes.append(porcentaje)
        dinero = round((porcentaje / 100) * alquiler, 2)
        dinero_correspondido.append(dinero)

    # Crear gráfico de barras con Plotly
    trace_sueldos = go.Bar(
        x=nombres_list,
        y=sueldos,
        name='Sueldos',
        marker=dict(color='skyblue')
    )

    trace_dinero = go.Bar(
        x=nombres_list,
        y=dinero_correspondido,
        name='Dinero Correspondido',
        marker=dict(color='lightgreen'),
        text=[f'{p}%' for p in porcentajes],
        textposition='outside'
    )

    layout = go.Layout(
        title='Comparación de Sueldos y Distribución del Dinero del Alquiler',
        xaxis=dict(title='Empleado'),
        yaxis=dict(title='Cantidad en pesos'),
        barmode='group'
    )

    fig = go.Figure(data=[trace_sueldos, trace_dinero], layout=layout)

    return fig
