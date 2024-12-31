import plotly.graph_objects as go


background_color = "#fff"
line_color = '#0592FF'



def calculate_r_chart(data):

    """Calcula a carta R."""
    r = data.max(axis=1) - data.min(axis=1)
    rbar = r.mean()

    # Constantes D3 e D4 para cartas R (dependendo do tamanho do subgrupo)
    constants = {
        2: (0, 3.267), 3: (0, 2.574), 4: (0, 2.282), 5: (0, 2.114),
        6: (0.076, 2.004), 7: (0.136, 1.924), 8: (0.184, 1.864),
        9: (0.223, 1.816), 10: (0.256, 1.777)
    }
    D3, D4 = constants.get(len(data.columns), 0)

    UCL_R_bar = D4 * rbar
    LCL_R_bar = D3 * rbar

    return r, rbar, UCL_R_bar, LCL_R_bar


def plot_r_chart(data):

    """Plota a carta R."""
    r, rbar, UCL_R_bar, LCL_R_bar = calculate_r_chart(data)

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=r, mode='lines+markers', name='Amplitude', marker = {'color' : line_color}))
    fig.add_hline(y=UCL_R_bar, line_dash="dash", line_color="red", annotation_text="UCL_R_bar")
    fig.add_hline(y=LCL_R_bar, line_dash="dash", line_color="red", annotation_text="LCL_R_bar")
    fig.add_hline(y=rbar.mean(), line_dash="dash", line_color="green", annotation_text="Mean")
    fig.update_yaxes(range=[LCL_R_bar, UCL_R_bar])
    fig.update_layout(title='Gráfico R-barra', xaxis_title='Amostra', yaxis_title='Valor')

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