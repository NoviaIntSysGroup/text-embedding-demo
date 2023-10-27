import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def hex_to_rgba(hex_color, alpha=1):
    # Remove the '#' character if present
    hex_color = hex_color.lstrip('#')

    # Convert the hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return f"rgba({r}, {g}, {b}, {alpha})"


def get_plotly_config():

    dpi = 600
    px_per_inch = 72  # Plotly appears to use 72 dpi, instead of 96 dpi
    cm_per_inch = 2.54

    alpha = 0.1
    colors = px.colors.qualitative.Plotly
    rgba_colors = [hex_to_rgba(hex_color, alpha) for hex_color in colors]

    # Plotly settings
    config = {
        'fontsize': 8,
        'png_scaling': dpi / px_per_inch,
        'px_per_cm': px_per_inch / cm_per_inch,
        'colors': colors,
        'rgba_colors': rgba_colors,
    }

    return config


def add_panel_annotation(fig, text, scale=1.0):
    fig.add_annotation(
        x=-0.05*scale, y=1.05,
        xref="paper", yref="paper",
        xanchor="right", yanchor="top",
        text="<b>" + text.upper() + "</b>",
        showarrow=False,
        borderpad=0,
        borderwidth=0,
        font=dict(size=10, color='black')
    )
    return fig


def get_scatter_plot(embeddings, topics, topic_similarities):

    config = get_plotly_config()

    margin = dict(
        l=1.2 * config['px_per_cm'],
        r=0.4 * config['px_per_cm'],
        t=0.4 * config['px_per_cm'],
        b=1.2 * config['px_per_cm'],
        pad=0
    )
    fig_settings = {
        "height": 6.6 * config['px_per_cm'],  #
        "width": 6.6 * config['px_per_cm'],
        "paper_bgcolor": "rgba(255, 255, 255, 0)",
        "margin": margin,
        "legend": dict(
            x=1, y=1,
            xanchor="right",
            yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.)",
            font=dict(size=config['fontsize']),
            itemwidth=30,
            tracegroupgap=10,
        ),
        "font": dict(size=config['fontsize']),
        "font_family": "arial",
        "title": dict(font=dict(size=config['fontsize'])),
    }

    ax_settings = {
        "showgrid": True,
        "showticklabels": True,
        "zeroline": False,
        "showline": False,
        "automargin": False,
        "titlefont": dict(size=config['fontsize']),
        "title_standoff": 0.1 * config['px_per_cm'],
    }

    topic_label = topic_similarities.argmax(axis=1)

    fig = go.Figure()
    for i in range(len(topics)):
        # Define a custom topic-specific color scale
        colorscale = [
            [0, config['rgba_colors'][i]],
            [1, config['colors'][i]]
        ]

        fig.add_trace(
            go.Scatter(
                x=embeddings[topic_label == i, 0],
                y=embeddings[topic_label == i, 1],
                hovertext=[str(i) for i in np.arange(embeddings.shape[0])],
                mode='markers',
                marker=dict(
                    color=topic_similarities[topic_label == i, i],
                    size=7,
                    opacity=0.8,
                    colorscale=colorscale,
                    line=dict(  # marker line (edge) settings
                        color=config['colors'][i],  # edge color
                        width=1  # edge thickness
                    )
                ),
                showlegend=False)
        )
    fig.update_xaxes(title=r"$z_1$", **ax_settings),
    fig.update_yaxes(title=r"$z_2$", **ax_settings),
    fig.update_layout(**fig_settings)

    return fig


def get_spider_plot(topics, topic_similarities, topic_breaks):

    config = get_plotly_config()

    margin = dict(
        l=2.5 * config['px_per_cm'],
        r=2.5 * config['px_per_cm'],
        t=0.4 * config['px_per_cm'],
        b=1.2 * config['px_per_cm'],
        pad=0
    )
    fig_settings = {
        "height": 6.6 * config['px_per_cm'],  #
        "width": 10 * config['px_per_cm'],
        "paper_bgcolor": "rgba(255, 255, 255, 0)",
        "margin": margin,
        "legend": dict(
            x=1, y=1,
            xanchor="right",
            yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.)",
            font=dict(size=config['fontsize']),
            itemwidth=30,
            tracegroupgap=10,
        ),
        "font": dict(size=config['fontsize']),
        "font_family": "arial",
        "title": dict(font=dict(size=config['fontsize'])),
    }

    topic_label = topic_similarities.argmax(axis=1)

    fig = go.Figure()
    # Add trace for the averages of all abstract grouped to each topic
    for i in range(len(topics)):
        r_tmp = topic_similarities[topic_label == i, :].mean(axis=0)

        fig.add_trace(
            go.Scatterpolar(
                r=np.append(r_tmp, r_tmp[0]),
                theta=topics + [topics[0]],
                mode='markers+lines',
                marker=dict(color=config['colors'][i]),
                showlegend=False,
            )
        )
    # Add mean over all abstracts in gray
    avg_topic_similarities = topic_similarities.mean(axis=0)
    fig.add_trace(
        go.Scatterpolar(
            r = np.append(avg_topic_similarities, avg_topic_similarities[0]),
            theta = topics + [topics[0]],
            mode = 'markers+lines',
            marker=dict(color='black'),
            name='Mean',
            showlegend=False,
        )
    )

    fig.update_polars(radialaxis_range=[0, 1], radialaxis_showticklabels=False)
    fig.update_polars(
        angularaxis_labelalias={k: v for k, v in zip(topics, topic_breaks)})
    fig.update_layout(**fig_settings)

    return fig


