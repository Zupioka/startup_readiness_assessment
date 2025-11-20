import plotly.graph_objects as go

FIGMA = {
    "bg":    "#004030",
    "teal":  "#4A9782",
    "cream": "#FFF9E5",
}

def radar_chart(levels: dict[str, int | float | str]) -> go.Figure:
    cats = ["CRL", "SRL", "BRL", "TMRL", "FRL", "IPRL", "TRL"]
    n = len(cats)
    theta_deg = [i * (360 / n) for i in range(n)] + [0]

    def to_num(v):
        try:
            return float(v)
        except Exception:
            return 0.0

    rvals = [to_num(levels.get(c, 0)) for c in cats]
    rvals_closed = rvals + [rvals[0]]

    fig = go.Figure()

    # --- Outer crown moved slightly outward & a bit thinner ---
    ring_thetas = list(range(0, 361, 2))
    fig.add_trace(go.Scatterpolar(
        r=[9.45]*len(ring_thetas),                 # was 9
        theta=ring_thetas,
        mode="lines",
        line=dict(color=FIGMA["teal"], width=16),  # was 22
        hoverinfo="skip",
        showlegend=False
    ))

    # Polygon
    fig.add_trace(go.Scatterpolar(
        r=rvals_closed,
        theta=theta_deg,
        mode="lines",
        fill="toself",
        line=dict(color="rgba(255,249,229,0.95)", width=2),
        fillcolor="rgba(255,249,229,0.55)",
        hovertemplate="%{customdata}: %{r}<extra></extra>",
        customdata=cats + [cats[0]],
        showlegend=False,
    ))

    # Numbers 1→9 on CRL spoke, nudged inward
    offset = 0.6
    fig.add_trace(go.Scatterpolar(
        r=[i - offset for i in range(1, 10)],
        theta=[0] * 9,
        mode="text",
        text=[str(i) for i in range(1, 10)],
        textposition="middle right",
        textfont=dict(color="#000000", size=10, family="Inter, sans-serif"),
        hoverinfo="skip",
        cliponaxis=False,
        showlegend=False
    ))

    fig.update_layout(
        polar=dict(
            domain=dict(x=[0.08, 0.92], y=[0.12, 0.90]),
            bgcolor="#4A9782",
            angularaxis=dict(
                rotation=0,
                direction="clockwise",
                tickmode="array",
                tickvals=[i * (360 / n) for i in range(n)],
                ticktext=cats,
                tickfont=dict(color=FIGMA["cream"], size=16, family="Inter, sans-serif"),
                ticks="",
                showline=False,
                showgrid=True,
                gridcolor="rgba(255,249,229,0.35)",
                gridwidth=1.2
            ),
            radialaxis=dict(
                range=[0, 9.6],                        # keeps 9 one ring inside the edge
                dtick=1,
                showticklabels=False,                  # <— HIDE default numeric labels
                ticks="",               # ← pas de petits traits
                ticklen=0,              # sécurité
                tickwidth=0,            # sécurité
                gridcolor="rgba(255,249,229,0.55)",
                linecolor="rgba(255,249,229,0.55)",
                showline=False
            )
        ),
        paper_bgcolor=FIGMA["bg"],
        plot_bgcolor=FIGMA["bg"],
        margin=dict(l=20, r=20, t=30, b=40),
        height=520
    )

    return fig
