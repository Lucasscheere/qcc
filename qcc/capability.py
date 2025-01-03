import numpy as np
import plotly.graph_objects as go

def calculate_capability(data, lsl, usl):
    #Calcula métricas de capabilidade do processo (cp, cpk, Pp, Ppk)
    overall_mean = data.to_numpy().flatten().mean()
    overall_std = data.to_numpy().flatten().std()  # Desvio padrão amostral


    # cp e cpk
    cp = (usl - lsl) / (6 * overall_std)
    cpu = (usl - overall_mean) / (3 * overall_std)
    cpl = (overall_mean - lsl) / (3 * overall_std)
    cpk = min(cpu, cpl)


    return {
        "cp": float(cp),
        "cpk": float(cpk),
        "cpu": float(cpu),
        "cpl": float(cpl),
        "Mean": float(overall_mean),
        "StdDev": float(overall_std)}

def plot_capability(data, lsl, usl):
    stats = calculate_capability(data, lsl, usl)


    # Calculate mean and standard deviation
    mean = data.to_numpy().flatten().mean()
    std_dev = data.to_numpy().flatten().std()


    # Create a new plotly figure"""
    fig = go.Figure()  # Removed the rows and columns arguments

    # Create the histogram with density
    n, bins = np.histogram(data.to_numpy().flatten(), density=True)
    min_value = bins[0]
    max_value = bins[-1]


    fig.add_trace(go.Histogram(
        x=bins[:-1],  # Use only the lower bound of each bin for the histogram
        y=n,
        #nbinsx=20
    )
    )

    # Add the normal distribution curve
    x = np.linspace(min_value, max_value, 100)
    p = np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2)) / (std_dev * np.sqrt(2 * np.pi))
    fig.add_trace(go.Scatter(x=x, y=p, mode='lines', name='Distribuição Normal'))

    # Add the specification limits
    fig.add_vline(x=lsl, line_color='red', name=f'LSL ({lsl})')
    fig.add_vline(x=usl, line_color='red', name=f'USL ({usl})')
    fig.add_vline(x=mean, line_color='blue', name=f'Média ({mean:.2f})')

    # Set the title and labels
    fig.update_layout(
        title='Análise de Capabilidade do Processo',
        xaxis_title='Valores do Processo',
        yaxis_title='Frequência Relativa'
    )

    fig.show()