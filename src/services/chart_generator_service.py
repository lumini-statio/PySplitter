import plotly.graph_objs as go


def calculate_charts(
        alquiler: float,
        values: dict,
        show_as: str
    ) -> go.Figure:
    nombres_list = list(values.keys())
    sueldos = list(values.values())
    porcentajes = []
    dinero_correspondido = []

    suma_total = round(sum(sueldos), 2)

    # calculate porcentages
    for sueldo in sueldos:
        porcentaje = round((sueldo / suma_total) * 100, 2)
        porcentajes.append(porcentaje)
        dinero = round((porcentaje / 100) * alquiler, 2)
        dinero_correspondido.append(dinero)

    trace_sueldos = go.Bar(
        x=nombres_list,
        y=sueldos,
        name='Sueldos',
        text=[f'${n}' for n in values.values()],
        textposition='outside',
        marker=dict(color='skyblue'),
    )

    if 'Percentage' in show_as:
        trace_dinero = go.Bar(
            x=nombres_list,
            y=dinero_correspondido,
            name='Porcentaje Correspondido',
            marker=dict(color='lightgreen'),
            text=[f'{p}%' for p in porcentajes],
            textposition='outside',
            textfont=dict(size=12),
        )
    elif 'Peso' in show_as:
        trace_dinero = go.Bar(
            x=nombres_list,
            y=dinero_correspondido,
            name='Dinero Correspondido',
            marker=dict(color='violet'),
            text=[f'${d}' for d in dinero_correspondido],
            textposition='outside',
        )

    layout = go.Layout(
        title='Comparación de Sueldos y Distribución del Dinero del Alquiler',
        xaxis=dict(title='Empleado'),
        yaxis=dict(title='Cantidad en pesos'),
        barmode='group'
    )

    fig = go.Figure(data=[trace_sueldos, trace_dinero], layout=layout)

    return fig
