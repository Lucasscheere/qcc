import plotly.graph_objects as go

background_color = "#fff"
line_color = '#0592FF'


def calculate_x_bar(data):

    xbar = data.sum(axis=1) / data.columns.size
    overall_mean = xbar.mean()
    r = data.max(axis=1) - data.min(axis=1)
    rbar = r.mean()

    # Constante A2 para cartas X-barra (dependendo do tamanho do subgrupo)
    A2 = {
        2: 1.88, 3: 1.023, 4: 0.729, 5: 0.577, 6: 0.483,
        7: 0.419, 8: 0.373, 9: 0.337, 10: 0.308
    }.get(len(data.columns), 0)

    UCL_xbar = overall_mean + A2 * rbar
    LCL_xbar = overall_mean - A2 * rbar

    return xbar, rbar, LCL_xbar, UCL_xbar


def plot_xbar(data):
    # Calcular estatísticas e limites
    xbar, rbar, LCL_xbar, UCL_xbar = calculate_x_bar(data)

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=xbar, mode='lines+markers', name='Média', marker = {'color' : line_color}))
    fig.add_hline(y=UCL_xbar, line_dash="dash", line_color="red", annotation_text="UCL_xbar")
    fig.add_hline(y=LCL_xbar, line_dash="dash", line_color="red", annotation_text="LCL_xbar")
    fig.add_hline(y=xbar.mean(), line_dash="dash", line_color="green", annotation_text="Mean")
    fig.update_yaxes(range=[LCL_xbar, UCL_xbar])
    fig.update_layout(title='Gráfico X-barra', xaxis_title='Amostra', yaxis_title='Valor')

    #background
    fig.layout.plot_bgcolor = background_color

    #grids
    fig.update_xaxes(
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black')

    fig.update_yaxes(
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    showline=True, linewidth=1, linecolor='black')

    fig.show()


